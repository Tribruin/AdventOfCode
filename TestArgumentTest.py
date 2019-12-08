#!/usr/local/bin/python3

from  io import StringIO 
from itertools import permutations
import sys


# class RedirectedStdout:
#     def __init__(self):
#         self._stdout = None
#         self._string_io = None
# 
#     def __enter__(self):
#         self._stdout = sys.stdout
#         sys.stdout = self._string_io = StringIO()
#         return self
# 
#     def __exit__(self, type, value, traceback):
#         sys.stdout = self._stdout
# 
#     def __str__(self):
#         return self._string_io.getvalue()
# 
# out = RedirectedStdout()


# oldStdOut = sys.stdout 
# sys.stdout = myStdOut = StringIO()
# 
# print("one")
# print("two")
# print("three")
# print("This is direct to stderr", file = sys.stderr )
# 
# 
# print("Reset Stdout")
# sys.stdout = oldStdOut
# 
# print("Redirecting Stdin")
# 
# # x = myStdOut
# myStdOut.seek(0)
# sys.stdin = myStdOut
# 
# x = input()
# print(x)
# # print(myStdOut.readline().strip())
# # print(myStdOut.readline().strip())
# # print(myStdOut.tell())
# # 	
# 	
# myStdOut.close()


basePhaseSettings = ['0','1','2','3','4']

# def generateCode(phaseSettings):
# 	returnValue = []
# 	print(len(phaseSettings), phaseSettings)
# 	for x in range(len(phaseSettings)):
# 		if phaseSettings:
# 			returnValue.append(phaseSettings.pop(x))
# 			print(phaseSettings)
# 			returnValue += generateCode(phaseSettings)
# 		else:
# 			return returnValue	
# 	print(returnValue)
	
combos = list(permutations(basePhaseSettings, len(basePhaseSettings)))
print(combos)



