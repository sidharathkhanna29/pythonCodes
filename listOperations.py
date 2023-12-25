
StdName  = ["Hesam ", "Sid"]
stdMarks = [[78, 84, 23, 59], [96, 90, 98, 89] ]

stdFinalMarks = []
contents = ["Quizzes", "Assignments", "Test1", "Test2"]
weight = [0.15, 0.35, 0.20, 0.30]

# Find avg of the class 
# avg of each contents! ( Avg quizes, assignments, test1, Test2)

for i in range(len(StdName)):
    finalMark = 0
    for j in range(len(contents)):
        finalMark += stdMarks[i][j] * weight[j]

    print(f'Final Marks for {StdName[i]} : {finalMark:.2f}')
    stdFinalMarks.append(finalMark)

classAvg = sum(stdFinalMarks) / len(stdFinalMarks)
print(f' Class Average :  {classAvg:.2f}')


for j in range(len(contents)):
    addContents = 0
    for i in range(len(StdName)):
        addContents += stdMarks[i][j]
    print(f'Avg of {contents[j]} : {addContents / len(StdName)}')


