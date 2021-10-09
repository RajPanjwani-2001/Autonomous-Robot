import socket
import Movement as m
import sys


A = []
C = []
s1_ip = '10.80.6.81'
s2_ip = '10.80.2.18'
s3_ip = '10.80.7.243'
s4_ip = '10.80.1.101'

s = socket.socket()
print('Socket Created')
s.bind(('192.168.12.20',9999))
try: 

    s.listen(1)
    print(bytes('waiting for connections','utf-8'))
    
    for i in range(2):
        t1, t2 = s.accept()
        C.append(t1)
        A.append(t2[0])
        print('Connected with ',t2[0])
    print(A)
    
    obj = m.Movement()
    
    s1_index = A.index(s1_ip)
    s1_soc = C[s1_index]
    obj.s1_forward(s1_soc)
    obj.s1_reverse(s1_soc)
    '''
    s2_index = A.index(s2_ip)
    s2_soc = C[s2_index] 
    obj.s2_forward(s2_soc)
    obj.s2_reverse(s2_soc)
    
    
    s3_index = A.index(s3_ip)
    s3_soc = C[s3_index] 
    obj.s3_forward(s3_soc)
    obj.s3_reverse(s3_soc)
    '''
    s4_index = A.index(s4_ip)
    s4_soc = C[s4_index] 
    obj.s4_forward(s4_soc)
    obj.s4_reverse(s4_soc)
    
except:
    
    print(sys.exc_info())
    t1.close()
    
 
    