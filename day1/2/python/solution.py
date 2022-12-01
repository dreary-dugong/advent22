# code for https://adventofcode.com/2022/day/1 problem 2
# program contants
INPUTFILE = "../input.txt"  # the file with our puzzle input


def main():
    # will contain the total calories held by each of the
    # top 3 elves who hold the most calories
    top3 = [0, 0, 0]

    # read our input to a string
    with open(INPUTFILE) as f:
        data = f.read().strip()

    # each elf has an inventory seperated by a blank line
    inventories = data.split("\n\n")
    for inventory in inventories:
        # each inventory consists of numbers of calories, one number per line
        calCounts = inventory.split("\n")
        # we sum these numbers to get the total calories in the inventory
        curTotal = sum([int(calCount) for calCount in calCounts])

        # see if current inventory has more calories than any of our top 3
        # if it does, insert it
        for i, topInv in enumerate(top3):
            if curTotal > topInv:
                top3.insert(i, curTotal)
                top3.pop()  # remove extra number after insert
                break

    print(sum(top3))


if __name__ == "__main__":
    main()
