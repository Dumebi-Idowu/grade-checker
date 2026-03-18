def get_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 45:
        return 'D'
    else:
        return 'F'

def analyze(student_name, score):
    score = int(score)
    grade = get_grade(score)

    print("Grade Report")
    print("------------")
    print(f"Student: {student_name}")
    print(f"Score:   {score}")
    print(f"Grade:   {grade}")

    if grade == 'F':
        print("Status:  ❌ Failed")
    else:
        print("Status:  ✅ Passed")

if __name__ == "__main__":
    import os

    student_name = os.environ.get("STUDENT_NAME", "Unknown Student")
    score = os.environ.get("STUDENT_SCORE", "0")

    analyze(student_name, score)