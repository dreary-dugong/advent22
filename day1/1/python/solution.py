# code for https://adventofcode.com/2022/day/1 problem 1
# program contants
INPUTFILE = "../input.txt"  # the file with our puzzle input


def main():
    # will contain our answer: the number of calories held by
    # the elf with the most calories of food in their inventory
    mostFoodCarried = 0

    # read our input to a string
    with open(INPUTFILE) as f:
        data = f.read().strip()

    # each elf has an inventory seperated by a blank line
    inventories = data.split("\n\n")
    for inventory in inventories:
        # each inventory consists of numbers of calories, one number per line
        calCounts = inventory.split("\n")
        # we sum these numbers to get the total calories in the inventory
        total = sum([int(calCount) for calCount in calCounts])
        # we compare this to our current maximum and change it if it's bigger
        mostFoodCarried = max(total, mostFoodCarried)

    print(mostFoodCarried)


if __name__ == "__main__":
    main()
