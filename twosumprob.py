arr=[1,2,3,7,8]
target=10
indexes=[]

for i in range(len(arr)-1):
    present_ind=[]
    for f in range(i+1,len(arr)):
        if arr[i]+arr[f]==10:
            present_ind=[i,f]
            indexes.append(present_ind) 
        else:
            continue
        

print(indexes)   