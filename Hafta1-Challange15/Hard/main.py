def find_combinations(nums, target):
    results = []
    dfs(nums, target, [], results)
    return results

def dfs(nums, target, path, results):
    if target == 0:
        results.append(path)
        return

    if target < 0:
        return

    for i in range(len(nums)):
        dfs(nums[i:], target - nums[i], path + [nums[i]], results)

nums = [3,5,7,9,11,13]
target = int(input("Hedef sayıyı girin: "))

combinations = find_combinations(nums, target)

print("Hedef sayıya ulaşan kombinasyonlar:")
for combination in combinations:
    print(combination)
