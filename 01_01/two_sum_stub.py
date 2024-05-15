# 2-Sum Interview Problem

def two_sum_problem(arr, target):

    solution = []
    nums = {}

    for i in range(len(arr)):
        if target - arr[i] in nums:
            solution.append((nums[target - arr[i]], i))
        
        nums[arr[i]] = i

    # Error exception
    if len(solution) == 0:
        return None
    # Check if there is only one solution
    elif len(solution) == 1:
        return solution[0]
    
    
    return solution

print(two_sum_problem([1, 2, 3], 4))

assert two_sum_problem([1, 2, 3], 4) == (0, 2)
assert two_sum_problem([1234, 5678, 9012], 14690) == (1, 2)
assert two_sum_problem([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([2, 2], 4) in [(0, 1), (1, 0)]
#assert two_sum_problem([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (1, 4)]
