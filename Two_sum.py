'''
Problem:Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Author:https://github.com/Rajkumary5610

'''
from typing import List
class Solution:
    def Twosum(self,num: List[int], target: int) -> List[int]:
        n = len(num)
        for i in range(n-1):
            for j in range(i+1,n):
                if num[i] + num[j] == target:
                    return [i,j]
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)  
 
#n = list(input("Enter the list number's"))
#for i in range(10):
   # n = input()
t = int(input("Enter the target \n"))
s = Solution()
print(s.Twosum(lst,t))