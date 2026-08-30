course_A = {
    "25K-0105", 
    "25K-0106", 
    "25K-0107", 
    "25K-0108", 
    "25K-0109"
}

course_B = {
    "25K-0108", 
    "25K-0109", 
    "25K-0110", 
    "25K-0111", 
    "25K-0112"
}

both_courses = course_A.intersection(course_B)

only_course_A = course_A.difference(course_B)

only_course_B = course_B.difference(course_A)

all_unique_students = course_A.union(course_B)

print(f"Enrolled in both: {both_courses}")       
print(f"Only Course A: {only_course_A}")         
print(f"Only Course B: {only_course_B}")
print(f"All unique students: {all_unique_students}")
