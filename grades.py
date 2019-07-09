n = int(input("number of assignments:"))
grade_list = [] 

for i in range(0, n): 

    grades = int(input()) 
    grade_list.append(grades)
    x = min(grade_list)
    
if len(grade_list) > 4:
    grade_list.remove((x))
            
print(grade_list)  

avg = float(sum(grade_list)/len(grade_list))
print(round(avg, 2))

if avg >= 90:
    print("Grade: A")
elif 80 <= avg < 90:
    print ("Grade: B")
elif 70 <= avg < 80:
    print ("Grade: C")
elif 60 <= avg < 70:
    print ("Grade: D")
elif avg < 60:
    print ("Grade: F")
else: 
    print("Error")