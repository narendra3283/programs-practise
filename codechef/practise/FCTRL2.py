__author__ = 'CustomFurnish'
'''
All submissions for this problem are available.

A bit-manipulation-tutorial for this problem is now available on our blog. Click here to read it.

You are asked to calculate factorials of some small positive integers.
Input

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.
Output

For each integer n given at input, display a line with the value of n!
Example

Sample input:
4
1
2
5
3
Sample output:
1
2
120
6
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for _ in range(int(input())):
    print(factorial(int(input())))