#***************************************************************************************************************************\\
#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.         |
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.                     | 
#Example                                                                                                                     |
# 'alpha' : [20,30,40]                                                                                                       |
# 'beta' : [30,50,70]                                                                                                        |
# 'beta' : [30,50,70]œ                                                                                                       |
# query_name= 'beta'                                                                                                         |
#The query_name is 'beta'. beta's average score is                                                                           |
# (30+50+70)/30 = 50.0                                                                                                       |
#Input Format                                                                                                                |
#The first line contains the integer                                                                                         |
#, the number of students' records. The next                                                                                 |
#lines contain the names and marks obtained by a student, each value separated by a                                          |
#space. The final line contains query_name, the name of a student to query.                                                  |
#Constraints                                                                                                                 |
# 2<n<10                                                                                                                     |
# 0<marks [i]<100                                                                                                            |
# length of marks arrays = 3                                                                                                 |
#                                                 /---------------------------------\                                        |
#                                                 |  FROM HACKER , BY OUALID AAZAB  |                                        |
#                                                 \--------------------------------/                                         |
#                                                                                                                            |
#**************************************************************************************************************************//
if __name__ == '__main__':
    n = int(input("Enter how many student in this class :"))
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter the name :") 
if query_name in student_marks:
    avrage_score =student_marks[query_name] 
print(round(sum(avrage_score)/len(avrage_score),2)) 








 
