import math
arr=['x','y','f','a','b']
def sorting(arr):
    for i in range(1,len(arr)):
        elem=ord(arr[i])
        k=i-1
        while k>=0 and elem<ord(arr[k]):
            arr[k+1]=arr[k]
            k-=1
        arr[k+1]=chr(elem)
def jump_search(ys,el):
    length=len(ys)
    jump=int(math.sqrt(length))
    left=0
    right=0
    while left <length and ord(ys[left])<=ord(el):
        right = min(length-1,left+jump)
        if ord(ys[left]) <=ord(el) and ord(ys[right])>=ord(el):
            break
        left+=jump
    if left>=length or ys[left]>el:
        return -1
    while left<= right and ord(ys[left])<=ord(el):
        if ys[left]==el:
            return left 
        left+=1
    return -1
(sorting(arr)) 
print(arr)
print(jump_search(arr,"x"))