English = 78;
Advanced_Func = 76;
Physics = 72;

Chemistry = 67; ##Grade 11
Computer_sci = 96; ##Grade 11
Computer_eng = 94; ##Grade 11
##
































marks = [English, Advanced_Func, Physics, Chemistry, Computer_sci, Computer_eng];

subject_marks = {
    "English" : English,
    "Advanced Functions" : Advanced_Func,
    "Physics" : Physics,
    "Chemistry" : Chemistry,
    "Computer Science" : Computer_sci,
    "Computer Engineering" : Computer_eng
    };

average = sum(marks)/len(marks);
print(subject_marks);
print("Average: ",average);
    


