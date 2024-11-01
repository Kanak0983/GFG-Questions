class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        i,maxsum=0,0
        n=len(arr)
        j=n-1
        l=[]
        while i<=j:
            if i==j:
                l.append(arr[i])
            else:
                l.append(arr[i])
                l.append(arr[j])
            i+=1
            j-=1
        
        for i in range (n):
            maxsum+=abs(l[i]-l[(i+1)%n])
        return maxsum