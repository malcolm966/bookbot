def find_minimum(nums):
    if nums:
        minimum = float('inf')
        for n in nums:
            if n < minimum:
                minimum = n
        return minimum
    return None