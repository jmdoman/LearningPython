hippos = 0
answer = 'y'
while answer == 'y':
    hippoString = ' balancing hippos'
    if hippos > 0:
        hippoString = ' balancing hippo'
    if hippos > 1:
        hippoString = ' balancing hippos'
    print('You have ' + str(hippos) + hippoString)
    hippos = hippos + 1
    answer = input('more hippos? y/n)')

print('done! you have ' + str(hippos) + hippoString)




#hippoString = ' balancing hippo'


