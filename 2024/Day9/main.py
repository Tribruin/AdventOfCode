from AOC import AOC, getDateYear
from TerminalColors import *

testing = False


def parse_input(codeInput: AOC):
    data = codeInput.read_file()
    idx = 0
    file_ptrs = list()
    free_space = list()
    for idx in data[::2]:
        file_ptrs.append(idx)
    for idx in data[1::2]:
        free_space.append(idx)
    return (file_ptrs, free_space)


def print_result(files: dict):

    sorted_list = list()
    for file_no, file_data in files.items():
        sorted_list.append((file_data["loc"], file_data["len"], file_no))
    sorted_list = sorted(sorted_list)
    last_loc = 0
    for start_loc, length, file_no in sorted_list:
        # start_loc = file_len["loc"]
        # length = file_len["len"]
        print("." * (start_loc - last_loc), end="")
        print(str(file_no) * length, end="")
        last_loc = start_loc + length
    print()


def part1(dataInput):
    file_ptrs, free_space = dataInput

    # Build the initial Disk Layout
    if len(free_space) % 2 == 1:  # If the free space is odd, add an extra 0
        free_space.append("0")
    file_list = list()
    total_files = 0
    for idx, ptr in enumerate(file_ptrs):
        file_list += [str(idx)] * int(ptr)
        total_files += int(ptr)
        file_list += ["."] * int(free_space[idx])

    idx = 0
    rev_idx = len(file_list) - 1
    while idx < total_files:
        if file_list[idx] != ".":
            idx += 1
        else:
            swapped = False
            while not swapped:
                if file_list[rev_idx] == ".":
                    rev_idx -= 1
                else:
                    file_list[idx], file_list[rev_idx] = (
                        file_list[rev_idx],
                        file_list[idx],
                    )
                    rev_idx -= 1
                    swapped = True
            idx += 1
            # print(" ".join(file_list[:20]), " | ", " ".join(file_list[-20:]))
            # print(" ".join(file_list))
    total_product = 0
    for i, x in enumerate(file_list):
        if x == ".":
            break
        total_product += i * int(x)
    print(total_product)


def part2(dataInput):

    file_lengths, free_spaces = dataInput
    free_spaces.append("0")
    files = dict()
    free_space_locs = dict()
    for idx in range(10):
        free_space_locs[idx] = list()

    # Create a dictionary that has the file_num as the key and then a dict of location and length
    location_idx = 0
    for file_idx, file_length in enumerate(file_lengths):
        files[file_idx] = {"loc": int(location_idx), "len": int(file_length)}
        location_idx += int(file_length)
        free_space = int(free_spaces[file_idx])
        free_space_locs[free_space].append(location_idx)
        location_idx += free_space
    # print_result(files)

    # last_poss_pos = files[9]["loc"] + files[9]["len"]
    for idx in range(len(files) - 1, 0, -1):

        # Find the length of the file that we need to find free space
        current_pos = files[idx]["loc"]
        len_of_file = files[idx]["len"]
        first_poss_pos = current_pos

        for idx2 in range(len_of_file, 10):
            if len(free_space_locs[idx2]) == 0:
                pass
            elif free_space_locs[idx2][0] < first_poss_pos:
                first_poss_pos, found_free_len = free_space_locs[idx2][0], idx2

        if first_poss_pos < current_pos:
            # print(
            #     f"Found a new space of {found_free_len} spaces for {idx}:{len_of_file} at {first_poss_pos}"
            # )
            files[idx]["loc"] = first_poss_pos
            free_space_locs[found_free_len].pop(0)
            remaining_free_space = found_free_len - len_of_file
            if remaining_free_space > 0:
                free_space_locs[remaining_free_space] = sorted(
                    free_space_locs[remaining_free_space]
                    + [first_poss_pos + len_of_file]
                )
        else:
            pass
            # print(f"No better position found for {idx}:{len_of_file} ")
        # print_result(files)
    pass

    # Calculate the Checksum
    sorted_list = list()
    for file_no, file_data in files.items():
        sorted_list.append((file_data["loc"], file_data["len"], file_no))
    sorted_list = sorted(sorted_list)
    checksum = 0
    for start_loc, length, file_no in sorted_list:
        for x in range(start_loc, start_loc + length):
            checksum += x * file_no
    print(checksum)


def main():
    # Get the path name and strip to the last 1 or 2 folder paths
    codeDate, codeYear = getDateYear()

    # global data
    codeInput = AOC(codeDate, codeYear, test=testing)
    dataInput = parse_input(codeInput)

    part1(dataInput)
    part2(dataInput)


if __name__ == "__main__":
    main()
