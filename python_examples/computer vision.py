import cv2
import numpy as np
import os 

# img = cv2.imread('/home/wasiy/Pictures/vault/fashion.jpg')
# re_img = cv2.resize(img,(0,0),fx=0.5, fy=0.5)
# h = np.hstack((re_img,re_img))
# v = np.vstack((h,h))

# cv2.imshow('Tanha',v)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# list_name = os.listdir('/home/wasiy/Pictures/vault')
   
# for name in list_name:
#     path = '/home/wasiy/Pictures/vault'
#     img_name = path + '/' + name
#     img = cv2.imread(img_name)
#     if img is None:
#         print("Error: OpenCV could not read the image.")
#     else:
#         re_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
        
#     cv2.imshow('Tanha',re_img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows() 

def window (win):
    cv2.namedWindow(win,cv2.WINDOW_NORMAL)
img = cv2.imread('/home/wasiy/Pictures/picture/moment.jpg')

txt1 = cv2.putText(
    img=img,       #(img: MatLike,
    text='Dream life',  #text: str,
    org= (10,60),      #org: Point, 
    fontScale= 2,   #fontScale: float,
    color= (34,50,55),        #color: Scalar,
    lineType= cv2.LINE_AA ,   #lineType: int = ...,
    thickness=2,       # #thickness: int = ..., 
    fontFace=cv2.FONT_HERSHEY_SIMPLEX)     #fontFace: int,

new_img = cv2.line(img=txt1,pt1=(10,70),pt2=(340,70),color=(64,64,64),thickness=2,lineType=4)


new_img1 = cv2.rectangle(img=new_img,pt1=(320,110),pt2=(420,250),color=(64,64,64),thickness=2,lineType=4)

txt2 = cv2.putText(
    img=new_img1,       #(img: MatLike,
    text='Tanha',  #text: str,
    org= (320,100),      #org: Point, 
    fontScale= 1,   #fontScale: float,
    color= (0,0,200),        #color: Scalar,
    lineType= cv2.LINE_AA ,   #lineType: int = ...,
    thickness=2,       # #thickness: int = ..., 
    fontFace=cv2.FONT_HERSHEY_SIMPLEX)     #fontFace: int,

new_img2 = cv2.rectangle(img=txt2,pt1=(160,310),pt2=(310,480),color=(64,64,64),thickness=2,lineType=4)
cir = cv2.circle(img = new_img2, center = (350,350), radius = 22, color = (0,0,255), thickness = 2, lineType = 16)

txt3 = cv2.putText(
    img=cir,       #(img: MatLike,
    text='Wasiy',  #text: str,
    org= (160,300),      #org: Point, 
    fontScale= 1,   #fontScale: float,
    color= (0,0,200),        #color: Scalar,
    lineType= cv2.LINE_AA ,   #lineType: int = ...,
    thickness=2,       # #thickness: int = ..., 
    fontFace=cv2.FONT_HERSHEY_SIMPLEX)     #fontFace: int,

if img is None:
    print("Error: OpenCV could not read the image.")
else:
    cv2.imshow('Tanha',new_img)

normalize = window('Tanha')

cv2.waitKey(0)
cv2.destroyAllWindows()




# def window (win):
#     cv2.namedWindow(win,cv2.WINDOW_NORMAL)

# img = cv2.imread('/home/wasiy/Pictures/picture/moment.jpg')

# poligon = cv2.polylines(img = img,pts = [np.array([[200,300],[250,250],[300,300],[400,400],[200,400],[200,300]])],
#                                          isClosed=False,color=(0,0,255),thickness=2,lineType=16)


# if img is None:
#     print("Error: OpenCV could not read the image.")
# else:
#     cv2.imshow('Tanha',img)

# normalize = window('Tanha')

# cv2.waitKey(0)
# cv2.destroyAllWindows()