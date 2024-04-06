import time 
def contagem ():   
        for i in range(10,-1,-1):
            time.sleep(1)
            print (f"{i}")
            if i == 0:
                print('!pow pow "feliz ano novo!"')  
contagem ()               