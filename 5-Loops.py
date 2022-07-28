'''
AIM: Practise using "for" and "while" loops in python.

Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers i<n, print i power 2.

Example
n=3

The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, n.

Constraints

1 <= n <=20

Output Format

Print n lines, one corresponding to each i.

Sample Input 0

5
Sample Output 0

0
1
4
9
16


SOLUTION:

'''
n = int(input("Enter the value of n: "))
i = 0

if n in range(1,21):
    for i in range(i,n):
        print (i**2)
else:
    print("The value of n is not between 1 and 20")

