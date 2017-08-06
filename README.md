# Current-Programming-Application

This repository consists of the activities and projects that was made in our current programming application class. The programming application used is Python.

# June 30, 2017
Hours, Minutes, Seconds
	..* Write a program a program to convert an input number of seconds (integer) into hours, minutes, and seconds. Output the result.

4 and 7
	..* Print all the numbers between 1 and n(inclusive) that are both divisible 4 and multiple of 7. N is user input.

Products of Digits
	..* Ask the user to input a postive integer. Compute then print the product of its digits.

Fibonacci
	..* Ask the user to input a number then print all Fibonacci numbers less than or equal to that number.

# July 14, 2017
Append
	..* Create an empty list. Continously ask the user for a value, then using list.append() add the user input to the list until the user enerted "exit". Finally, print the resulting list.

Ingly
	..* Ask the user to input a string. If its length is atleast 3, add 'ing' to it. However, if it already ends in 'ing', add 'ly' instead. If the string length is less than three, leave it unchanged. Continue doing this until the user entered 'stop'. Note: Use str.endswith(sub) function.

Unite Union
	..* Write a function that takes one or more arrays and returns a new array of unique values in the order of the original provided arrays.
	..* In other words, all values present from all arrays should be included in their original order, but with no duplicates in the final array.
	..* The unique numbmers should be sorted by their original order, (the final array should not be sourted in numberical order)

Reverse Complement
	..* In genetic the reverse compliment of a sequence is formed by reversing the sequence and then taking the compliment of each symbol. The four nucleotides in DNA is Adenine (A), Cytosine (C), Guanine(G), and Thymine (T). This a bidirectional relation.
		A is complement ot T. T is a complement of A. C is a complement of G. G is a complement of C.
	..* For this exercise you need to complete the reverse complement function that takes a DNA string and returns the reverse complement.
	..* Note: You need to take care of lower and upper case. And if a sequence contains some invalid characters you need to return 'Invalid sequence'. You can use str[::-1] to reverse the string.

# July 21, 2017
Inventory
Given the following dictionary:

inventory = {
	'gold' : 500,
	'pouch' : ['flint', 'twine', 'gemstone'],
	'backpack' : ['xylophone', 'dagger', 'bedroll', 'bead loaf']
}

Do the following:
Add a key to inventory called 'pocket'.
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.
Sort the items in the list stored under the 'backpack' key.
Then remove dagger from the list of items stored under the 'backpack' key.
Add 50 to the number stored under the 'gold' key.
Sample run: {'pocket': ['seashell', 'strange berry', 'lint'], 'backpack': ['bedroll', 'bread loaf', 'xylophone'], 'pouch': ['flint', 'twine', 'gemstone'], 'gold': 550}

LetterCount
	..* Count the occurrence of each letter in a string and save the result in a dictionary. 
	..* The function d.get(key, default) might be useful

Letter and Digit count
	..* Write a funtion that accepts a sentence and calculate the number of letters and digits. Save the counts in a dictionary.
	..* Use function available on string to check whether a character is a letter of digit.

Permutation
	..* In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order. Create a list comprehension expression permutes even numbers from 0 through 4 with odd numbers from 0 through 4.

RemoveElements
	..* Using list comprehension, create a new list without the values in even indices numbers in [12,24,35,70,88,120,155].

VowelCount
	..* Using any functional programming tool, create a python script that will count the number of vowels in a text file. 

# AUGUST 02, 2017 - CODEWARS
Matrices: Adding Diagonal Products
	..* We have a square matrix M of dimension n x n that has positive and negative numbers in the ranges [-9,-1] and [0,9],( the value 0 is excluded).

	..* We want to add up all the products of the elements of the diagonals UP-LEFT to DOWN-BOTTOM, that is the value ofsum1; and the elements of the diagonals UP-RIGHT to LEFT-DOWN and that is sum2. Then, as a final result, the value of sum1 - sum2.

Base-2
	..* Negative-base systems can accommodate all the same numbers as standard place-value systems, but both positive and negative numbers are represented without the use of a minus sign (or, in computer representation, a sign bit); this advantage is countered by an increased complexity of arithmetic operations.

	..* To help understand, the first eight digits (in decimal) of the Base(-2) system is:
	[1, -2, 4, -8, 16, -32, 64, -128]

Direction Reduction
	..* Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

	..* The Haskell version takes a list of directions with data Direction = North | East | West | South. The Clojure version returns nil when the path is reduced to nothing. The Rust version takes a slice of enum Direction {NORTH, SOUTH, EAST, WEST}.