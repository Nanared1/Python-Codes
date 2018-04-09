##Nana Abekah
##ICS-4U0
##March 23 2018
##Lists Test
##Mr. Veera

#First, ask user for number of students being paired
no_students = int(input("How many students are in the class: "));
#Make a list to receive the first names of the students
name_students_1 = [str(x) for x in input('Names: ').split()]; ##This will run until the user presses 'Enter'. It allows multiple inputs on one line and is split by a space.
#Receive the second pair in different orders
name_students_2 = [str(x) for x in input('Names: ').split()];
##Now, check to see if it is consistently matched
##my idea is to make pairs of the names,
##then sort the names out to make checking them easy.
##If the names in the list are found twice in the original list, then it's consistently paired.
pairs = []; ##Receives the pairs of students, the indexes of each list are paired together to make a 2d list.
##add the names to the pairs list
for x in range(no_students):
    pairs.append([name_students_1[x],name_students_2[x]]);
    pairs[x].sort();##Sorts the names out to make it easy to check if the list have the same elements.
paired = False;## boolean to keep up with the checking.
##This loops takes one list in the pairs 2d list and checks for # of occurences.
for x in range(len(pairs)):
    add = 0;
    for i in range(len(pairs)):
        if(pairs[x] == pairs[i]):
            add+=1;
    if(add==2):##If a list has shown up twice, then its consistent so set the paired boolean to true;
        paired = True;
    ##if it's not been found twice, then set the paired boolean to false and stop checking for consistency.
    else:
        paired = False;
        break;
##Print good or bad depending on whether if it's paired of not.
if(paired == True):
    print("Good");
else:
    print("Bad");

##Have a good day :)


