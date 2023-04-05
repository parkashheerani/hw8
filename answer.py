"""
Questons 1:
========================================================================================================
Given an integer, write a function to determine if it is a power of 4. If so, return true ; otherwise, return false.
Integer n is a power of 4 such that: there exists an integer x such that n == 4^x
Example 1:
========================================
Input: n =4
Output: true
Example 2:
========================================
Input: n = 16
Output: true
Example 3:
========================================
Input: n = 64
Output: true
Example 4:
========================================
Input: n = 63
Output: false
"""
def isPowerOfFour(n):

    return ans

"""
Questons 2:
========================================================================================================
Given an array nums. The formula for calculating the "dynamic sum" of the array is: runningSum[i] = sum(nums[0]…nums[i]).
Please return the dynamic sum of nums.
Example 1:
========================================
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: The dynamic and computational process is [1, 1+2, 1+2+3, 1+2+3+4]
Example 2:
========================================
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: The dynamic and computational process is [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]
Example 3:
========================================
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
"""
def runningSum(nums):

    return nums

"""
Questons 3:
========================================================================================================
Give you an integer array nums whose subscript starts from 0. If the array is strictly incremented after exactly one element is deleted, please return true, otherwise return false. 
You also return true if the array itself is already strictly increasing.
The array nums is strictly increasing by definition: nums[i - 1] < nums[i] is satisfied for any subscript 1 <= i < nums.length.
Example 1:
========================================
Input: nums = [1,2,10,5,7]
Output: true
Explanation: Remove the 10 at subscript 2 from nums to get [1,2,5,7]. [1,2,5,7] is strictly increasing, so returns true .
Example 2:
========================================
Input: nums = [2,3,1,2]
Output: false
Explanation: 
[3,1,2] is the result of deleting the element at index 0.
[2,1,2] is the result of deleting the element at subscript 1.
[2,3,2] is the result obtained after deleting the element at subscript 2.
[2,3,1] is the result obtained after deleting the element at subscript 3.
None of the resulting arrays are strictly increasing, so false is returned.
Example 3:
========================================
Input: nums = [1,1,1]
Output: false
Explanation: 
The result after removing any element is [1,1].
[1,1] is not strictly increasing, so returns false .
Example 4:
========================================
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is already strictly increasing, so return true.
"""
def canBeIncreasing(nums):

    # write your code here
"""
Questons 4:
========================================================================================================
Design an algorithm to find how many trailing zeros n factorials have.
Example 1:
========================================
Input: 3
Output: 0
Explanation: 3! = 6, no zeros in the mantissa.
Example 2:
========================================
Input: 5
Output: 1
Explanation: 5! = 120, with 1 zero in the mantissa.
Example 3:
========================================
Input: n = 10
Output: 2
"""
def trailingZeroes(n):

    return count

