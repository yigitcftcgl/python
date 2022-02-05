prevNum = 0
curNum = 0
print('Printing current and previous number sum in a range(10)')
for curNum in range(10):
    prevNum = curNum - 1
    sum = curNum + prevNum
    print('Previous Number:' + str(prevNum))
    print('Current Number:' + str(curNum))
    print('Sum:' + str(sum))

   
