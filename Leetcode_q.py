#1. Two Sum
nums = [2,7,11,15]
target = 9
d = {}
for i, x in enumerate(nums):
    #print(x-target)
    if target-x in d:
        print(d[target-x],i)
    d[x]=i
print('t')