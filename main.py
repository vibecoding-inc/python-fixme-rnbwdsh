def main():
    names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
    grades = [85, 42, 60, 49, 90]
    students = dict(zip(names, grades))
    passing_grades = [grade for grade in students.values() if grade >= 50]
    if (count := len(passing_grades)) > 0:
        average = sum(passing_grades) / count
        print(f"Processing complete.\nPassing Student Count: {count}")
        print(f"Average Grade of Passing Students: {average}")
    else:
        print("No passing students.")

if __name__ == "__main__":
    main()