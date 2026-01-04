import cv2 
print(cv2)
#opencv relies on NumPy and it installs automatically with CV2 
#i can also install Matplotlib for rending certain graphical output(still learning what this mean)

#Opencv has the imread() function to read images, we activate it with a line such as this 
# img = cv2.imread(filename, flags)
# the flag  is a special kind of enumeration aka numbering method that represents multiple states or permissions at once, where each constant value is a power of 2 aka 1,2,4,6,8
#anyways 
# cv2.IMREAD_COLOR(1) - LOADS A COLOR IMAGE
# CV2.IMREAD_GRAYSCALE(0) - LOADS IMAGE IN GRAYSCALE MODE
# CV2.IMREAD_UNCHANGE(-1) - LOADS IMAGE AS SUCH INCLUDING ALPHA CHANNEL(DONT KNOW WHAT AN ALPHA CHANNEL IS, COULD BE A COLOR THING LOL)
# THE IMREAD FUNCTION WILL RETURN AND IMAGE OBJECT THAT CAN BE RENDERED USING IMSHOW() PLUS MATPLOTLIB COULD HELP, TO USE IMSHOW() HERE IT IS
# CV2.IMSHOW(WINDOW-NAME, IMAGE)
#IDK WHAT WINDOW-NAME IS AND IF IMAGE NEEDS THE ./ OR SOMETHING BEFORE THE NAME TO FIND IT AKA A PATH 
#OHHH THE IMAGE IS DISPLAYED IN A NAMED WINDOW WHICH I CAN NAME, A NEW WINDOW IS CREATED WITH THE AUTOSIZE FLAG SET, THE WAITKEY() IS A KEYBOARD BINDING FUNCTION. 
#ITS ARGUMENT OR THE SECOND PART OF THE PARAMENT IS THE TIME IN MILLISECONDS LET SEE WHAT THIS LOOKS LIKE
# CV2.WAITKEY(0) ZERO TIME 
# THE FUNCTION WAITS FOR A SPECIFIED MILLISECOPNDS AND KEEPS THE WINDOW ON DISPLAU TILL A KEY IS PRESSED. FINNALLY WE CAN DESTORY ALL THE WINDOS THUS CREATED
#BASICALLY THE FUNCTION KEEPS ALL THE WINDOWS WAITING FOR A CERTAIN AMOUNT OF MILLISECOND AND KEEP THE WINDOW ON DISPLAY TILL A KEY IS PRESSED. HERES A TEST
import numpy as np
# loads a color image in grayscale is what they told me this line does, imma need to see it
img = cv2.imread("OpenCV_logo.png", 1) # the 1 is a flag and if its one i hope that means it just 1 and not 0 or sum or 2 because they follow everything to the power of two
cv2.imshow('opencvpic', img) # the windows name is opencvpic and they are looking for an img 
cv2.waitKey(0) # NOOO TIME
cv2.destroyAllWindows() # i thought this happened automatically but i think that this function destorys the windows they just need to wait for the key press first
# cv the goat has a package called imwrite() aka a function that saves an image object to a specifed file, idk what this means but imma find out
#cv2.imwrite(filename, img) lots of im*insertname*()the image format is automatically decided by opencv from the file extension. OPENCV SUPORTS 
# *.bmp, .dib, .jpeg , .jpg , .png , .webp, .sr, .tiff ,\.tif etc image file types/
# example 


# write images 
import numpy as np 
import cv2
img = cv2.imread("OpenCV_Logo.png", 0)
cv2.imshow('image', img)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite("opencv_logo_GS.png", img)
cv2.destroyAllWindows()
