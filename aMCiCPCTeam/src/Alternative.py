'''
(solution by user https://www.hackerrank.com/SigmaSquared)

Downloaded from the comment section on hackerrank. Not tested, but
it uses combinations rather than looping over two loops - is sort
of more straight forwards than mine, for certain cases it will 
probably run faster. Would be interesting to combine them.

Edit:

It runs in close to idential time for all test cases. Worth taking
note of combinations, as that seems more pythonic. Apart from that,
it's all good.

Created on 30 Dec 2015

@author: chris
'''

import itertools
N,M = map(int,raw_input().strip().split())
knowledge=[]
for i in range(N):
    knowledge.append(int(raw_input().strip(),2))
mx = -float('inf')
teams=0
for p1,p2 in itertools.combinations(range(N),2):
    combined_topics = bin(knowledge[p1]|knowledge[p2]).count('1')
    if (combined_topics==mx):
        teams+=1
    elif (combined_topics>mx):
        mx = combined_topics
        teams=1

print mx
print teams