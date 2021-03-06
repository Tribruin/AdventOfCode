#!/usr/local/bin/python3

#Test Input #1
# moves1 = "R8,U5,L5,D3"
# moves2 = "U7,R6,D4,L4"


# Test Input #2
# moves1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
# moves2 = "U62,R66,U55,R34,D71,R55,D58,R83"

# Test Input #3
# moves1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# moves2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

# Puzzle Input

moves1 = "R1009,U993,L383,D725,R163,D312,R339,U650,R558,U384,R329,D61,L172,D555,R160,D972,L550,D801,L965,U818,L123,D530,R176,D353,L25,U694,L339,U600,L681,D37,R149,D742,R762,U869,R826,U300,L949,U978,L303,U361,R136,D343,L909,U551,R745,U913,L566,D292,R820,U886,R205,D431,L93,D71,R577,U872,L705,U510,L698,U963,R607,U527,L669,D543,R690,U954,L929,D218,R490,U500,L589,D332,R949,D538,R696,U659,L188,U468,L939,U833,L445,D430,R78,D303,R130,D649,R849,D712,L511,U745,R51,U973,R799,U829,R605,D771,L837,U204,L414,D427,R538,U116,R540,D168,R493,U900,L679,U431,L521,D500,L428,U332,L954,U717,L853,D339,L88,U807,L607,D496,L163,U468,L25,U267,L759,D898,L591,U445,L469,U531,R596,D486,L728,D677,R350,D429,R39,U568,R92,D875,L835,D841,R877,U178,L221,U88,R592,U692,R455,U693,L419,U90,R609,U672,L293,U168,R175,D456,R319,D570,R504,D165,L232,D624,L604,D68,R807,D59,R320,D281,L371,U956,L788,D897,L231,D829,R287,D798,L443,U194,R513,D925,L232,U225,L919,U563,R448,D889,R661,U852,L950,D558,L269,U186,L625,U673,L995,U732,R435,U849,L413,D690,L158,D234,R361,D458,L271,U90,L781,U754,R256,U162,L842,U927,L144,D62,R928,D238,R473,U97,L745,U303,L487,D349,L520,D31,L825,U385,L133,D948,L39,U62,R801,D664,L333,U134,R692,U385,L658,U202,L279,D374,R489,D686,L182,U222,R733,U177,R94,D603,L376,U901,R216,D851,L155,D214,L460,U758,R121,D746,L180,U175,L943,U146,L166,D251,L238,U168,L642,D341,R281,U182,R539,D416,R553,D67,L748,U272,R257,D869,L340,U180,R791,U138,L755,D976,R731,U713,R602,D284,L258,U176,R509,U46,R935,U576,R96,U89,L913,U703,R833"
moves2 = "L1006,D998,R94,D841,R911,D381,R532,U836,L299,U237,R781,D597,L399,D800,L775,D405,L485,U636,R589,D942,L878,D779,L751,U711,L973,U410,L151,U15,L685,U417,L106,D648,L105,D461,R448,D743,L589,D430,R883,U37,R155,U350,L421,U23,R337,U816,R384,D671,R615,D410,L910,U914,L579,U385,R916,U13,R268,D519,R289,U410,L389,D885,L894,U734,L474,U707,L72,U155,L237,U760,L127,U806,L15,U381,L557,D727,L569,U320,L985,D452,L8,D884,R356,U732,L672,D458,L485,U402,L238,D30,R644,U125,R753,U183,L773,U487,R849,U210,L164,D808,L595,D668,L340,U785,R313,D72,L76,D263,R689,U604,R471,U688,R462,D915,R106,D335,R869,U499,R190,D916,R468,D882,R56,D858,L143,D741,L386,U856,R50,U853,R151,D114,L773,U854,L290,D344,L23,U796,L531,D932,R314,U960,R643,D303,L661,D493,L82,D491,L722,U848,L686,U4,L985,D509,L135,D452,R500,U105,L326,D101,R222,D944,L645,D362,L628,U305,L965,U356,L358,D137,R787,U728,R967,U404,R18,D928,L695,D965,R281,D597,L791,U731,R746,U163,L780,U41,L255,U81,L530,D964,R921,D297,R475,U663,L226,U623,L984,U943,L143,U201,R926,U572,R343,U839,R764,U751,R128,U939,R987,D108,R474,U599,R412,D248,R125,U797,L91,D761,L840,U290,L281,U779,R650,D797,R185,D320,L25,U378,L696,U332,R75,D620,L213,D667,R558,U267,L846,U306,R939,D220,R311,U827,R345,U534,R56,D679,R48,D845,R898,U8,R862,D960,R753,U319,L886,D795,R805,D265,R876,U729,R894,D368,R858,U744,R506,D327,L903,U919,L721,U507,L463,U753,R775,D719,R315,U128,R17,D376,R999,D386,L259,U181,L162,U605,L265,D430,R35,D968,R207,U466,R796,D667,R93,U749,L315,D410,R312,U929,L923,U260,R638"


def createWire(moves):
	movesArray=moves.split(",") 
	
	(x,y) = (0,0) 
	wireArray = [(0,0)]
	for move in movesArray:
		direction = move[0:1]
		distance =  int(move[1:])
				
		if direction == "U":
			y += distance
		elif direction == "D":
			y -= distance
		elif direction == "R":
			x += distance
		else:								# "L"
			x -= distance
		
		wireArray.append((x,y))
		
	return (wireArray)
	
def checkCrossPoints(wire1, wire2):

	def checkSegment(p1, p2, wire2Distance, currentBestPoint, currentBestDistance):
	# Check a segment of wire2 from p1 to p2 and see if wire1 crosses it anywhere
		
		
		x1, y1 = p1
		x2, y2 = p2
		
		if y1 == y2: 
		# Orientation is Horizontal on the segment so we only want the Vertical segments of wire1

			wire1Distance = 0
			for k in range(len(wire1)-1):
				xx1, yy1 = wire1[k]
				xx2, yy2 = wire1[k+1]
	
					
				if xx1 == xx2:
				# This is vertical segment, so check for crossings. 

# 					print("    Checking Vertical Segment for crossing at Y={3} on Wire 1 from ({0},{1}) to ({0},{2})".format(xx1, yy1, yy2, y1))
					if (x1 < xx1 < x2) or (x2 < xx1 <x1):
					# First, make sure the wire2 segment is within the wire1 horizontal range
						if (yy1 < y1 < yy2) or (yy2 < y1 < yy1): 
						# Now check if wire1 is crossing wire2 vertically
							allCrossPoints.append((xx1, y1))
							
							#Now lets figure out the travel distance to his point
							wire2NetDistance = (x1-xx1)
							wire1NetDistance = (y1-yy1)
							totalDistance = wire1Distance + wire2Distance + abs(wire1NetDistance) + abs(wire2NetDistance)
							print("        Found Crossing at ({0},{1}) with distance: {2} and offset ({3},{4})".format(xx1, y1, totalDistance, wire2NetDistance, wire1NetDistance))
							if totalDistance < currentBestDistance:
								currentBestDistance = totalDistance
								currentBestPoint = (xx1,y1)
								print("        ** New Best Travel Distance  **")
# 						else:
# 							print("        No Crossing Found")
# 					else:
# 						print("        No Crossing Found")
# 					
# 				else:
# 					print("    Checking Horizontal Segment for crossing at X={3} on Wire 1 from ({1},{0}) to ({2},{0})".format(yy1, xx1, xx2, x1))
# 					print("        Parallel Segment")
# 
				wire1Distance += (abs(xx2-xx1) + abs(yy2-yy1))
# 				print("           Wire1 Total Distance: {0}".format(wire1Distance))
				
		else: 
		# Orientation is Vertical on the segment, so we only want the Horizontal segments of wire1

			wire1Distance = 0
			for k in range(len(wire1)-1):
				xx1, yy1 = wire1[k]
				xx2, yy2 = wire1[k+1]
			
				if yy1 == yy2:
				# This is horizontal segment, so check for crossings
					
# 					print("    Checking Horizontal Segment for crossing at X={3} on Wire 1 from ({1},{0}) to ({2},{0})".format(yy1, xx1, xx2, x1))
					if (y1 < yy1 < y2 ) or (y2 < yy1 < y1):
					# This is horizontal segment, so check for crossings
						if (xx1 < x1 < xx2) or (xx2 < x1 < xx1):
							allCrossPoints.append((x1, yy1))

							#Now lets figure out the travel distance to his point
							wire2NetDistance = (y1-yy1)
							wire1NetDistance = (x1-xx1)
							totalDistance = wire1Distance + wire2Distance + abs(wire2NetDistance) + abs(wire1NetDistance)
							print("        Found Crossing at ({0}, {1}) with distance: {2} and offset ({3},{4})".format(x1, yy1, totalDistance, wire1NetDistance, wire2NetDistance))
							if totalDistance < currentBestDistance:
								currentBestDistance = totalDistance
								currentBestPoint = (x1,yy1)
								print("        ** New Best Travel Distance  **")				
# 						else:
# 							print("       (a) No Crossing Found")
# 					else:
# 						print("        (b) No Crossing Found")
# 
# 				else:
# 					print("    Checking Vertical Segment for crossing at Y={3} on Wire 1 from ({0},{1}) to ({0},{2})".format(xx1, yy1, yy2, y1))
# 					print("        Parallel Segment")

				wire1Distance += (abs(xx2-xx1) + abs(yy2-yy1))
# 				print("            Wire1 Total Distance: {0}".format(wire1Distance))
# 				print("----------------------------------------------")
		return currentBestPoint, currentBestDistance
				
				
	# Let's walk through the wire, segment by segment
	allCrossPoints = []
	bestTravelDistance=9999999							# Start with a real high distance
	finalDistancePoint=(0,0)
	wire2TotalDistance=0
	for i in range(len(wire2)-1):
		x1,y1 = wire2[i]
		x2,y2 = wire2[i+1]
		
				
		# Check to see if the wire is moving horizontal 
		if x1 == x2:
			# Check Vertical Segment
# 			print("Checking Vertical Segment on Wire 2 from ({0},{1}) to ({0},{2})".format(x1, y1, y2))
			finalDistancePoint, bestTravelDistance = checkSegment(wire2[i], wire2[i+1], wire2TotalDistance, finalDistancePoint, bestTravelDistance)
		else:
		# Check Horizontal Segment
# 			print("Checking Horizontal Segment on Wire 2 from ({0},{2}) to ({1},{2})".format(x1, x2, y1))
			finalDistancePoint, bestTravelDistance = checkSegment(wire2[i], wire2[i+1], wire2TotalDistance, finalDistancePoint, bestTravelDistance)

		wire2TotalDistance += (abs(x2-x1) + abs(y2-y1))
# 		print("        Wire2 Total Distance: {0}".format(wire2TotalDistance))
# 		print("===============================================")
# 		print("")


	return allCrossPoints, finalDistancePoint, bestTravelDistance
		

# Main Program
wire1Array = createWire(moves1)
wire2Array = createWire(moves2)



finalCrossPoints, finalPoint, finalDistance = checkCrossPoints(wire1Array, wire2Array)
# print(finalCrossPoints)

print("The shortest Distance is {0} steps at point {1}".format(finalDistance, finalPoint))

