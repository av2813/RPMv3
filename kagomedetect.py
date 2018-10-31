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

def redo(im_with_keypoints):
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.setMouseCallback("Keypoints", click_event_bars)
	cv2.waitKey(-1)

	for i in range(int(len(newbar)*0.5)):
		xl = int(newbar[2*i][0])
		yl = int(newbar[2*i][1])
		cl = (xl,yl)
		xd = int(newbar[(2*i)+1][0])
		yd = int(newbar[(2*i)+1][1])
		cd = (xd,yd)
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

		elif xd>xl and yd>yl:#4th quad
			deg = math.degrees(math.atan((yd-yl)/(xd-xl))) 
			deg = 360-deg

	#print(deg)
		elif yd>yl and xd<xl:
			deg = math.degrees(math.atan((yd-yl)/(xl-xd)))  #third
			deg = 180+deg
	#print(deg)
		elif yd<yl and xd<xl:
			deg = math.degrees(math.atan((yl-yd)/(xl-xd)))  #second
			deg = 180- deg

	#print(deg)
		elif yd<yl and xd>xl:
			deg = math.degrees(math.atan((yl-yd)/(xd-xl)))  #first

		if ( deg>45 and deg < 225):
			cv2.arrowedLine(im_with_keypoints, cl, cd, (0,0,255),2)

						
		elif (deg<45 or deg > 225):
			cv2.arrowedLine(im_with_keypoints, cl, cd, (255,0,0),2)

		if (deg<degree_change) or (deg>(360-degree_change)):
			mx = 1
			my = 0
			cv2.arrowedLine(im_with_keypoints, cl, cd, (255,0,0),2)
			print(deg)

		if (60-degree_change)<deg<(60+degree_change):
			mx = 0.5
			my = 0.866025
			cv2.arrowedLine(im_with_keypoints, cl, cd, (255,182,0),2)

		if (120-degree_change)<deg<(120+degree_change):
			mx = -0.5
			my = 0.866025
			cv2.arrowedLine(im_with_keypoints, cl, cd, (178,255,0),2)

		if (180-degree_change)<deg<(180+degree_change):
			mx = -1
			my = 0
			cv2.arrowedLine(im_with_keypoints, cl, cd, (0,242,255),2)

		if (240-degree_change)<deg<(240+degree_change):
			mx = -0.5
			my = -0.866025
			cv2.arrowedLine(im_with_keypoints, cl, cd, (0,0,255),2)

		if (300-degree_change)<deg<(300+degree_change):
			mx = 0.5
			my = -0.866025
			cv2.arrowedLine(im_with_keypoints, cl, cd, (255,0,255),2)



		IslandProperties.append([xa,ya,mx,my])

	

	#for j in range(len(removebar)):


def connectdots(keypoints_dark, keypoints_light, im_with_keypoints):
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
			
			if pixelcolour != 255: #if the pixel colour is not black, continue to line drawing.
				
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

				elif xd>xl and yd>yl:#4th quad
					deg = math.degrees(math.atan((yd-yl)/(xd-xl))) 
					deg = 360-deg

			#print(deg)
				elif yd>yl and xd<xl:
					deg = math.degrees(math.atan((yd-yl)/(xl-xd)))  #third
					deg = 180+deg
			#print(deg)
				elif yd<yl and xd<xl:
					deg = math.degrees(math.atan((yl-yd)/(xl-xd)))  #second
					deg = 180- deg

			#print(deg)
				elif yd<yl and xd>xl:
					deg = math.degrees(math.atan((yl-yd)/(xd-xl)))  #first
					
				
				
				if line_length_lower < ((xd-xl)**2 + (yd-yl)**2)**0.5 < line_length_upper and ((deg<degree_change) or ((60-degree_change)<deg<(60+degree_change)) or ((120-degree_change)<deg<(120+degree_change)) or ((180-degree_change)<deg<(180+degree_change)) or ((240-degree_change)<deg<(240+degree_change)) or ((300-degree_change)<deg<(3000+degree_change)) or (deg>(360-degree_change))):
					mx, my = 0,0
					

					if (deg<degree_change) or (deg>(360-degree_change)):
						mx = 1
						my = 0
						cv2.arrowedLine(im_with_keypoints, cl, cd, (255,0,0),2)
						print(deg)

					if (60-degree_change)<deg<(60+degree_change):
						mx = 0.5
						my = 0.866025
						cv2.arrowedLine(im_with_keypoints, cl, cd, (255,182,0),2)

					if (120-degree_change)<deg<(120+degree_change):
						mx = -0.5
						my = 0.866025
						cv2.arrowedLine(im_with_keypoints, cl, cd, (178,255,0),2)

					if (180-degree_change)<deg<(180+degree_change):
						mx = -1
						my = 0
						cv2.arrowedLine(im_with_keypoints, cl, cd, (0,242,255),2)

					if (240-degree_change)<deg<(240+degree_change):
						mx = -0.5
						my = -0.866025
						cv2.arrowedLine(im_with_keypoints, cl, cd, (0,0,255),2)

					if (300-degree_change)<deg<(300+degree_change):
						mx = 0.5
						my = -0.866025
						cv2.arrowedLine(im_with_keypoints, cl, cd, (255,0,255),2)



					IslandProperties.append([xa,ya,mx,my])

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

Xlist =[]
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
line_length_upper =100
line_length_lower = 20
dimension = 5
circle_radius = 5
degree_change = 10






#SETS ARGUEMENTS
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")

ap.add_argument("-l", "--lattice", help = "path to the image file")
args = vars(ap.parse_args())

#TAKES LATTICE IMAGE
lattice = cv2.imread(args["lattice"])

# initiates click event for the lattice image
cv2.imshow("click",lattice)
cv2.setMouseCallback("click", click_event_lattice)
cv2.waitKey(-1)

#SETS MIN AND MAX FOR EACH CLICK
X1, Y1, X2, Y2, X3, Y3, X4, Y4, X5, Y5= verts[0][0], verts[0][1], verts[1][0], verts[1][1], verts[2][0], verts[2][1], verts[3][0], verts[3][1], verts[4][0], verts[4][1]
#calculates lattice length and dimension
latticewidth=X4-X3
latticeheight=Y5-Y1
vertexlengthXbig = X2-X1
vertexlengthY = Y3-Y1

Xmin = X3
Ymin = Y1
Ymax = Y5
Xmax = X4


dimension = int(round((latticeheight/(2*vertexlengthY)),0))
print(dimension)
vertexlengthXsmall = (X4-X3)/((3*dimension)+1)
vertexlengthY = (Y5-Y1)/(2*dimension)

C=[]

#DRAWS CIRCLES ON THE VERTICES
for y in range(0,2*dimension+1):
	for x in range(0,(3*dimension)+2): #creates x range and y range for vertex coordinates coordinates
		if (y%2 == 0 and x%2 == 0 and (x+1)%3 == 0):
			C.append([int(Xmin + (x-1)*(vertexlengthXsmall)), int((Ymin + (y*vertexlengthY)))])
			C.append([int(Xmin + (x+1)*(vertexlengthXsmall)), int((Ymin + (y*vertexlengthY)))])
		if (y%2!=0 and x%2==0 and (x+1)%3!=0):
			C.append([int(Xmin + x*(vertexlengthXsmall)),int(Ymin + y*vertexlengthY)])

print(C)



for vertex in C:
	cv2.circle(lattice,(vertex[0],vertex[1]), circle_radius, (255,255,255), -1)



#SHOWS THE RESULT AND WAITS FOR A KEY TO PROCEED
cv2.imshow("lattice w/ vertex",lattice)
cv2.waitKey(-1)
cv2.destroyAllWindows()

#SETS THE UPPER LIMIT FOR A CONNECTION TO BE A PERCENTAGE OF THE ISLAND DISTANCE
line_length_upper = vertexlengthXbig*0.7
line_length_lower = vertexlengthXbig*0.4


#READS THE MFM FILE AND CONVERTS IT TO GREYSCALE
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_lattice =cv2.cvtColor(lattice, cv2.COLOR_BGR2GRAY)
'''
#DRAWS CROSSES ON THE VERTICES TO SEPERATE BLOBS WHICH ARE MERGED
#for vertex in C:
#	cv2.line(gray,(int((vertex[0]-line_length_upper)),int((vertex[1] - line_length_upper))),(int(vertex[0]+line_length_upper),int(vertex[1] + line_length_upper)), 158,1)
#	cv2.line(gray,(int((vertex[0]-line_length_upper)),int((vertex[1] + line_length_upper))),(int(vertex[0]+line_length_upper),int(vertex[1] - line_length_upper)), 158,1)
'''
#DRAWS GREY RECTANGLES AROUND THE EDGE OF THE LATTICE.
cv2.rectangle(gray,(0,int(Ymin-line_length_upper*0.5)), (700,0), 158, -1)
cv2.rectangle(gray,(0,int(Ymax+line_length_upper*0.5)), (700,700), 158, -1)
cv2.rectangle(gray,(int(Xmin-line_length_upper*0.5),0), (0,700), 158, -1)
cv2.rectangle(gray,(int(Xmax+line_length_upper*0.5),0), (700,700), 158, -1)


#ALLOWS THE USER TO CONTROL THE LEVEL OF THRESHOLD TO MAKE WHITE SPOTS BLACK. (NEED TO MOVE THIS TO A FUNCTION)
cv2.namedWindow("WHITE SPOTS TO BLACK (ESC WHEN DONE)")
hh='Max'
hl='Min'
wnd = "WHITE SPOTS TO BLACK (ESC WHEN DONE)"
cv2.createTrackbar("Max", wnd,0,255,nothing)

while(1):
	hul=cv2.getTrackbarPos("Max", wnd)
	#ret,thresh1 = cv2.threshold(image,hul,huh,cv2.THRESH_BINARY)
	ret,whitedetect = cv2.threshold(image,hul,250,cv2.THRESH_BINARY_INV)
	#ret,thresh3 = cv2.threshold(image,hul,huh,cv2.THRESH_TRUNC)
	#ret,thresh4 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO)
	#ret,thresh5 = cv2.threshold(image,hul,huh,cv2.THRESH_TOZERO_INV)
   # cv2.imshow(wnd)
	#cv2.imshow("thresh1",thresh1)
	cv2.namedWindow('original', cv2.WINDOW_NORMAL)
	cv2.resizeWindow('original', 400,400)
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
	ret,blackdetect = cv2.threshold(image,hul,250,cv2.THRESH_BINARY_INV)
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
params.filterByArea = False
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


connectdots(keypoints_dark, keypoints_light, im_with_keypoints)
				

			 	
redo(im_with_keypoints)
print(IslandProperties)
cv2.imshow("",im_with_keypoints)
cv2.waitKey(-1)

#Defines grids the same as RPM CODE
grid = np.zeros((2*dimension+1, 4*dimension+1,9))
xfactor = 2*np.cos(np.pi/6)
yfactor = 2*np.sin(np.pi/6)
test= 0.7071
for x in range(0, 2*dimension+1):
    for y in range(0, 4*dimension+1):
        if x%2!=0 and (y+2)%2==0:
            if (x-1)%4==0 and (y)%4==0:
                if (y+2)%(dimension-1)!=0:
                    grid[x+1,y] = np.array([xfactor*(x+test),(y),0.,0.,0.,0.,0.,0, 0])
                    grid[x-1,y] = np.array([xfactor*(x-test),(y),0.,0.,0.,0.,0.,0, 0])
                grid[x,y] = np.array([xfactor*x,(y),0.,1.,0.,0.,0,0, None])
            elif (x-3)%4==0 and (y+2)%4==0:
                if (y+2)%(dimension-1)!=0:
                    grid[x+1,y] = np.array([xfactor*(x+test),(y),0.,0.,0.,0.,0.,0, 0])
                    grid[x-1,y] = np.array([xfactor*(x-test),(y),0.,0.,0.,0.,0.,0, 0])
                grid[x,y] = np.array([xfactor*x,y,0.,1.,0.,0.,0,0,None])
            else:
                grid[x,y] = np.array([xfactor*x,y,0.,0,0,0,0,0,None])
        elif x%2 ==0 and (y+1)%4==0:
            if x%4==0:
                grid[x,y] = np.array([xfactor*x,yfactor*y,0.,0.5,(3**0.5/2),0.,0,0,None])
            else:
                grid[x,y] = np.array([xfactor*x,yfactor*y,0.,-0.5,(3**0.5/2),0.,0,0,None])
        elif x%2 ==0 and (y-1)%4==0:
            if x%4==0:
                grid[x,y] = np.array([xfactor*x,yfactor*y,0.,-0.5,(3**0.5/2),0.,0,0,None])
            else:
                grid[x,y] = np.array([xfactor*x,yfactor*y,0.,0.5,(3**0.5/2),0.,0,0,None])
        else:
            if np.array_equal(grid[x,y,0:2], [0., 0.]):
                grid[x,y] = np.array([xfactor*x,y,0.,0,0,0,0,0,None])
X = grid[:,:,0]
Y = grid[:,:,1]
Mx=grid[:,:,3]
My=grid[:,:,4]


#Changes X and Y into coordinate system
for Island in IslandProperties:
	for n in range(2*dimension+1):
		if ((Island[0] - (3*vertexlengthXbig)/8) < (Xmin + 0.25*vertexlengthXbig + ((3*n*vertexlengthXbig)/4)) < ((Island[0] + (3*vertexlengthXbig)/8))):
			Island[0] = n
	for m in range(2*dimension+1):
		if Island[0]%2==0:
			if (Island[1] - vertexlengthY/2) < (Ymin + 0.5*vertexlengthY + (m*vertexlengthY)) < (Island[1] + vertexlengthY/2):
				Island[1] = (4*dimension) - (2*m +1)
		if Island[0]%2!=0:
			if (Island[1] - vertexlengthY/2) < (Ymin + (m*vertexlengthY)) < (Island[1] + vertexlengthY/2):
				Island[1] = (4*dimension) - 2*m






IslandProperties.sort(key=lambda x: x[0])
#Removes any duplicates
b = list()
for sublist in IslandProperties:
    if sublist not in b:
        b.append(sublist)
print(b)

#Defines coordinates for mx and my


for bar in b:
	print(bar[0], bar[1])
	Mx[(bar[0]),(bar[1])]=bar[2]
	My[(bar[0]),(bar[1])]=bar[3]


print(Mx,My)
fig, ax = plt.subplots()

q= ax.quiver(X, Y, Mx, My, np.arctan2(My, Mx), pivot='mid')
plt.show()


cv2.imshow("",im_with_keypoints)
cv2.waitKey(-1)



'''
save = input("Save? Y/N")
if save == ("Y"):
	name = input("Filename?")
	cv2.imwrite(name, im_with_keypoints)
'''
'''
((deg<degree_change) or ((90-degree_change)<deg<(90+degree_change)) or ((180-degree_change)<deg<(180+degree_change)) or ((270-degree_change)<deg<(270+degree_change)) or (deg>(360-degree_change))):

'''
