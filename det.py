import torch
import yolov5
import cv2
import numpy as np

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



#Mid points
s1_mid = ((s1_x1+s1_x2)/2, (s1_y1+s1_y2)/2)
model = yolov5.load('dataset/runs/train/exp2/weights/best.pt')
url = 'http://10.80.6.78:8080/video'
cap = cv2.VideoCapture(url)

while(True):
    ret,frame = cap.read()

    results = model(frame, size=640)
    predictions = results.pred[0]
    #s1-d1 - yellowbox = box.cpu().numpy()

    cv2.rectangle(frame, (s1_x1, s1_y1), (s1_x2,s1_y2), (244,33,0), 2)
    cv2.rectangle(frame, (d1_x1,d1_y1), (d1_x2,d1_y2), (244,33,0), 2)
    
    #s2-d2 - blue
    cv2.rectangle(frame, (s2_x1, s2_y1), (s2_x2,s2_y2), (244,246,51), 2)
    cv2.rectangle(frame, (d2_x1,d2_y1), (d2_x2,d2_y2), (244,246,51), 2)
      
    #s3-d3 - red
    cv2.rectangle(frame, (s3_x1, s3_y1), (s3_x2,s3_y2), (45,245,179), 2)
    cv2.rectangle(frame, (d3_x1,d3_y1), (d3_x2,d3_y2), (45,245,179), 2)
    
    #s4-d4 - green
    cv2.rectangle(frame, (s4_x1, s4_y1), (s4_x2,s4_y2), (51,246,248), 2)
    cv2.rectangle(frame, (d4_x1,d4_y1), (d4_x2,d4_y2), (51,246,248), 2)
    

    
    ##rint(predictions, type(predictions))
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
                      
            cv2.circle(frame,(cent_x,cent_y),3,(255,0,0),2)
            label = int(predictions[j][-1].cpu().numpy())
            #print(cent_x,cent_y,label.cpu().numpy())
            #cv2.rectangle(frame,tuple(box[0,:2]),tuple(box[0,1:3]),(0,255,0),2)
            data.append((cent_x,cent_y,label))  
    print(data)
        
    cv2.imshow('vid',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
res = max(data, key = lambda i : i[1] and i[2]==0)
x = res[0]
y =res[1]
lab = res[2]
C1 = []
C2 = []
c1_cor = min(data, key = lambda i : i[0] and i[2]==2)
c1_x = c1_cor[0]
c1_y = c1_cor[1]
C1.append(c1_cor)

c2_cor = max(data, key = lambda i : i[0] and i[2]==2)
c2_x = c2_cor[0]
c2_y = c2_cor[1]
C2.append(c2_cor)
    
dt = ((c1_x - x)**2 + (c1_y - y)**2)**0.5

cap.release()

cv2.destroyAllWindows()
