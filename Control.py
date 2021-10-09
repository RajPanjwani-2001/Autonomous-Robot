class Control:

    # forward
    def forward(self, soc):
        to_send ='1'
        soc.send(bytes(to_send,'utf-8'))
        #print(to_send)

    # backward   
    def backward(self, soc):
        soc.send(bytes('2','utf-8'))
    
    # left
    def left(self, soc):
        soc.send(bytes('3','utf-8'))

    # right 
    def right(self, soc):
        soc.send(bytes('4','utf-8'))


    def Slight_left(self, soc):
        soc.send(bytes('5','utf-8'))

    def Slight_right(self, soc):
        soc.send(bytes('6','utf-8'))
        
    def Slight_forward(self, soc):
        soc.send(bytes('7','utf-8'))
        
    def drop(self, soc):
        soc.send(bytes('8','utf-8'))