def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i

    return [-1, -1]

n = int(input("Enter number of elements: "))
nums = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

print("Indices:", twoSum(nums, target))