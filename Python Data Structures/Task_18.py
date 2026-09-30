student = {
    "Ridham": 85,
    "Rahul": 90,
    "Prince": 78
}

reversed_dict = {}

for key, value in student.items():
    reversed_dict[value] = key

print("Original Dictionary:", student)
print("Reversed Dictionary:", reversed_dict)