
import random
import bigo
LIST_SIZE = 1000
total_points = 15

#
# Code to test the four find functions of program 3 
#

def testFind(find_func, the_list, points):
    global total_points
    if find_func(the_list, LIST_SIZE + 1):
        print("Error: found when not there, -",points,find_func)
        total_points -= points
    random_location = random.randint(0,LIST_SIZE)
    temp = the_list[random_location]
    if not find_func(the_list, temp):
        print("Error: not found when there, -",points,find_func)
        total_points -= points
    the_list[random_location] = temp
    if not find_func(the_list, the_list[3]):
        print("Error: not found when there. -",points,find_func)
        total_points -= points
        
test_list = []
for i in range(LIST_SIZE):
    test_list.append(random.randint(0,LIST_SIZE))

testFind(bigo.find1, test_list, 1)
testFind(bigo.find2, test_list, 1)
testFind(bigo.find3, test_list, 1)
test_list.sort()
testFind(bigo.find4, test_list, 2)
print("Total Score: ", total_points)



