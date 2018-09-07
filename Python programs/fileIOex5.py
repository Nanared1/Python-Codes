#Nana Abekah
#Merge Files - File Reading

file1 = [];
file2 = [];
file3 = [];
with open('file1.txt', 'r') as file:
    for line in file:
        file1.append(line);
        
with open('file2.txt', 'r') as file:
    for line in file:
        file2.append(line);

for element in file1:
    file1 = element.split(' ');

for element in file2:
    file2 = element.split(' ');
    
file3 = file1+file2;

file3 = [int(x) for x in file3];
file3.sort(key = int);
file3 = [str(x) for x in file3];

with open('file3.txt', 'w') as file:
    for num in file3:
        file.write(num+' ');
print(num);
