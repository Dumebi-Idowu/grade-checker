# Development version - grade checker
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

def analyze(student_name, score, report_type):
    score = int(score)
    grade = get_grade(score)
    status = "✅ Passed" if grade != 'F' else "❌ Failed"

    print("Grade Report")
    print("------------")
    print(f"Student: {student_name}")
    print(f"Score:   {score}")
    print(f"Grade:   {grade}")
    print(f"Status:  {status}")

    # only shown in detailed report
    if report_type == 'detailed':
        print("\nDetailed Breakdown")
        print("------------------")
        print(f"A: 70 and above")
        print(f"B: 60 - 69")
        print(f"C: 50 - 59")
        print(f"D: 45 - 49")
        print(f"F: Below 45")
        print(f"\nYour score of {score} falls in grade {grade}")

if __name__ == "__main__":
    import os
    student_name = os.environ.get("STUDENT_NAME", "Unknown Student")
    score        = os.environ.get("STUDENT_SCORE", "0")
    report_type  = os.environ.get("REPORT_TYPE", "simple")

    analyze(student_name, score, report_type)