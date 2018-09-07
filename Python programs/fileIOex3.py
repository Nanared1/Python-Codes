#Nana Abekah
#Test Processor - File Reading

correct = '';
student = [];
answers = [];
words = [];
with open('ex3.txt', 'r') as file:
    for line in file:
        words.append(line);
correct = words[0];
def percent(string):
    count = -1;
    string = string.upper();
    for x in range(len(string)):
        if(correct[x] == string[x]):
            count += 1;
    return((count/(len(string)-1))*100);

for x in range(1, len(words)):
    if(x%2 is 0):
        answers.append(words[x]);
    else:
        student.append(words[x]);

for x in range(len(answers)):
    print(student[x],int(percent(answers[x])),'%');



