def calculate_gpa(subjects):
    # 평점 매핑
    grade_to_point = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'D+': 1.5,
        'D0': 1.0,
        'F': 0.0
    }

    total = 0
    sum = 0

    for subject in subjects:
        part = subject.split()
        credit = float(part[1])
        grade = part[2]

        if grade != 'P':
            total += credit
            sum += credit * grade_to_point[grade]

    if total == 0:
        return 0.0

    return sum / total

subjects = [input().strip() for _ in range(20)]

gpa = calculate_gpa(subjects)

print(gpa)