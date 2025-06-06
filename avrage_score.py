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








 
