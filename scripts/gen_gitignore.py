#!/bin/python3
def main():
    """generate a gitignore file for this repository by adding target and .vscode directories for the rust implementations of all days"""
    """There's definitely a better way to do this with patterns but git's documentation is bewildering to me"""
    with open("./.gitignore", "w") as f:
        for day in range(1, 25 +1):
            for part in range(1, 2 +1):
                package_path = f"day{day}/{part}/rust/advent22day{day}part{part}/"
                f.write(package_path + "target/*\n")
                f.write(package_path + ".vscode/*\n")
    print("Successfully Generated .gitignore")

if __name__ == "__main__":
    main()
