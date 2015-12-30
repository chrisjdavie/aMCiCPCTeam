'''
Solving the hackerrank AMP ICPC Team puzzle.

https://www.hackerrank.com/challenges/acm-icpc-team


-------------------
Problem Statement

You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can know that maximum number of topics.

Note Suppose a, b, and c are three different people, then (a,b) and (b,c) are counted as two different teams.

Input Format

The first line contains two integers, N and M, separated by a single space, where N represents the number of people, and M represents the number of topics. N lines follow.
Each line contains a binary string of length M. If the ith line's jth character is 1, then the ith person knows the jth topic; otherwise, he doesn't know the topic.

Constraints 
2<=N<=500 
1<=M<=500

Output Format

On the first line, print the maximum number of topics a 2-person team can know. 
On the second line, print the number of 2-person teams that can know the maximum number of topics.

Sample Input

4 5
10101
11100
11010
00101
Sample Output

5
2

-------------------

Never done bitwise calculations before. This exploits dictionaries
and bitwise stuff in Python. Is all interesting.

Created on 30 Dec 2015

@author: chris
'''

n, m = map(int, raw_input().strip().split(' '))


topicCounts = {}

for _ in range(n):
    topicT = str(raw_input().strip())
    topicInt = int(topicT,2)
    try:
        topicCounts[topicInt] += 1
    except(KeyError):
        topicCounts[topicInt] = 1

expertCombs = topicCounts.keys()

numExpertInMax = -1
countsMax = 0

for i, comb0 in enumerate(expertCombs):
    for comb1 in expertCombs[i:]:
        sumTopicsExpert = bin(comb0|comb1).count("1")
        if sumTopicsExpert > numExpertInMax:
            numExpertInMax = sumTopicsExpert
            countsMax = 0
        
        if sumTopicsExpert == numExpertInMax:
            countsMax += min([topicCounts[comb0],topicCounts[comb1]])
            if comb0 == comb1:
                countsMax -= 1

print numExpertInMax
print countsMax
        
        
#         print bin(comb0), bin(comb1), totalTopicsExpert


