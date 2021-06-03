'''Count of Substring: count of last 2 characters
ABC123.com is an online learning Academy. It helps children in building a strong foundation for future academic success by providing a comprehensive and engaging online curriculum
to greatly assist early learners to succeed in pre-k, kindergarten, and early elementary school programs.
Today Sitha has a new puzzle to solve in ABC123.com. In this puzzle, she has to identify the count of the substring in the String, she has to consider substring as last two 
characters of an original string and she has to take the count excluding the substring count. For Example: Consider the string "hiaahi", So substring will be "hi", Now she has 
to find the occurrences of "hi" in the string "hiaa" [substring (last 2 characters) is not considered], So count of hi in the string will be 
1. Help her to find the count of the substring.

Input and output format Input is a string. 
The output consists of a count of a substring. 
All text in bold corresponds to the input and the rest corresponds to output [Refer sample input and output format]. 
Sample Input and 
Output 1: Enter String hixxhi Substring count : 1 Sample Input and Output 2: Enter String axxxaaxx Substring count : 2'''


def last2(str):
  return len([i for i in range(len(str) - 2) if str[i:i+2] == str[-2:]])
str=input()
print(last2(str))
