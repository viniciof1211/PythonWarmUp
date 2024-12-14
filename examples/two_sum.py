# Find two numbers in a list that add up to a specified target
def two_sum(nums, target):
    visited = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in visited:
            return [diff,num]
        visited[num] = i