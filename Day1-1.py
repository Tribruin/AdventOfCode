#!/usr/bin/python3

# Read input from file

r = open("Day1-1Input.txt","r")
masses=r.readlines()

totalFuel = 0

for mass in masses:
	massInt=int(mass)
	
	# Divide by 3 (Round Down) and subtract 2
	fuel=(massInt//3)-2
	totalFuel+=fuel
	
print(totalFuel)
	

