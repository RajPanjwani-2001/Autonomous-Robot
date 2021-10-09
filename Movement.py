import Control
from Camera import *
import time
import cv2

class Movement(Control.Control):
    def __init__(self):
        self.__n = 6
        C1, C2 = getCorners()
        S1,D1 = getMid1()
        S2,D2 = getMid2()
        S3,D3 = getMid3()
        S4,D4 = getMid4()
        
        self.c1_x = C1[0]
        self.c1_y = C1[1]
        self.c2_x = C2[0]
        self.c2_y = C2[1]
        
        self.s1_x = S1[0]
        self.s1_y = S1[1]
        self.d1_x = D1[0]
        self.d1_y = D1[1]
        
        self.s2_x = S2[0]
        self.s2_y = S2[1]
        self.d2_x = D2[0]
        self.d2_y = D2[1]
        
        self.s3_x = S3[0]
        self.s3_y = S3[1]
        self.d3_x = D3[0]
        self.d3_y = D3[1]
        
        self.s4_x = S4[0]
        self.s4_y = S4[1]
        self.d4_x = D4[0]
        self.d4_y = D4[1]
        

    def s1_forward(self, soc):
        for i in range(8):
            self.forward(soc)
            time.sleep(0.1)
            print('start')
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.05)
                print('error')
                continue
            
            dst = abs(self.d1_y - y)
            
            print(dst, self.d1_y, y, self.s1_x, x, end=" ")
            if(dst < 12):
                self.right(soc)
                print('Right')
                time.sleep(1)
                
                self.Slight_right(soc)
                time.sleep(0.1)
                print('SR')
                self.Slight_right(soc)
                time.sleep(0.1)
                print('SR')
                
                break
                
            if (x < self.s1_x):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL Forward')
            
            if (x > self.s1_x):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                
            if (x == self.s1_x):
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_forward(soc)
                time.sleep(0.05)
                print('error')
                continue
            
            dst = abs(x - self.d1_x)
            print(x, y, dst, self.d1_y)
            if  dst < 12:
                self.drop(soc)
                time.sleep(12)
               
                break
            if y == self.d1_y:
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                
            elif y > self.d1_y:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR forward')
            else:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL forward')
                
    def s1_reverse(self, soc):
        for i in range(4):
            self.backward(soc)
            time.sleep(0.1)
            print('backward')
             
        self.right(soc)
        time.sleep(1)
        print('right')
        self.right(soc)
        time.sleep(1)
        print('right')
        self.right(soc)
        time.sleep(1)
        print('right')
        self.right(soc)
        time.sleep(1)
        print('right')
        
        
        
        while True:
            x, y = getLoc()
            if(x == -1):                
                self.Slight_right(soc)
                time.sleep(0.1)
                #self.Slight_forward(soc)
                print('error')
                continue
            
            dst = abs(self.s1_x - x)
            
            print(dst, x, y)
            if(dst < 10):
                self.left(soc)
                time.sleep(0.5)
                print('left')
                self.Slight_left(soc)
                time.sleep(0.1)
                print('SL')
               
                break
            
            if(self.d1_y - y == 0):    
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                
            if(self.d1_y - y < 0):    
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL Forward')
                 
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print(' SR Forward')
                
        
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            dst = abs(y - self.s1_y)
            print(x, y, dst, self.s1_y)
            print('Check:', dst, dst < 55)
            
            if  dst < 55:
                for i in range(4):
                    self.forward(soc)
                    time.sleep(0.1)
                    print('Home')
                break
            
            if x == self.s1_x-5:
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                 
            elif x > self.s1_x-5:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL Forward')
                 
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                
    def s2_forward(self, soc):
        #for i in range(self.__n):
        for i in range(8):
            self.forward(soc)
            time.sleep(0.1)
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.d2_y - y)
            
            print(dst, self.d2_y, y, self.s2_x, x, end=" ")
            if(dst < 15):
                self.right(soc)
                time.sleep(0.5)
                self.right(soc)
                time.sleep(0.5)
                #self.Slight_right(soc)
                #time.sleep(0.1)
                print('Right')
                break
                
            if (x < self.s2_x):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL Forward')
            
            if (x > self.s2_x):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                
            if (x == self.s2_x):
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(x - self.d2_x)
            print(dst, self.d2_x, x, self.s2_y, y, end=" ")
            if  dst < 10:
                self.drop(soc)
                time.sleep(12)
                break
            if y == self.d2_y:
                self.forward(soc)
                time.sleep(0.1)
                print('forward')
                
            elif y > self.d2_y:
                self.right(soc)
                time.sleep(0.8)
                self.forward(soc)
                time.sleep(0.1)
                print('SR')
            else:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL')
                
    def s2_reverse(self, soc):
        
        for i in range(4):
            self.backward(soc)
            time.sleep(0.1)
            print('backward')
             
        self.left(soc)
        time.sleep(0.5)
        print('left')
        self.left(soc)
        time.sleep(0.5)
        print('left')
        self.left(soc)
        time.sleep(0.5)
        print('left')
        self.left(soc)
        time.sleep(0.5)
        print('left')
        self.left(soc)
        time.sleep(0.5)
        print('left')
        self.Slight_left(soc)
        time.sleep(0.5)
        print('SL')
        
        
            
        while True:
            x, y = getLoc()
            if(x == -1):                
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.s2_x - x)
            
            print(dst, x, y)
            if(dst < 15):
                self.left(soc)
                time.sleep(0.5)
                print('left')
                self.left(soc)
                time.sleep(0.5)
                print('left')
                self.left(soc)
                time.sleep(0.5)
                print('left')
                break
            
            if(self.d2_y - y == 0):    
                self.forward(soc)
                time.sleep(0.1)
            if(self.d2_y - y < 0):    
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                
        
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            dst = abs(y - self.s2_y)
            print(x, y, dst, self.s2_y)
            print('Check:', dst, dst < 55)
            if  dst < 55:
                for i in range(5):
                    self.Slight_forward(soc)
                    time.sleep(0.1)
                    self.Slight_right(soc)
                    time.sleep(0.1)
                    print('home')
                break
            
            if x == self.s2_x-5:
                self.forward(soc)
                time.sleep(0.1)
            elif x > self.s2_x-5:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                
    def s3_forward(self, soc):
        for i in range(8):
            self.forward(soc)
            time.sleep(0.1)
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.d3_y - y)
            
            print(dst, self.d3_y, y, self.s3_x, x, end=" ")
            if(dst < 12):
                self.left(soc)
                print('left')
                time.sleep(1.0)
                self.Slight_left(soc)
                print('SL')
                time.sleep(1.0)
                self.forward(soc)
                print('forward')
                time.sleep(0.1)
                break
                
            if (x < self.s3_x):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL Forward')
            
            if (x > self.s3_x):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                
            if (x == self.s3_x):
                self.forward(soc)
                time.sleep(0.1)
                print('Forward')
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(x - self.d3_x)
            print(x, y, dst, self.d3_y)
            if  dst < 10:
                self.drop(soc)
                time.sleep(12)
                break
                
            if y == self.d3_y:
                self.forward(soc)
                time.sleep(0.1)
                
            elif y > self.d3_y:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                
    def s3_reverse(self, soc):
        for i in range(4):
            self.backward(soc)
            print('Backward')
            time.sleep(0.1)
            
        self.left(soc)
        print('left')
        time.sleep(2)
        self.left(soc)
        print('left')
        time.sleep(2)
        self.left(soc)
        print('left')
        time.sleep(2)
        
        
        while True:
            x, y = getLoc()
            if(x == -1):                
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.s3_x - x)
            
            print(dst, x, y)
            if(dst < 10):
                self.right(soc)
                time.sleep(1.5)
                self.right(soc)
                time.sleep(1.5)
                self.forward(soc)
                time.sleep(0.1)
                break
            
            if(self.d3_y - y == 0):    
                self.forward(soc)
                time.sleep(0.1)
            if(self.d3_y - y < 0):    
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
            else:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                            
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            dst = abs(y - self.s3_y)
            print(x, y, dst, self.s3_y)
            print('Check:', dst, dst < 55)
            if  dst < 55:
                for i in range(6):
                    self.forward(soc)
                    time.sleep(0.1)
                    print('Home')
                break
            
            if x == self.s3_x:
                self.forward(soc)
                time.sleep(0.1)
                print('Frwd')
                
            elif x > self.s3_x:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('Lft')
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('Rgt')
                
    def s4_forward(self, soc):
        for i in range(self.__n):
            self.forward(soc)
            time.sleep(0.2)
                
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.d4_y - y)
            
            print(dst, self.d4_y, y, self.s4_x, x, end=" ")
            if(dst < 8):
                self.left(soc)
                time.sleep(0.5)
                print('left')
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                break
                
            if (x < self.s4_x):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('SL Forward')
            
            if (x > self.s4_x):
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR Forward')
                
            if (x == self.s4_x):
                self.forward(soc)
                time.sleep(0.2)
                print('Forward')
                
        while True:
            x, y = getLoc()
            if(x == -1): 
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(x - self.d4_x)
            print(x, y, dst, self.d4_y)
            if  dst < 10:
                self.drop(soc)
                time.sleep(12)
                break
            if y == self.d4_y:
                self.forward(soc)
                time.sleep(0.2)
                print('Forward')
                
            elif y > self.d4_y:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('SL SF')
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('SR SF')
                
    def s4_reverse(self, soc):
        for i in range(4):
            self.backward(soc)
            print('Backward')
            time.sleep(0.2)
            
        self.left(soc)
        print('left')
        time.sleep(0.5)
        self.left(soc)
        print('left')
        time.sleep(0.5)
        self.Slight_right(soc)
        time.sleep(0.1)
        self.Slight_right(soc)
        time.sleep(0.1)
        
        
        while True:
            x, y = getLoc()
            if(x == -1):                
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(self.s4_x - x)
            
            print(dst, x, y)
            if(dst < 10):
                self.right(soc)
                time.sleep(0.8)
                
                break
            
            if(self.d4_y - y == 0):    
                self.forward(soc)
                time.sleep(0.1)
                print('forward')
            if(self.d4_y - y < 0):    
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SR SF')
            else:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('SL SF')
                
        
        while True:
            x, y = getLoc()
            if(x == -1):
                self.Slight_left(soc)
                time.sleep(0.1)
                self.Slight_forward(soc)
                time.sleep(0.1)
                print('error')
                continue
            
            dst = abs(y - self.s4_y)
            print(x, y, dst, self.s4_y)
            print('Check:', dst, dst < 55)
            if  dst < 55:
                for i in range(5):
                    self.forward(soc)
                    time.sleep(0.1)
                    self.Slight_left(soc)
                    time.sleep(0.1)
                    print('Home')
                break
            
            if x == self.s4_x:
                self.forward(soc)
                time.sleep(0.1)
                print('Frwd')
                
            elif x > self.s4_x:
                self.Slight_left(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('Lft')
            else:
                self.Slight_right(soc)
                time.sleep(0.1)
                self.forward(soc)
                time.sleep(0.1)
                print('Rgt')