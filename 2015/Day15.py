from itertools import combinations

props_to_check_1 = ["capacity", "durability", "flavor", "texture"]
props_to_check_2 = ["capacity", "durability", "flavor", "texture", "calories"]


def get_combos(sum_N, count):
    array = list()
    top_count = sum_N - count + 1
    for i in range(count):
        array += list(range(1, top_count + 1))
        top_count = top_count // 2

    array_combos = list(combinations(array, count))

    valid_combos = [x for x in array_combos if sum(x) == 100]
    return valid_combos


def part1():
    high_value = 0
    for combo in combos:
        combo_value = 1
        for prop in props_to_check_1:
            prop_value = 0
            for n, x in enumerate(combo):
                prop_value += x * ingredients[n][prop]
            if prop_value <= 0:
                prop_value = 0
            combo_value *= prop_value
        if combo_value > high_value:
            high_value = combo_value
    print(high_value)


def part2():
    high_value = 0
    for combo in combos:
        combo_value = 1
        for prop in props_to_check_1:
            prop_value = 0
            for n, x in enumerate(combo):
                prop_value += x * ingredients[n][prop]
            if prop_value <= 0:
                prop_value = 0
            combo_value *= prop_value
        cal_value = 0
        for n, x in enumerate(combo):
            cal_value += x * ingredients[n]["calories"]

        if cal_value == 500 and combo_value > high_value:
            high_value = combo_value
    print(high_value)


ingredients = list()
with open("Day15-Input.txt") as f:
    lines = f.read().splitlines()
    for line in lines:
        temp = dict()
        ingredient, props = line.split(": ")
        temp["name"] = ingredient
        for prop in props.split(","):
            name, value = prop.split()
            temp[name] = int(value)
        ingredients.append(temp)

combos = get_combos(100, len(ingredients))
# part1()
part2()