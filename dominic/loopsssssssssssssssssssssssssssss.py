hippos = 0
answer = 'y'
while answer == 'y':
    wewe = ' balancing hippos'
    if  hippos > 0:
        wewe  = ' balancing hippo'
    if hippos > 1:
        wewe = ' balancing hippos'
    print('You have ' + str(hippos) + wewe)
    hippos = hippos + 1
    answer = input('more hippos? y/n)')
    
