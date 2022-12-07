#!/bin/python3
# solution for https://adventofcode.com/2022/day/7 part 1

# constants
INPUT_FILE = "../input.txt"

# helper classes
class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.contents = []
        self.parent = parent

    def get_item(self, item_name):
        """return the first file or directory in contents that matchs the given name"""
        for item in self.contents:
            if item.name == item_name:
                return item
        return None

    def get_size(self):
        """return the total size of all contents of the directory"""
        # this current implementation means a lot of rework in the script later on
        # this hasn't been a problem because the input is small but it could be fixed if needed
        size = 0
        for item in self.contents:
            if type(item) == Directory:
                size += item.get_size()
            elif type(item) == File_:
                size += item.size
        self.size = size
        return size

    def get_complete_path(self):
        """return a string of the complete path from root"""
        if not parent:
            return self.name
        else:
            return self.parent.get_complete_path() + self.name + "/"

    def __hash__(self):
        return self.get_complete_path.__hash__()


class File_:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def main():
    # read input
    with open(INPUT_FILE) as f:
        data = f.read().strip()
    lines = data.split("\n")

    # parse commands and output to make file system
    wd = Directory("/", None)  # we assume the first line  is "$ cd /"
    directories = []  # maintain a running list of all directories
    line_pointer = 1
    while line_pointer < len(lines):
        cur_line = lines[line_pointer]
        tokens = cur_line.split(" ")
        command = tokens[1]

        # cd command
        if command == "cd":
            arg = tokens[2]
            if arg == "..":
                wd = wd.parent
            else:
                wd = wd.get_item(arg)
            line_pointer += 1

        # ls command
        elif command == "ls":

            # get containing files from output
            line_pointer += 1
            while line_pointer < len(lines) and lines[line_pointer][0] != "$":
                cur_line = lines[line_pointer]
                tokens = cur_line.split(" ")

                # is the file a directory or a file?
                if tokens[0] == "dir":
                    item = Directory(tokens[1], wd)
                    directories.append(item)
                elif tokens[0].isnumeric():
                    item = File_(tokens[1], int(tokens[0]))
                else:
                    print(f"Attempt to create file from {cur_line}")
                wd.contents.append(item)

                line_pointer += 1

    # with the file system fully constructed, we get the sizes of all directories
    total_under_100k = 0  # the total size of all directories whose size is under 100k
    for directory in directories:
        size = directory.get_size()
        if size < 100000:
            total_under_100k += size

    print(total_under_100k)


if __name__ == "__main__":
    main()
