class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        i = 0
        n = len(arr)
        for i in range(n):
            end_idx = i+k
            if i + k > n:
                end_idx = n
            if arr[i] in arr[i+1:end_idx+1]:
                return True
        return False