##Nana Abekah
##April 9th, 2018
##Objects and Classes Test 2
##ICS 4UO
##Mr. Veera

## student class, contains all required student data
class student():
    def __init__(self, stu_number):
        self.s_number = stu_number;
        self.s_FirstName = '';
        self.s_LastName = '';
        self.s_age = 0;
        self.s_course = [];
    def getFirstName(self, name):
        self.s_FirstName = name;
    def getLastName(self, name):
        self.s_LastName = name;
    def getAge(self, age):
        self.s_age = age;
    def sNumber(self):
        return(self.s_number);
    def enroll_course(self, name):
        self.s_course.append(name);
    def list_course(self):
        return(self.s_course);
    def get_info(self):
        print("Student #: ", self.s_number);
        print("First Name: ", self.s_FirstName);
        print("Last Name: ", self.s_LastName);
        print("Age: ", self.s_age);
        print("Courses: ", self.s_course);
    def __repr__(self):
        print(self.s_FirstName, self.s_LastName);

## course class to keep track of students in cours
class course():
    def __init__(self, name):
        self.course_name = name;
        self.students = [];
    def add_student(self, s_number):
        self.students.append(s_number);
    def show_student(self):
        print(self.course_name,": ", self.students);
    def __repr__(self):
        print(self.course_name);

science = course("Science"); # course object call 'science'
computers = course("computer Science"); # course object call 'computers'
math = course("Math"); # course object call 'math'

##Student object called 'Nana'
nana = student(803356);
nana.getFirstName("Nana");
nana.getLastName("Abekah");
nana.getAge(17);
nana.enroll_course("Science");
nana.enroll_course("Computers");

science.add_student(nana.sNumber()); ## Enroll Nana in science
computers.add_student(nana.sNumber()); ## Enroll Nana in computers

##Student object called 'Senthura'
sen = student(555546);
sen.getFirstName("Senthura");
sen.getLastName("Yogaragan");
sen.getAge(18);
sen.enroll_course("Science");
sen.enroll_course("Math");

science.add_student(nana.sNumber()); ## Enroll Senthura in science
math.add_student(nana.sNumber()); ## Enroll Senthura in math

nana.get_info(); ## print Nana's info
print();
sen.get_info(); ## print Senthura's info
