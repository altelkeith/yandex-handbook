a = int(input())
b = int(input())
c = int(input())
arr = [a, b, c]
arr_size = len(arr)
for i in range(0, arr_size - 1):
    swap = 0
    if arr[i] < arr[i + 1]:
        pass
    else:
        swap = arr[i]
        arr[i] = arr[i + 1]
        arr[i + 1] = swap

first_half = arr[0] ** 2 + arr[1] ** 2
second_half = arr[2] ** 2

if first_half == second_half:
    print("100%")
elif first_half < second_half:
    print("велика")
else:
    print("крайне мала")