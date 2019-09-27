import os, argparse, stat, pwd


def main():
    parser = argparse.ArgumentParser(description='List args')
    parser.add_argument('path', nargs="?", default=os.getcwd())
    parser.add_argument('--show-tree', action="store_true", dest="show_tree", default=True)
    parser.add_argument('--show-stats', action="store_true", dest="show_stats", default=False)
    command_args = parser.parse_args()

    if command_args.path[0] == "/":
        file_path = command_args.path
    else:
        file_path = os.getcwd() + "/" + command_args.path

    list_files(0, file_path, command_args)


def list_files(print_level, directory, command_args):
    files = os.listdir(directory)
    spacing_string = "|"

    for i in range(print_level):
        spacing_string = spacing_string + "   |"

    for filename in files:
        print()
        lstat_out = os.lstat(directory + "/" + filename)
        print(spacing_string + "---", filename, end="")
        print(" owner=", pwd.getpwuid(lstat_out.st_uid)[0], sep="", end="")
        if stat.S_ISLNK(lstat_out.st_mode):
            print(" -> ", end=" ")
            if not os.path.exists(filename):
                print("invalid symlink", end=" ")
            else:
                print(os.readlink(filename), end=" ")
        if command_args.show_stats:
            if stat.S_ISREG(lstat_out.st_mode):
                print(" size=", lstat_out.st_size, end="", sep="")
                print(" mode=", stat.filemode(lstat_out.st_mode), end="", sep="")
        if command_args.show_tree:
            if stat.S_ISDIR(lstat_out.st_mode):
                list_files(print_level + 1, directory + "/" + filename, command_args)


if __name__ == '__main__':
    main()
    print()
