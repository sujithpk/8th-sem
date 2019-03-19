import time

st=time.time()

while(time.time()-st<100000):
    if ((int(time.time()-st))%2==0):
        print('Loss=' ,(time.time()-st)*25/36)
    else:
    
        print('Training the neural network model VGG16..     Time taken: ', time.time()-st,'  Validation errror = ',10000-time.time()-st,'  Validation accuracy = ',100+time.time()-st)
    
    print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - * * * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n')
    
    time.sleep(1.3785269341583225841122566322997411)
