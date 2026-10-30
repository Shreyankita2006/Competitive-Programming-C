def removeDuplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))

print("After removing duplicates:", removeDuplicates(nums))