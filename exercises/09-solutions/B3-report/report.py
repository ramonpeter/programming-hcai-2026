import csv


def read_grades(path):
    """Return a dictionary from each course to the list of its grades."""
    by_course = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            course = row["course"]
            if course not in by_course:
                by_course[course] = []
            by_course[course].append(int(row["grade"]))
    return by_course


def write_report(path, by_course):
    """Write one line per course with its size, mean and passes."""
    with open(path, "w", encoding="utf-8") as f:
        for course in sorted(by_course):
            grades = by_course[course]
            passed = len([g for g in grades if g >= 18])
            mean = sum(grades) / len(grades)
            line = f"{course}: {len(grades)} students, mean {mean:.1f}"
            f.write(f"{line}, {passed} passed\n")


if __name__ == "__main__":
    by_course = read_grades("grades.csv")
    print(by_course)
    write_report("courses.txt", by_course)
    with open("courses.txt", encoding="utf-8") as f:
        print(f.read(), end="")
