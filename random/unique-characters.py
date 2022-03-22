# String with maximum number of unique characters
# Difficulty Level : Medium
# Last Updated : 07 Mar, 2022
# Given a list of strings, find the largest string among all. 
# The largest string is the string with the largest number of unique characters.


# Example: 

# Input : "AN KOW", "LO JO", "ZEW DO RO" 
# Output : "ZEW DO RO" 
# Explanation : 
# "ZEW DO RO" has maximum distinct letters.

# Input : "ROMEO", "EMINEM", "RADO"
# Output : "ROMEO" 
# Explanation : In case of tie, we can print
# any of the strings.

def largestString(input: list) -> str:
    str_map = dict()
    for v in input:
        str_map[unique_str_size(v)] = v
    return str_map[max(str_map.keys())]


def unique_str_size(s: str) -> int:
    str_set = set()
    for v in s:
        str_set.add(v)
    return len(str_set)


input = ["ROMEO", "EMINEM", "RADO"]
print(largestString(input))
