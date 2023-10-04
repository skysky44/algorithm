def solution(nums):
    N = len(nums)
    new_nums = set(nums)
    if len(new_nums) >= N//2 :
        return N//2
    else:
        return len(new_nums)