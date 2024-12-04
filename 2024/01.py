def main(left_list, right_list):
    """
    1. left_list and right_list and store them as two lists
    What's a list?
    > An list has a length. Arrays are denoted by `[]`.
    The array [1,2,3] has a length of 3. An array in indexable. The array [1,2,3] position 0 is 1.
    What is position 2 in the above list?
    > 3

    2. We will sort left_list and right_list in ascending order
        a) call a library sort function
        b) implement a bubble sort algorithm

    3. Subtract the left_list from the right_list. Take the absolute value. | a - b |. Store this result
    into distance_list

    4. Add all entries of distance_list together

    5. Profit
    """


with open("01.inp", "r") as f:
    rows = f.readlines()
left_list = []
right_list = []
for row in rows:
    left_list.append(int(row.split("   ")[0]))
    right_list.append(int(row.split("   ")[1]))


print(rows)
print(len(rows))
left_list.sort()
right_list.sort()
print("left list:")
print(left_list)
print("right_list:")
print(right_list)

distance_list = []
for i in range(len(left_list)):
    print(i)
    distance_list.append(abs(left_list[i] - right_list[i]))

print(distance_list)

total_distance = 0
for distance in distance_list:
    total_distance = total_distance + distance
    print(total_distance)
