def disjoint_arr(arr1,arr2,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if(arr1[i]==arr2[j]):
                return false
        return true
arr1=[1,2,3,4,5]
arr2=[6,7,8,9,10]
m=len(arr1)
n=len(arr2)
print("yes")if disjoint_arr(arr1,arr2,m,n)else("no")
    
