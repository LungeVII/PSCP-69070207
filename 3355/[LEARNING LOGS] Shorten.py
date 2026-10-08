"""kkk"""

nums = []
while True:
    x = int(input())
    if x == -1:
        break
    nums.append(x)

if not nums:
    print("")
else:
    ranges = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            ranges.append((start, prev))
            start = prev = n
    ranges.append((start, prev))

    parts = []
    for a, b in ranges:
        if a == b:
            parts.append(str(a))
        else:
            parts.append(f"{a}-{b}")

    print(", ".join(parts))
