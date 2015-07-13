""""Here is the problem: (link below) From Pythonist Contest
https://www.hackerrank.com/contests/pythonist/challenges/regex-1-validating-the-phone-number

Problem Statement

Let's dive into the interesting topic of regular expressions! You are given some inputs and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with 7, 8 or 9.

Input Format

The first line contains an integer N followed by N lines, each containing some string.

Output Format

For every string listed, print YES if it is a valid mobile number and NO if it isn’t.

Constraints 
1 <= N <= 10 
Mobile Number contains valid alpha-numeric characters 
2 <= len(Number) <= 15

""""

def validPhone():
    test_case = int(raw_input())
    number = [i for i in range(0, test_case)]

    for i in range(0, test_case):

        number[i] = raw_input()


    for i in range(0, test_case):
        if (len(number[i]) == 10) and (number[i].isdigit()) and ((number[i][0] == "7") or (number[i][0] == "8") or number[i][0] == "9"):
            print("YES")
        else:
            print("NO")




validPhone()
