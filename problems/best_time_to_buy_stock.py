# Best Time to Buy and Sell Stock
# You are given an array of prices where prices[i] is the price of agiven stock on an ith day.
# You want to maximize your profit by choosing a single day to buyone stock and choosing a different day in the future to sell thatstock.
# Return the maximum profit you can achieve from this transaction.If you cannot achieve any profit, return 0
# Input
# : prices = [7,1,5,3,6,4]
# Output
# : 5
# Explanation
# : Buy on day 2 (price = 1) and sell on day 5 (price = 6),profit = 6-1 = 5.
# PRACTICE NOW
# PRACTICE NOW                     
# --------------------------------------------------------------------------------------------------------------------
prices = [7455,102,520.555,352,69.3,400,1050,254,1000,635.54]
def best_stock_time(arr):
    max = 0
    best  = {"best_time":[]}

    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]-arr[i]>=max:
                max = arr[j]-arr[i]
                best['best_time'] = [i,j]
   
    return best['best_time']
result = best_stock_time(prices)
print(f"best time to buy the stock is :day {result[0]}")
print(f"best time to sell the stock is :day {result[1]+1}")

