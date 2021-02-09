# Author: Bojan G. Kalicanin
# Date: 11-Nov-2016
# Consider the following:
# A string, s, of length n where s=c0c1...cn-1.
# An integer, k, where k is a factor of n.
# We can split into subsegments where each subsegment, , consists of a contiguous block of characters in . Then, use each to create string such that:
#
#    The characters in are a subsequence of the characters in .
#    Any repeat occurrence of a character is removed from the string such that each character in occurs exactly once. In other words, if the character at some index in occurs at a previous index in , then do not include the character in string .
#
#Given and , print lines where each line denotes string .

s, n = input(), int(input())
for i in zip(*[iter(s)] * n):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in i if c not in d ]))
   

#Another method in simple language for beginners
n = int((len(string))/k)
l = [ ]
len_l = 0
for i in string:
   len_l = len_l + 1
   if i not in l:
      l.append(i)
   if len_l == k:
      print (''.join(l))
      len_l = 0
      l = [ ]
