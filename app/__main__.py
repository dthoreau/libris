import sys

if __name__ == "__main__":
    sys.path.append('.python_packages/lib/site_packages')
    from .cli import main

    main(sys.argv[1:])
