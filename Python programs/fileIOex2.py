#Nana Abekah
#May 10 2018
words = '';
keep = [];
temp = [];
##count_the = 0;
##count_zoo = 0;
##count_and = 0;

unique = '';

def check_unique(string):
    for x in range(len(unique)):
        if(string in unique):
            return True;
        else:
            return False;
with open('input.txt', 'r') as file:
##    for line in file:
##        temp.append(line);
##    keep.append(temp);
##words = words.lower().split(' ');
    for line in file:
        keep.append(line);
print(keep[0]);

for x in keep:
    temp.append(x.split(' '));
print(temp);
print(temp[0][2][0:1]);


lst1 = [1, 2, 3]
lst2 = lst1
del lst1[:]
print(lst2)

##words.sort();
##for i in range(len(words)):
##    if(check_unique(words[i])):
##        print(True)
##    elif(not check_unique(words[i])):
##        count = 0;
##        ##print(False);
##        for j in range(len(words)):
##            if(words[i] == words[j]):
##                count+=1;
##                ##print(j);
##        print(words[i], count);
##        unique+= " "+words[i];
##
##print(unique);

##for i in words:
##    if(i.lower()  == 'and'):
##        count_and += 1;
##    if(i.lower()  == 'the'):
##        count_the += 1;
##    if(i.lower()  == 'zoo'):
##        count_zoo += 1;
##
##print('WORD   OCCURENCES', '\nthe   ', count_the, '\nand   ', count_and,
##      '\nzoo   ', count_zoo)
##print(sorted(words, key=str.lower))

