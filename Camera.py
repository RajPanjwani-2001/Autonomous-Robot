import yolov5
import cv2
import numpy as np
import torch

#s1-d1
s1_x1,s1_y1 = 286, 10
s1_x2,s1_y2 = 314, 39
d1_x1,d1_y1 = 64, 271
d1_x2,d1_y2 = 89, 299

#s2-d2
s2_x1,s2_y1 = 319, 10
s2_x2,s2_y2 = 346, 39   
d2_x1,d2_y1 = 64,303
d2_x2,d2_y2 = 89,329

#s3-d3
s3_x1,s3_y1 = 350, 10
s3_x2,s3_y2 = 378, 39
d3_x1,d3_y1 = 604,301
d3_x2,d3_y2 = 630,328

#s4-d4
s4_x1,s4_y1 = 382, 10
s4_x2,s4_y2 = 409, 39
d4_x1,d4_y1 = 604, 269
d4_x2,d4_y2 = 630, 299



def getLoc():
    #load model
    model = yolov5.load('dataset/runs/train/exp2/weights/best.pt')
    
    #get video
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)


    ret,frame = cap.read()
    
    results = model(frame, size=640)
    predictions = results.pred[0]
    #print(predictions, type(predictions))
    #print(predictions.size()[0])

    data = []    
    if predictions.size()[0] > 0:
        box = predictions[:,:4]
        box = box.cpu().numpy()
        box = np.asarray(box, dtype='int')
        
        for j in range(len(predictions)):
            #cv2.rectangle(frame, (box[j,0], box[j,1]), (box[j,2], box[j,3]),(0,255,0), 1)
            cent_x = (int((box[j,0] + box[j, 2])/2))
            cent_y = (int((box[j,1] + box[j, 3])/2))
            #cv2.circle(frame,(cent_x,cent_y),3,(255,0,0),2)
            label = int(predictions[j][-1].cpu().numpy())
            prob = predictions[j][-2].cpu().numpy()
            #print(cent_x,cent_y,label.cpu().numpy())
            #cv2.rectangle(frame,tuple(box[0,:2]),tuple(box[0,1:3]),(0,255,0),2)
            if label == 0 and cent_y > 55:
                data.append((cent_x,cent_y,label, prob))     
    #return data
    try:
        res = max(data, key = lambda i : i[1])
        x = res[0]
        y =res[1]
        lab = res[2]
    except:
        x = -1
        y = -1

    #dist = ((s1_mid[0] - x)**2 + (s1_mid[1] - y)**2)**0.5
    
    #cv2.imshow('vid',frame)
    cap.release()    
    #cv2.destroyAllWindows()
    #return data,dist,lab
    return x,y

def getCorners():
    model = yolov5.load('dataset/runs/train/exp2/weights/best.pt')
    
    #get video
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)


    ret,frame = cap.read()
    
    results = model(frame, size=640)
    predictions = results.pred[0]
    #print(predictions, type(predictions))
    #print(predictions.size()[0])

    data = []    
    C1 = []
    C2 = []
    if predictions.size()[0] > 0:
        box = predictions[:,:4]
        box = box.cpu().numpy()
        box = np.asarray(box, dtype='int')
        
        for j in range(len(predictions)):
            #cv2.rectangle(frame, (box[j,0], box[j,1]), (box[j,2], box[j,3]),(0,255,0), 1)
            cent_x = (int((box[j,0] + box[j, 2])/2))
            cent_y = (int((box[j,1] + box[j, 3])/2))
                      
            #cv2.circle(frame,(cent_x,cent_y),3,(255,0,0),2)
            label = int(predictions[j][-1].cpu().numpy())
            #print(cent_x,cent_y,label.cpu().numpy())
            #cv2.rectangle(frame,tuple(box[0,:2]),tuple(box[0,1:3]),(0,255,0),2)
            data.append((cent_x,cent_y,label))  
    c1_cor = min(data, key = lambda i : i[0] and i[2]==2)
    cd1_x = c1_cor[0]
    cd1_y = c1_cor[1]
    
    C1.append(cd1_x)
    C1.append(cd1_y)
    
    c2_cor = max(data, key = lambda i : i[0] and i[2]==2)
    cd2_x = c2_cor[0]
    cd2_y = c2_cor[1]
    
    C2.append(cd2_x)
    C2.append(cd2_y)
    
    
    return C1, C2

def getMid1():
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)

    s1_mid = []
    ret,frame = cap.read()
    s1_mid_x = (s1_x1+s1_x2)/2
    s1_mid_y = (s1_y1+s1_y2)/2
    s1_mid.append(s1_mid_x)
    s1_mid.append(s1_mid_y)
    
    d1_mid = []
    d1_mid_x = (d1_x1+d1_x2)/2
    d1_mid_y = (d1_y1+d1_y2)/2
    d1_mid.append(d1_mid_x)
    d1_mid.append(d1_mid_y)
    
    return s1_mid,d1_mid


def getMid2():
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)

    s2_mid = []
    ret,frame = cap.read()
    s2_mid_x = (s2_x1+s2_x2)/2
    s2_mid_y = (s2_y1+s2_y2)/2
    s2_mid.append(s2_mid_x)
    s2_mid.append(s2_mid_y)
    
    d2_mid = []
    d2_mid_x = (d2_x1+d2_x2)/2
    d2_mid_y = (d2_y1+d2_y2)/2
    d2_mid.append(d2_mid_x)
    d2_mid.append(d2_mid_y)
    
    return s2_mid,d2_mid


def getMid3():
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)

    s3_mid = []
    ret,frame = cap.read()
    s3_mid_x = (s3_x1+s3_x2)/2
    s3_mid_y = (s3_y1+s3_y2)/2
    s3_mid.append(s3_mid_x)
    s3_mid.append(s3_mid_y)
    
    d3_mid = []
    d3_mid_x = (d3_x1+d3_x2)/2
    d3_mid_y = (d3_y1+d3_y2)/2
    d3_mid.append(d3_mid_x)
    d3_mid.append(d3_mid_y)
    
    return s3_mid,d3_mid

def getMid4():
    url = 'http://10.80.6.78:8080/video'
    cap = cv2.VideoCapture(url)

    s4_mid = []
    ret,frame = cap.read()
    s4_mid_x = (s4_x1+s4_x2)/2
    s4_mid_y = (s4_y1+s4_y2)/2
    s4_mid.append(s4_mid_x)
    s4_mid.append(s4_mid_y)
    
    d4_mid = []
    d4_mid_x = (d4_x1+d4_x2)/2
    d4_mid_y = (d4_y1+d4_y2)/2
    d4_mid.append(d4_mid_x)
    d4_mid.append(d4_mid_y)
    
    return s4_mid,d4_mid

    


    
    
    
    
