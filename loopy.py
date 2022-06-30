import msvcrt as m
def wait():
    m.getch()

##print('a for loop - will run 10 times: ') 
##for counter in range(1,11):
##    print(str(counter) + ': Dominic\'s Room -- KEEP OUT!!')
##print('a while loop - will run until a condition is met: ')

hippos = 0
answer = 'y'
while answer == 'y':
    hippos = hippos + 1
    print(str(hippos) + ' balancing hippos!')
    answer = input('add another hippo? (y/n)')
hippoString = ' balancing hippo'

if hippos > 1:
    hippoString = ' balancing hippos'    

print('you now have ' + str(hippos) + hippoString)

##while True:
##    print ('this is an infinite loop!') 

for hooray_counter in range(1,4):
    for hip_conter in range(1,3):
        print('Hip')
    print('Hooray!')
    


wait()



