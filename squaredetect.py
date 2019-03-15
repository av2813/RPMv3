from skimage import data, feature, exposure
from PIL import Image
import numpy as np
import argparse
import cv2
import math
from shapely import geometry
from matplotlib import pyplot as plt
from scipy import spatial
import itertools
import matplotlib.cm as cm
import matplotlib.colors as cl
global mx, my


    

def send(X,Y,Mx,My):
	X = X
	Y = Y
	Mx = Mx
	My= My
	return(X, Y, Mx, My)


def click_event_lattice(event, x, y, flags, param):
	
    if event == cv2.EVENT_LBUTTONDOWN:
    	verts.append([x,y])
    	print(x,y)


def click_event_bars(event, x, y, flags, param):
	
    if event == cv2.EVENT_LBUTTONDOWN:
    	newbar.append([x,y])
    	print(x,y)
    if event == cv2.EVENT_RBUTTONDOWN:
    	removebar.append([[x,y]])
    	print(x,y)

def nothing(x):
	pass

def redo(im_with_keypoints, IslandProperties):
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.setMouseCallback("Keypoints", click_event_bars)
	cv2.waitKey(-1)

	for i in range(int(len(newbar)*0.5)):
		xd = int(newbar[2*i][0])
		yd = int(newbar[2*i][1])
		cd = (xd,yd)
		xl = int(newbar[(2*i)+1][0])
		yl = int(newbar[(2*i)+1][1])
		cl = (xl,yl)
		xa, ya = (xd+xl)/2, (yd+yl)/2 #assigns middle coordinates
		ca = (xa,ya)

		if (xd-xl) == 0: #fixes problem when divinding by zero in tan function.
			if yd<yl:
				xd +=0.1
			else:
				xl+=0.1

		if yd == yl:
			if xd>xl:
				deg = 0
			if xl>xd:
				deg = 180

		elif xd>xl and yd>yl:#first quad
			deg = math.degrees(math.atan((yd-yl)/(xd-xl))) 

		#print(deg)
		elif yd>yl and xd<xl:
			deg = math.degrees(math.atan((yd-yl)/(xl-xd)))  #second
			deg = 180-deg
		#print(deg)
		elif yd<yl and xd<xl:
			deg = math.degrees(math.atan((yl-yd)/(xl-xd))) 
			deg = 180+ deg

		#print(deg)
		elif yd<yl and xd>xl:
			deg = math.degrees(math.atan((yl-yd)/(xd-xl))) 
			deg = 360-deg

		if ( deg>45 and deg < 225):
			cv2.arrowedLine(im_with_keypoints, cd, cl, (0,0,255),2)

						
		elif (deg<45 or deg > 225):
			cv2.arrowedLine(im_with_keypoints, cd, cl, (255,0,0),2)

		if (deg<degree_change) or (deg>(360-degree_change)):
			mx = -1
			my = 0
			Mx.append(mx)
			My.append(my)

		elif (90-degree_change)<deg<(90+degree_change):
			mx = 0
			my = 1
			Mx.append(mx)
			My.append(my)

		elif (180-degree_change)<deg<(180+degree_change):
			mx = 1
			my = 0
			Mx.append(mx)
			My.append(my)

		elif (270-degree_change)<deg<(270+degree_change):
			mx = 0
			my = -1
			Mx.append(mx)
			My.append(my)


		IslandProperties.append([xa,ya,mx,my])
	return(IslandProperties)
			
	

	#for j in range(len(removebar)):


def connectdots(keypoints_dark, keypoints_light, im_with_keypoints, latticethresh, line_length_lower, line_length_upper, IslandProperties):
	for dark in keypoints_dark:
		xd = int(dark.pt[0]) #assigns x and y values and puts them as a coordinate
		yd = int(dark.pt[1])
		cd = (xd,yd)
		for light in keypoints_light:
			xl = int(light.pt[0])
			yl = int(light.pt[1])
			cl = (xl,yl)
			 
			xa, ya = (xd+xl)/2, (yd+yl)/2 #assigns middle coordinates
			
			
			
			pixelcolour = latticethresh[int(xa),int(ya)] #gets pixel colour on the lattice image
			
			if pixelcolour != 0: #if the pixel colour is not black, continue to line drawing.
				
				if (xd-xl) == 0: #fixes problem when divinding by zero in tan function.
					if yd<yl:
						xd +=0.1
					else:
						xl+=0.1

				if yd == yl:
					if xd>xl:
						deg = 0
					if xl>xd:
						deg = 180

				elif xd>xl and yd>yl:#first quad
					deg = math.degrees(math.atan((yd-yl)/(xd-xl))) 

			#print(deg)
				elif yd>yl and xd<xl:
					deg = math.degrees(math.atan((yd-yl)/(xl-xd)))  #second
					deg = 180-deg
			#print(deg)
				elif yd<yl and xd<xl:
					deg = math.degrees(math.atan((yl-yd)/(xl-xd))) 
					deg = 180+ deg

			#print(deg)
				elif yd<yl and xd>xl:
					deg = math.degrees(math.atan((yl-yd)/(xd-xl))) 
					deg = 360-deg
				
				if line_length_lower < ((xd-xl)**2 + (yd-yl)**2)**0.5 < line_length_upper and ((deg<degree_change) or ((90-degree_change)<deg<(90+degree_change)) or ((180-degree_change)<deg<(180+degree_change)) or ((270-degree_change)<deg<(270+degree_change)) or (deg>(360-degree_change))):
					
					
					if ( deg>45 and deg < 225):
						cv2.arrowedLine(im_with_keypoints, cd, cl, (0,0,255),2)

						
					elif (deg<45 or deg > 225):
						cv2.arrowedLine(im_with_keypoints, cd, cl, (255,0,0),2)

					if (deg<degree_change) or (deg>(360-degree_change)):
						mx = -1
						my = 0

					if (90-degree_change)<deg<(90+degree_change):
						mx = 0
						my = 1

					if (180-degree_change)<deg<(180+degree_change):
						mx = 1
						my = 0

					if (270-degree_change)<deg<(270+degree_change):
						mx = 0
						my = -1

				
					IslandProperties.append([xa,ya,mx,my])
	return(IslandProperties)

def finalcoordinates(cfinal,degreefinal):
	for i in range(len(cfinal)):
		print(cfinal[i], degreefinal[i])

def lattice(Xmin, Ymin, Xmax, Ymax, X1, Y1):

	latticelength=Xmax-Xmin
	vertexlength = X1-Xmin
	dimension = latticelength/vertexlength
	dimension = int(dimension)
	xgrid=np.linspace(0,(2*dimension)+1,(2*dimension)+1)
	ygrid=np.linspace(0,(2*dimension)+1,(2*dimension)+1)
	xv, yv = np.meshgrid(xgrid,ygrid)
	print(xv, yv)

	for i in range(dimension+1): #creates x range and y range for coordinates
		Xlist.append(int(Xmin + ((Xmax-Xmin)/dimension)*(i))) 
		Ylist.append(int(Ymin + ((Ymax-Ymin)/dimension)*(i)))
	C=[] 
	for i in range(len(Xlist)): #creates a list of the vertex coordinates
		for j in range(len(Ylist)):
			C.append((Xlist[i-1],Ylist[j-1]))

	#DRAWS CIRCLES ON THE VERTICES
	for vertex in C:
		cv2.circle(lattice,(vertex[0],vertex[1]), circle_radius, (0,0,0), -1)

global latticeim, imageim
latticethresh = []
Ylist =[]
closestbar=[]
verts = []
newbar = []
removebar= []
Mx=[]
My=[]
Xvertex = []
Yvertex = []
Xbar=[]
Ybar=[]
Xlist=[]
Ylist=[]
Bargrid=[]
deg = 0
threshold = 180
threshold_mask = 50
line_length_upper =25
line_length_lower = 10
dimension = 5
circle_radius = 5
degree_change = 15

IslandProperties = []



def square(lattice, image):

	#SETS ARGUEMENTS
	#ap = argparse.ArgumentParser()
	#ap.add_argument("-i", "--image", help = "path to the image file")

	#ap.add_argument("-l", "--lattice", help = "path to the image file")
	#args = vars(ap.parse_args())

	#TAKES LATTICE IMAGE
	lattice = cv2.imread(lattice)

	# initiates click event for the lattice image
	cv2.imshow("click",lattice)
	cv2.setMouseCallback("click", click_event_lattice)
	cv2.waitKey(-1)

	#SETS MIN AND MAX FOR EACH CLICK
	Xmin, Ymin, X1, Y1, X2, Y2, Xmax, Ymax= verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], verts[3][0], verts[3][1]
	#calculates lattice length and dimension
	latticelength=Xmax-Xmin
	vertexlengthX = X1-Xmin
	vertexlengthY = Y2 - Ymin

	dimension = int(round((latticelength/vertexlengthX),0))
	print(dimension)
	vertexlengthY = (Ymax-Ymin)/dimension


	#DRAWS CIRCLES ON THE VERTICES
	for i in range(dimension+1): #creates x range and y range for vertex coordinates coordinates
		Xlist.append(int(Xmin + ((Xmax-Xmin)/dimension)*(i))) 
		Ylist.append(int(Ymin + ((Ymax-Ymin)/dimension)*(i)))
	C=[] 
	for i in range(len(Xlist)): #creates a list of the vertex coordinates
		for j in range(len(Ylist)):
			C.append((Xlist[i-1],Ylist[j-1]))


	for vertex in C:
		cv2.circle(lattice,(vertex[0],vertex[1]), circle_radius, (0,0,0), -1)



	#SHOWS THE RESULT AND WAITS FOR A KEY TO PROCEED
	cv2.imshow("lattice w/ vertex",lattice)
	cv2.waitKey(-1)

	#SETS THE UPPER LIMIT FOR A CONNECTION TO BE A PERCENTAGE OF THE ISLAND DISTANCE
	line_length_upper = ((Xmax-Xmin)/dimension)*0.7
	line_length_lower = ((Xmax-Xmin)/dimension)*0.5


	#READS THE MFM FILE AND CONVERTS IT TO GREYSCALE
	image = cv2.imread(image)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray_lattice =cv2.cvtColor(lattice, cv2.COLOR_BGR2GRAY)

	#DRAWS CROSSES ON THE VERTICES TO SEPERATE BLOBS WHICH ARE MERGED
	for vertex in C:
		cv2.line(gray,(int((vertex[0]-line_length_upper)),int((vertex[1] - line_length_upper))),(int(vertex[0]+line_length_upper),int(vertex[1] + line_length_upper)), 158,1)
		cv2.line(gray,(int((vertex[0]-line_length_upper)),int((vertex[1] + line_length_upper))),(int(vertex[0]+line_length_upper),int(vertex[1] - line_length_upper)), 158,1)

	#DRAWS GREY RECTANGLES AROUND THE EDGE OF THE LATTICE.
	cv2.rectangle(gray,(0,int(Ymin-line_length_upper*0.5)), (10000,0), 158, -1)
	cv2.rectangle(gray,(0,int(Ymax+line_length_upper*0.5)), (10000,10000), 158, -1)
	cv2.rectangle(gray,(int(Xmin-line_length_upper*0.5),0), (0,10000), 158, -1)
	cv2.rectangle(gray,(int(Xmax+line_length_upper*0.5),0), (10000,10000), 158, -1)


	#ALLOWS THE USER TO CONTROL THE LEVEL OF THRESHOLD TO MAKE WHITE SPOTS BLACK. (NEED TO MOVE THIS TO A FUNCTION)
	cv2.namedWindow("WHITE SPOTS TO BLACK (ESC WHEN DONE)")
	hh='Max'
	hl='Min'
	wnd = "WHITE SPOTS TO BLACK (ESC WHEN DONE)"
	cv2.createTrackbar("Max", wnd,0,255,nothing)

	while(1):
		hul=cv2.getTrackbarPos("Max", wnd)
		#ret,thresh1 = cv2.threshold(image,hul,huh,cv2.THRESH_BINARY)
		ret,whitedetect = cv2.threshold(gray,hul,250,cv2.THRESH_BINARY_INV)
		#ret,thresh3 = cv2.threshold(image,hul,huh,cv2.THRESH_TRUNC)
		#ret,thresh4 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO)
		#ret,thresh5 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO_INV)
	   # cv2.imshow(wnd)
		#cv2.imshow("thresh1",thresh1)
		cv2.imshow('original', gray)
		cv2.moveWindow('original',0,0)
		cv2.imshow(wnd, whitedetect)
		#cv2.imshow("thresh3",thresh3)
		#cv2.imshow("thresh4",thresh4)
		#cv2.imshow("thresh5",thresh5)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break
	cv2.destroyAllWindows()
	#Rectangle drawing


	#ALLOWS THE USER TO CONTROL THE LEVEL OF THRESHOLD TO MAKE BLACK SPOTS BLACK. (NEED TO MOVE THIS TO A FUNCTION)
	cv2.namedWindow("BLACK SPOTS TO BLACK (ESC WHEN DONE)")
	hh='Max'
	hl='Min'
	wnd = "BLACK SPOTS TO BLACK (ESC WHEN DONE)"
	cv2.createTrackbar("Max", wnd,0,255,nothing)


	while(1):
		hul=cv2.getTrackbarPos("Max", wnd)

		#ret,thresh1 = cv2.threshold(image,hul,huh,cv2.THRESH_BINARY)
		ret,blackdetect = cv2.threshold(gray,hul,250,cv2.THRESH_BINARY_INV)
		blackdetect = cv2.bitwise_not(blackdetect)
		#ret,thresh3 = cv2.threshold(image,hul,huh,cv2.THRESH_TRUNC)
		#ret,thresh4 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO)
		#ret,thresh5 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO_INV)
	   # cv2.imshow(wnd)
		#cv2.imshow("thresh1",thresh1)
		cv2.imshow('ORIGINAL', gray)
		cv2.moveWindow('ORIGINAL',0,0)
		cv2.imshow(wnd,blackdetect)
		#cv2.imshow("thresh3",thresh3)
		#cv2.imshow("thresh4",thresh4)
		#cv2.imshow("thresh5",thresh5)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break
	cv2.destroyAllWindows()
	#Rectangle drawing

	#ALLOWS THE USER TO CONTROL THE LEVEL OF THRESHOLD FOR THE LATTICE. (NEED TO MOVE THIS TO A FUNCTION)
	cv2.namedWindow("Lattice threshold (esc when done)")
	hh='Max'
	hl='Min'
	wnd = "Lattice threshold (esc when done)"
	cv2.createTrackbar("Max", wnd,0,255,nothing)

	while(1):
		hul=cv2.getTrackbarPos("Max", wnd)
		ret,latticethresh = cv2.threshold(gray_lattice,hul,250,cv2.THRESH_BINARY)
		#ret,blackdetect = cv2.threshold(gray_lattice,hul,huh,cv2.THRESH_BINARY_INV)
		#ret,thresh3 = cv2.threshold(image,hul,huh,cv2.THRESH_TRUNC)
		#ret,thresh4 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO)
		#ret,thresh5 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO_INV)
	   # cv2.imshow(wnd)
		#cv2.imshow("thresh1",thresh1)
		cv2.imshow('Lattice', lattice)
		cv2.moveWindow('Lattice', 0,0)
		cv2.imshow(wnd,latticethresh)
		#cv2.imshow("thresh3",thresh3)
		#cv2.imshow("thresh4",thresh4)
		#cv2.imshow("thresh5",thresh5)
		k = cv2.waitKey(1) & 0xFF
		if k == ord('m'):
			mode = not mode
		elif k == 27:
			break
	cv2.destroyAllWindows()
	#Rectangle drawing



	#PARAMETERS FOR THE BLOB DETECTION

	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 1
	params.maxThreshold = 300

	# Filter by Area.
	params.filterByArea = True
	params.minArea = 20

	# Filter by Circularity
	params.filterByCircularity = False
	params.minCircularity = 0.1

	# Filter by Convexity
	params.filterByConvexity = False
	params.minConvexity = 0.87

	# Filter by Inertia
	params.filterByInertia = False
	params.minInertiaRatio = 0.01

	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)



	#DETECTS DARK AND WHITE BLOBS AND STORES THEM TO ARRAYS
	keypoints_dark = detector.detect(blackdetect)
	keypoints_light = detector.detect(whitedetect)

	keypoints_total = keypoints_light + keypoints_dark

	#DRAWS CIRCLES ON THE ORIGINAL IMAGE WHERE THE BLOBS ARE
	im_with_keypoints = cv2.drawKeypoints(gray, keypoints_total, np.array([]), (46,155,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	final_im = im_with_keypoints
	# Draw detected blobs as red circles.

	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures

	# the size of the circle corresponds to the size of blob

	#PARAMETERS FOR THE NEXT PART.
	IslandProperties = []
	BarCoordinates = []
	BarCoordinatesend = []
	mxfinal = []
	myfinal = []

	connectdots(keypoints_dark, keypoints_light, im_with_keypoints, latticethresh, line_length_lower, line_length_upper, IslandProperties)
					

				 	
	redo(im_with_keypoints, IslandProperties)
	print(IslandProperties)
	cv2.imshow("",im_with_keypoints)
	cv2.waitKey(-1)
	grid(IslandProperties, im_with_keypoints, vertexlengthX, dimension, vertexlengthY, Xmin, Ymin)

def grid(IslandProperties, im_with_keypoints, vertexlengthX, dimension, vertexlengthY, Xmin, Ymin):
	#Changes X and Y into coordinate system
	for Island in IslandProperties:
		for n in range(2*dimension+1):
			if (Island[0] - vertexlengthX/4) < ((Xmin + 0.5*n*vertexlengthX) or (Xmax - 0.5*((2*dimension)-n)*vertexlengthX)) < (Island[0] + vertexlengthX/4):
				Island[0] = n
		for m in range(2*dimension+1):
			if (Island[1] - vertexlengthY/4) < ((Ymin + 0.5*m*vertexlengthY) or (Ymax - 0.5*((2*dimension)-n)*vertexlengthY)) < (Island[1] + vertexlengthY/4):
				Island[1] = m
		if (Island[0]%2==0 and Island[1]%2==0) or (Island[0]%2!=0 and Island[1]%2!=0):
			print(Island)




	IslandProperties.sort(key=lambda x: x[0])
	#Removes any duplicates
	b = list()
	for sublist in IslandProperties:
	    if sublist not in b:
	        b.append(sublist)
	print(b)

	#Defines coordinates for mx and my
	X = np.zeros((2*dimension+1, 2*dimension+1))
	Y = np.zeros((2*dimension+1, 2*dimension+1))
	Mx = np.zeros((2*dimension+1, 2*dimension+1))
	My = np.zeros((2*dimension+1, 2*dimension+1))

	#Assigns mx and my into corresponding point through x and y coordinates
	for x in range(2*dimension+1):
		X[:,x] = (2*dimension - x)
	for y in range(2*dimension+1):
		Y[y] = (y)

	for bar in b:
		print(bar[0], bar[1])
		Mx[(bar[0]),(2*dimension - (bar[1]))]=bar[2]
		My[(bar[0]),(2*dimension - (bar[1]))]=bar[3]
		if bar[0]%2 == 0 and bar[1]%2==0:
			Mx[(bar[1]),(bar[0])]=0
			My[(bar[1]),(bar[0])]=0



	np.savez('Outfile', X, Y, Mx, My)


		





