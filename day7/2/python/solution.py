#!/bin/python3
# solution for https://adventofcode.com/2022/day/7 part 2

# imports
import timeit
from collections import deque

# helper classes
class Directory:
    """represent a directory that can contain other files in a filesystem"""

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

    def get_complete_path(self):
        """return a string of the complete path from root"""
        if not self.parent:
            return self.name
        else:
            return self.parent.get_complete_path() + self.name + "/"

    def __hash__(self):
        """magic method for getting a hash of the object"""
        return self.get_complete_path().__hash__()


class File_:
    """represent a file in a filesystem (not a directory)"""

    def __init__(self, name, size):
        self.name = name
        self.size = size


class StackFrame:
    """represent an item in our queue for the size finding algorithm"""

    def __init__(self, item):
        self.item = item
        self.contents_ptr = 0
        self.size = 0


# helper functions
def read_input(input_file):
    """read input from file and convert it to lines of commands and output"""
    with open(input_file) as f:
        data = f.read().strip()
    lines = data.split("\n")
    return lines


def parse_lines(lines):
    """given lines of commands and output, construct a file system and list of directories"""
    wd = Directory("/", None)  # we assume the first line  is "$ cd /"
    directories = [wd]  # maintain a running list of all directories
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
            # read in lines as files until we reach the end of the input or the next command
            while line_pointer < len(lines) and lines[line_pointer][0] != "$":
                cur_line = lines[line_pointer]
                tokens = cur_line.split(" ")

                # is the item a directory or a file?
                if tokens[0] == "dir":
                    name = tokens[1]
                    parent = wd
                    item = Directory(name, parent)
                    directories.append(item)
                elif tokens[0].isnumeric():
                    size = int(tokens[0])
                    name = tokens[1]
                    item = File_(name, size)

                wd.contents.append(item)

                line_pointer += 1

    return directories


def get_directory_sizes(directories):
    """given a list of all directories in a file system, return a dictionary of their sizes"""
    dir_sizes = dict()  # dictionary of directories with known sizes
    queue = deque(
        map(StackFrame, directories)
    )  # queue of directories whose size we don't know yet

    # while there are still directories with unknown sizes
    while queue:
        frame = queue.pop()
        size_knowable = True  # flag to add frame back to the queue later if needed
        cur_dir, contents_ptr, cur_size = frame.item, frame.contents_ptr, frame.size
        # calculate size by going over items in the directory
        for i, item in enumerate(cur_dir.contents[contents_ptr:]):

            # if the item is a file, just add the size
            if type(item) == File_:
                cur_size += item.size

            # if the item is a directory and we know its size, just add it
            elif (type(item) == Directory) and (item in dir_sizes):
                subdir_size = dir_sizes[item]
                cur_size += subdir_size

            # otherwise, we'll need to get the size of the new directory first
            else:
                size_knowable = False
                break

        # if we've determined that the size is unknowable, stick it back in the queue
        if not size_knowable:
            frame.contents_ptr += i
            frame.size = cur_size
            queue.appendleft(frame)

        # otherwise, we have the final size
        else:
            dir_sizes[cur_dir] = cur_size

    return dir_sizes


def find_deletion_target(sizes, total_space, update_size):
    """find the smallest directory we can delete to free up enough space for the update"""

    # find the size of the root directory (aka the entire file system)
    for directory in sizes:
        if directory.name == "/":
            root = directory
            root_size = sizes[root]

    # figure out how much space we need to free
    max_filled_space = total_space - update_size
    space_to_free = root_size - max_filled_space

    # search through the directories and find the smallest one bigger than the space we need to free
    cur_target = root
    cur_target_size = root_size
    for directory, size in sizes.items():
        if space_to_free <= size < cur_target_size:
            cur_target = directory
            cur_target_size = size

    return cur_target


def solve():
    """return the solution to the challenge"""
    # mostly this function just exists to make benchmarking easier
    # constants
    INPUT_FILE = "../input.txt"
    TOTAL_SPACE = 70000000
    UPDATE_SIZE = 30000000

    lines = read_input(INPUT_FILE)
    directories = parse_lines(lines)
    sizes = get_directory_sizes(directories)
    target = find_deletion_target(sizes, TOTAL_SPACE, UPDATE_SIZE)

    return sizes[target]


def benchmark():
    """run the solution 10k times and output the number of seconds that took"""
    setup_code = "from __main__ import solve"
    test_code = "solve()"
    print(timeit.timeit(setup=setup_code, stmt=test_code, number=10000))


def main():
    print(solve())


if __name__ == "__main__":
    main()
