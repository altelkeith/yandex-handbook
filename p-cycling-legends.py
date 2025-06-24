# Легенды велогонок возвращаются: кто быстрее?

petya = int(input())
vasya = int(input())
tolya = int(input())

my_arr = [(petya, "Петя"), (vasya, "Вася"), (tolya, "Толя")]

mins = my_arr[0][0]
maxs = my_arr[0][0]
for j in range(0, 2):
    for i in range(0, 3):
        if my_arr[i][0] <= mins:
            mins = my_arr[i][0]
            min_arr = my_arr[i][1]
        if my_arr[i][0] >= maxs:
            maxs = my_arr[i][0]
            max_arr = my_arr[i][1]
        if my_arr[i][0] != maxs and my_arr[i][0] != mins:
            middle_arr = my_arr[i][1]
    j = j + 1

new_arr = [min_arr, middle_arr, max_arr]

print(f"{new_arr[2]:^24}")
print(f"{new_arr[1]:^8}{' ':^16}")
print(f"{' ':^16}{new_arr[0]:^8}")
print(f"{'II':^8}{'I':^8}{'III':^8}")