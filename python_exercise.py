# Write a program that takes in a list of words 
# and return the vowels present in a string
def words(word):
    vowels  = ("a","i","u","o","e")
    count=""
    character = sorted(word)
    for char in character:
        if char in (vowels):
            count+=char
            
    return count
word="darthewiermq"
print(words(word))

# Given two lists, write a function to find the common elements between them and
# return them in a new list.

def elements(a,b):
    result = [i for i in a if i in b]
    return result

a = [10,30,4,89]
b = [10,90,75,12]
print(elements(a,b))


# Given a list of integers, write a function that 
# returns the smallest element in the list.

def find_smallest(numbers):
    smallest = numbers[0] 
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

my_list = [3, 7, 1, 9, 4, 2]
smallest_num = find_smallest(my_list)
print(smallest_num) 


      
   

