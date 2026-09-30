students = {
    "Rahul": 85,
    "Ridham": 92,
    "Prince": 78
}

highest = max(students, key=students.get)

print("Highest marks:", highest)