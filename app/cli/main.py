import sys
import argparse
from app.cli.commands import create_route


def main():
    parser = argparse.ArgumentParser(description="Resume Analyzer CLI")
    subparsers = parser.add_subparsers(
        dest='command', help='Available commands')

    # Create route command
    route_parser = subparsers.add_parser(
        'create-route', help='Create a new API route')
    route_parser.add_argument('name', nargs='?', help='Route name (e.g., users, posts)')
    route_parser.add_argument(
        '--prefix', help='Route prefix (default: /route_name)')
    route_parser.add_argument(
        '--tags', nargs='+', help='Route tags (default: [route_name])')

    args = parser.parse_args()

    if args.command == 'create-route':
        try:
            create_route(args.name, args.prefix, args.tags)
        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
