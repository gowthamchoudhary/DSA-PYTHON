outputs = [0,0]

count = {}
nums = [1,2,2,4]
for i in range(1,len(nums)+1):
    if i in count:
        count[i]+=1
    else:
        count[i]=1
for i in nums:
    if i in count:
        count[i]+=1
print(count)

# outputs[0] = [key for key in nums if count[key]>2]
# outputs[1] = [key for key in nums if count[key]==0]
for i in nums:
    if count[i]>2:
        outputs[0]=i
shadow=[i for i,value in count.items() if value==1]
outputs[1] = shadow[-1]
print(outputs)

