if __name__ == '__main__':
    records = []

    # Input number of students
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    # Get all unique scores, sort them, and find second lowest
    scores = sorted(set([x[1] for x in records]))
    second_lowest = scores[1]

    # Get names of students with the second lowest score
    names = sorted([x[0] for x in records if x[1] == second_lowest])

    # Print names
    for name in names:
        print(name)
