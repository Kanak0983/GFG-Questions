def countPairsWithDiffK(self,arr, k):
        # code her
        arr.sort()
        c = 0
        hs = {}  # Initialize dictionary with a base case
        
        for i in arr:
            if i + k in hs:
                c += hs[i + k]
            elif (i - k) in hs:
                c += hs[i - k]
            if i not in hs:
                hs[i] = 1
            else:
                hs[i]+=1
        return c