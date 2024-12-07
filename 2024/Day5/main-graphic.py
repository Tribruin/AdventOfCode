from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    data = codeInput.read_lines()
    valid_page_orders = dict()
    for k, line in enumerate(data):
        if line == "":
            break
        i, j = map(int, line.split("|"))
        if i in valid_page_orders.keys():
            valid_page_orders[i].append(j)
        else:
            valid_page_orders[i] = [j]

    page_lists = list()
    for pages in data[k + 1 :]:
        page_lists.append(list(map(int, pages.split(","))))

    return (valid_page_orders, page_lists)


def check_page_order(pages_to_check, invalid_page_order):
    """check if any pages in pages to check are in invalid_page_order
    pages to check is all the pages BEFORE the check page
    invalid_page_order is a list of pages that should be after the check page"""

    # Check all pages BEFORE the current page
    for page_to_check in pages_to_check:
        if page_to_check in invalid_page_order:
            return False, pages_to_check.index(page_to_check)
    return True, None


def check_page_list(page_list, valid_page_orders):
    """Check a list of pages and ensure that it is valid"""
    # Check if page list is vaild
    for i, page in enumerate(page_list):
        if page in valid_page_orders.keys():
            valid, invalid_page_index = check_page_order(
                page_list[:i], valid_page_orders[page]
            )
            if not valid:
                return False, i, invalid_page_index
    return True, None, None


def part1(dataInput):

    valid_page_lists_middle_page = list()
    invalid_page_lists = list()
    page_orders, valid_page_dict = dataInput
    for page_list in valid_page_dict:
        valid, i, j = check_page_list(page_list, page_orders)
        mid_point = len(page_list) // 2
        page_str = list(map(str, page_list))
        if valid:
            # print(f"Valid Page: {pages}")
            valid_page_lists_middle_page.append(page_list[len(page_list) // 2])
            print(
                f"{GREEN}{",".join(page_str[:mid_point])},{BYELLOW}{page_str[mid_point]}{GREEN},{",".join(page_str[mid_point + 1:])}{ENDCOLOR}"
            )

        else:
            if i > j:
                j, i = i, j
            if i != 0:
                print(f"{GREEN}{",".join(page_str[:i])},", end="")
            print(f"{BRED}{page_str[i]}{GREEN},", end="")
            if i + 1 != j:
                print(f"{GREEN}{",".join(page_str[i+1:j])},", end="")
            print(f"{BRED}{page_str[j]}{GREEN}", end="")
            if j != len(page_str) - 1:
                print(f",{",".join(page_str[j+1:])}", end="")
            print()
            invalid_page_lists.append(page_list)

    print(f"Sum of mid-pages of valid pages: {sum(valid_page_lists_middle_page)}")
    return invalid_page_lists


def part2(dataInput, invalid_pages_to_fix):
    valid_page_dict, _ = dataInput
    valid_page_lists_middle_page = list()

    for page_list in invalid_pages_to_fix:
        valid_page_list = page_list.copy()
        valid = False
        while not valid:
            valid, i, j = check_page_list(valid_page_list, valid_page_dict)
            if not valid:
                valid_page_list[i], valid_page_list[j] = (
                    valid_page_list[j],
                    valid_page_list[i],
                )
        valid_page_lists_middle_page.append(valid_page_list[len(valid_page_list) // 2])
    print(sum(valid_page_lists_middle_page))


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    invalid_page_list = part1(dataInput)
    part2(dataInput, invalid_page_list)


if __name__ == "__main__":
    main()
