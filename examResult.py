midtermExam = input('Midterm exam:')
finalExam = input('Final exam:')
midtermExam = float(midtermExam)
finalExam = float(finalExam)
weightedAvarage = (4 * midtermExam / 10)+(6 * finalExam / 10)

if weightedAvarage >= 50 and finalExam >= 50 :
    print('You passed')
    print('Reasons(Final exam - weighted avarage):'+ str(finalExam)+' '+str(weightedAvarage))
else :
    print('You failed\nReasons(Final exam - weighted avarage):' + str(finalExam)+' '+str(weightedAvarage))
    