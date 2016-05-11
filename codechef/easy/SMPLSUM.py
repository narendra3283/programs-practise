__author__ = 'Narendra Avula'
'''
All submissions for this problem are available.

Read problems statements in Mandarin Chinese, Russian and Vietnamese as well.

Given a positive integer n, Chef has asked you to calculate the following sum in the most efficient way:

Here gcd(a,b) means greatest common divisor of two integers a and b.
Input

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.The only line describing each test case contains a single integer n, given to you by Chef.

Please note that input can be very large. So it's recommended to use fast IO methods.
Output

For each test case, output a single line containing one integer: answer to Chef's query.
Constraints and Subtasks

1 ? T ? 106
1 ? n ? 107


Subtask1(10 points): 1 ? sum of n over all testcases ? 107, TL=1.5s
Subtask2(20 points): 1 ? n ? 104,
TL=1s
Subtask3(70 points): No additional constraints,
TL=1s
Example

Input:
5
1
2
3
4
5

Output:
1
3
7
11
21
'''

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(gcd(10,11))

# for _ in range(int(input())):
#     number = int(input())
#     sum = 0
#     for i in range(number):
#         sum += number / gcd(i, number)
#     print(int(sum))