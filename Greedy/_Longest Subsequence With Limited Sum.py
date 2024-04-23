nums=sorted(accumulate(nums))
return sorted(bisect_right(nums,q) for q in queries)