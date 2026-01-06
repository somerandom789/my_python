for repeat in range(4):
    grades = list(input(f"Enter grades: ").split())
    count_a = grades.count("A")
    total = len(grades)
    result = count_a / total
    print(f"{int(result)}.{int(result % 1 * 100):02}")

