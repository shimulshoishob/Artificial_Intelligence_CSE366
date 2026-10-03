# CSE366 Artificial Intelligence Lab 01 - basics.py
# Run: python basics.py

# ---------- Variables and types ----------
name = "Rahim"          # str
age = 21                # int
cgpa = 3.65             # float
is_student = True       # bool
print(f"{name} is {age} years old, CGPA {cgpa}")

# ---------- Lists, tuples, dictionaries, sets ----------
courses = ["CSE366", "CSE405", "MAT205"]   # list (changeable, ordered)
point = (3, 4)                              # tuple (cannot change)
marks = {"CSE366": 85, "CSE405": 78}       # dictionary (key -> value)
visited = {"A", "B"}                        # set (no duplicates)

courses.append("CSE477")
marks["MAT205"] = 90
visited.add("A")                            # ignored: already present

# ---------- Conditions and loops ----------
for course, mark in marks.items():
    grade = "A" if mark >= 80 else "B"
    print(course, mark, grade)

# ---------- List comprehension ----------
squares = [x * x for x in range(1, 6)]          # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

# ---------- Functions ----------
def manhattan(p, q):
    """Distance used as a heuristic on grids (Chapter 3)."""
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

print(manhattan((0, 0), (3, 4)))   # 7

# ---------- Classes ----------
class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def is_honours(self):
        return self.cgpa >= 3.5

s = Student("Karim", 3.8)
print(s.name, s.is_honours())      # Karim True
