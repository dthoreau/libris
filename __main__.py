import sys

if __name__ == "__main__":
    # This is needed to make python -m app work from the command line on
    # azure containers.
    #
    sys.path.append('.python_packages/lib/site-packages')


    main(sys.argv[1:])


def main(args) -> None:
    pass
