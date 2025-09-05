import os
import re
from pathlib import Path


def create_route(route_name: str = None, prefix: str = None, tags: list = None):
    """Create a new API route file and update main.py"""
    
    # Interactive prompts if not provided
    if not route_name:
        route_name = input("Enter route name (e.g., users, posts): ").strip()
    
    # Validate route name
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', route_name):
        raise ValueError("Route name must be a valid Python identifier")
    
    if not prefix:
        default_prefix = f"/{route_name}"
        prefix = input(f"Enter route prefix (default: {default_prefix}): ").strip() or default_prefix
    
    if not tags:
        default_tags = [route_name]
        tags_input = input(f"Enter tags separated by spaces (default: {route_name}): ").strip()
        tags = tags_input.split() if tags_input else default_tags
    
    # Paths
    project_root = Path(__file__).parent.parent.parent
    routes_dir = project_root / "app" / "api" / "routes"
    main_file = project_root / "app" / "api" / "main.py"
    route_file = routes_dir / f"{route_name}.py"
    
    # Check if route already exists
    if route_file.exists():
        raise FileExistsError(f"Route {route_name} already exists")
    
    # Create route file content
    route_content = f'''from fastapi import APIRouter

router = APIRouter(prefix="{prefix}", tags={tags})


@router.get("/")
async def get_{route_name}():
    return {{"message": "Get {route_name}"}}


@router.post("/")
async def create_{route_name}():
    return {{"message": "Create {route_name}"}}


@router.put("/{{item_id}}")
async def update_{route_name}(item_id: int):
    return {{"message": f"Update {route_name} {{item_id}}"}}


@router.delete("/{{item_id}}")
async def delete_{route_name}(item_id: int):
    return {{"message": f"Delete {route_name} {{item_id}}"}}
'''
    
    # Write route file
    route_file.write_text(route_content)
    
    # Update main.py
    main_content = main_file.read_text()
    
    # Add import
    import_line = f"from app.api.routes import {route_name}"
    if import_line not in main_content:
        # Find the last import line and add after it
        lines = main_content.split('\n')
        import_index = -1
        for i, line in enumerate(lines):
            if line.startswith('from app.api.routes import'):
                import_index = i
        
        if import_index >= 0:
            lines.insert(import_index + 1, import_line)
        else:
            # Add after existing imports
            for i, line in enumerate(lines):
                if line.startswith('from app.api.routes'):
                    lines.insert(i + 1, import_line)
                    break
        
        main_content = '\n'.join(lines)
    
    # Add router inclusion
    include_line = f"api_router.include_router({route_name}.router)"
    if include_line not in main_content:
        lines = main_content.split('\n')
        # Find the last include_router line and add after it
        include_index = -1
        for i, line in enumerate(lines):
            if 'include_router' in line:
                include_index = i
        
        if include_index >= 0:
            lines.insert(include_index + 1, include_line)
        else:
            # Add at the end
            lines.append(include_line)
        
        main_content = '\n'.join(lines)
    
    # Write updated main.py
    main_file.write_text(main_content)
    
    print(f"✅ Created route: {route_name}")
    print(f"📁 File: {route_file}")
    print(f"🔄 Updated: {main_file}")