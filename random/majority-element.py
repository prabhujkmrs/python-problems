"""
Problem Description

Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2.
"""
import math


def majorityElement(arr: list) -> int:
    size = len(arr)
    maxCount = 1
    elements = {}
    maxElement = arr[0]
    for v in arr:
        if v not in elements:
            elements[v] = 1
        else:
            elements[v] = elements.get(v) + 1
            if elements[v] > maxCount:
                maxCount = elements[v]
                maxElement = v

    if maxCount >= floor(size, 2):
        return maxElement


def floor(n, e):
    return int(math.floor(n / e))


print(majorityElement([2, 1, 2, 2, 3, 3]))
