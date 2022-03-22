# Given an array of integers greater than zero, 
# find if it is possible to split it in two subarrays (without reordering the elements), 
# such that the sum of the two subarrays is the same. Print the two subarrays.

# Examples : 

# Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
# Output :  { 1 2 3 4 } 
#           { 5 , 5 }

# Input : Arr[] = { 4, 1, 2, 3 }
# Output : {4 1}
#          {2 3}

# Input : Arr[] = { 4, 3, 2, 1}
# Output : Not Possible

def printTwoSubArrays(s: list):
    if split_point(s) == -1:
        print("Not possible")
        return

    for x in range(len(s)):
        if x == split_point(s):
            print(s[x])
        else:
            print(s[x], end=' ')


def split_point(s: list) -> int:
    left_sum = 0
    for i in range(0, len(s)):
        left_sum += s[i]
        right_sum = 0
        for j in range(i + 1, len(s)):
            right_sum += s[j]

        if left_sum == right_sum:
            return i

    return -1


printTwoSubArrays([4, 3, 2, 5])
