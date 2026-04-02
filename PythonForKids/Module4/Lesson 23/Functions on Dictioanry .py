# Sample dictionary
student = {
    "name": "Manomay",
    "age": 14,
    "grade": "A",
    "subjects": ["Math", "Physics", "Chess"],
    "city": "Mumbai",
    "height": 170
}

print("Original dictionary:", student)

# 1. dict.keys() - get all keys
print("Keys:", student.keys())

# 2. dict.values() - get all values
print("Values:", student.values())

# 3. dict.items() - get key-value pairs
print("Items:", student.items())

# 4. dict.get(key, default) - safely get value
print("Age using get():", student.get("age"))
print("Weight using get():", student.get("weight", "Not specified"))

# 5. dict.update() - update or add new key-value
student.update({"grade": "A+"})
print("After update:", student)

# 6. dict.pop(key) - remove a key and get its value
removed_grade = student.pop("grade")
print("Removed grade:", removed_grade)
print("After pop:", student)

# 7. dict.popitem() - remove last inserted item
last_item = student.popitem()
print("Removed last item:", last_item)
print("After popitem:", student)

# 8. dict.setdefault(key, default) - add key if not present
student.setdefault("country", "India")
print("After setdefault:", student)

# 9. dict.clear() - remove all items (we'll make a copy first)
student_copy = student.copy()
student_copy.clear()
print("After clear():", student_copy)

# 10. dict.copy() - shallow copy of dictionary
student_copy2 = student.copy()
print("Copy of student:", student_copy2)
 