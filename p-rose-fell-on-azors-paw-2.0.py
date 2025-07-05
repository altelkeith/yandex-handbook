num = int(input())
lo = len(str(num))
part_one = str(num)
part_one = part_one[0:(lo // 2)]
part_two = str(num)
if lo % 2 == 0:
    part_two = part_two[(lo // 2):lo]
else:
    part_two = part_two[((lo + 1) // 2):lo]

if part_one == part_two[::-1]:
    print("YES")
else:
    print("NO")