def two_sum(nums,target):
    hashmap_nums={}
    for i,element in enumerate(nums):
        complement=target-element 
        if complement in hashmap_nums:
            return [i,hashmap_nums[complement]]
        hashmap_nums[element]=i

nums=[2,7,11,15]
target=9
print(two_sum(nums,target))