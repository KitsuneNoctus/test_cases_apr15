'''
Introduction

Calculate the Hamming Distance between two DNA strands.

Your body is made up of cells that contain DNA. Those cells regularly
wear out and need replacing, which they achieve by dividing into daughter cells.
In fact, the average human body experiences about 10 quadrillion cell divisions in a lifetime!

When cells divide, their DNA replicates too. Sometimes during this process
mistakes happen and single pieces of DNA get encoded with the incorrect information.
If we compare two strands of DNA and count the differences between them we
can see how many mistakes occurred. This is known as the "Hamming Distance".

We read DNA using the letters C,A,G and T. Two strands might look like this:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

They have 7 differences, and therefore the Hamming Distance is 7.

The Hamming Distance is useful for lots of things in science, not just biology,
so it's a nice phrase to be familiar with :)
Implementation notes

The Hamming distance is only defined for sequences of equal length,
so an attempt to calculate it between sequences of different lengths should not work.
The general handling of this situation (e.g., raising an exception vs returning a special
 value) may differ between languages.
'''

def dna_comparison(arr, nums):
    count = 0
    for i, j in zip(nums, arr):
        if i != j:
            count += 1
    return count
#Good cases
# arr = "GAGCCTACTAACGGGAT"
# nums = "GAGCCTACTAACGGGAT"
arr = "GAGCCTACTAACGGGAT"
nums = "CATCGTAATGACGGCCT"
print(dna_comparison(arr, nums))
arr = "jk"
nums = ["j","k"]
# nums = {"j":1,"k":2}
print(dna_comparison(arr, nums))

#Bad Cases
# arr = 39640 - its not iterable
# nums = "Lazy"
#------
# arr = 45-6
# nums = "e"


print("----------")
# print(dna_comparison("", ""))



# Edge cases
# arr1 = ‘zdfgnghxnhgxn’ - not same length
# nums1 = ‘xvbgf’
# print(dna_comparison(arr1, nums1))
arr2 = ""
nums2 = "jarquevious"
print(dna_comparison(arr2, nums2))
arr3 = "JARQUEVIOUS" #Runs as different due to casing
nums3 = "jarquevious"
print(dna_comparison(arr3, nums3))
