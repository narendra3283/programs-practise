__author__ = 'narendra'
'''
Your friend Max has written a string S in your textbook. The string consists of lowercase latin letters. The problem is that Max is not good at writing at all! Especially, you never know if he wanted to write "w" or two consecutive "v". Given the string S, return the minimum and maximum length of a word which can be represented by it. The input string represents what you initially think the word is.

Input format:

In the first line there is a single integer N denoting the length of word S. In the second line there is string S itself.

Output format:

Print the minimum and the maximum length of a word which can be represented by S. Output these numbers in one line and separate them by a single space.

Constraints:

N <= 106

SAMPLE INPUT
5
avwvb
SAMPLE OUTPUT
4 6
Explanation
The shortest word which can be represented by this string is awwb, while the longest is avvvvb
'''

string_length = int(raw_input())
string = raw_input()
v_count = string.count('v')
w_count = string.count('w')
min_string = 0
max_string = 0
if ( v_count % 2 ) == 0:
    min_string += 0