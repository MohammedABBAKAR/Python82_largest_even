

#* Find The Largest Even Number
# *Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.

# !Examples
# ?largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10

# ?largest_even([1, 3, 5, 7]) ➞ -1

# ?largest_even([0, 19, 18973623]) ➞ 0
# !Notes
# !Consider using the modulo operator % or the bitwise and operator &.



def largest_even(lst):
   x=  sorted(lst)
   lsit1 =[y for y in x if y %2==0]
   if lsit1 ==[]:
      return -1
   else:
      return max(lsit1)
print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
print(largest_even([1, 3, 5, 7]))
print(largest_even([0, 19, 18973623]))


#! /////////////////////////////////////////////////////////////////////////
def largest_even(lst):
    largest = -1  # Initialize the largest even number as -1
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            if num > largest:  # Compare with the current largest even number
                largest = num
    return largest
