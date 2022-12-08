#!/bin/python3
# solution for https://adventofcode.com/2022/day/7 part 1

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


def total_size_under_n(directories, n):
    """given a list of directories, return the total size of all directories under n in size"""
    total_size = 0  # total size of directories under 100k each, our output
    memo = dict()  # dictionary of directories with known sizes
    queue = deque(
        map(StackFrame, directories)
    )  # queue of directories whose size we don't know yet

    # while there are still directories with unknown sizes
    while queue:
        frame = queue.pop()
        size_known = True  # flag to add frame back to the queue later if needed
        cur_dir, contents_ptr, cur_size = frame.item, frame.contents_ptr, frame.size
        # calculate size by going over items in the directory
        for i, item in enumerate(cur_dir.contents[contents_ptr:]):

            # if the item is a file, just add the size
            if type(item) == File_:
                cur_size += item.size
                if cur_size > n:  # if at any point the size goes over n, stop counting
                    cur_size = None
                    break

            # if the item is a directory and we know its size, just add it
            elif (type(item) == Directory) and (item in memo):
                subdir_size = memo[item]
                if (subdir_size is None) or ((cur_size + subdir_size) > n):
                    cur_size = None
                    break
                else:
                    cur_size += subdir_size

            # otherwise, we'll need to get the size of the new directory first
            else:
                size_known = False
                break

        # if we've gone through all the items and know the size, add it to memo
        if size_known:
            memo[cur_dir] = cur_size
            if cur_size is not None:
                total_size += cur_size

        # otherwise, stick it at the end of the queue to resume later
        else:
            frame.contents_ptr += i
            frame.size = cur_size
            queue.appendleft(frame)

    return total_size


def solve():
    """return the solution to the challenge"""
    # mostly this function just exists to make benchmarking easier
    # constants
    INPUT_FILE = "../input.txt"
    N = 100000

    lines = read_input(INPUT_FILE)
    directories = parse_lines(lines)
    total_size_under_100k = total_size_under_n(directories, N)

    return total_size_under_100k


def benchmark():
    """run the solution 10k times and output the number of seconds that took"""
    setup_code = "from __main__ import solve"
    test_code = "solve()"
    print(timeit.timeit(setup=setup_code, stmt=test_code, number=10000))


def main():
    print(solve())


if __name__ == "__main__":
    main()
