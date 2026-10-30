def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))

print("Single number:", singleNumber(nums))