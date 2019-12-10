#!/usr/local/bin/python3

import numpy as np

def computeAngle(a, b):
	# Computer an angle between vector a->b and the horizontal
	ax, ay = a
	bx, by = b
	c = np.array([abs(bx), abs(ay)])
	
	ba = b - a
	bc = c - b
	
	if (by - ay) != 0:
		cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
	else:
		cosine_angle = 0
	angle = np.degrees(np.arccos(cosine_angle)) - 90.0
	
	return angle
	
	
def main():

	centerPoint = np.array([0,0])
	for i in range(-360,370, 10):
		p2 = (i , ((-360-i)*(i < 0)) + ((360-i)*(i >= 0)))
		print(p2, computeAngle(centerPoint,p2))
	print()
	print()

if __name__ == "__main__":
	main()
	

	


	