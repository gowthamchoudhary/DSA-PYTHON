def maxSubarraySum( arr, k):
        # code here 
        n=len(arr)
        if n<k:
            return -1
        window_sum =0
        for i in range(k):
            window_sum = window_sum+arr[i]
            i=+1
        max_sum = window_sum
        for i in range(k,n):
            window_sum= window_sum+arr[i]-arr[i-k]
            max_sum = max(window_sum,max_sum)
            i=+1
        return max_sum

print(maxSubarraySum([100,200,300,400],2))