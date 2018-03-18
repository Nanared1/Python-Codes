num_students = int(input());
names_1 = [str(x) for x in input().split()];
names_2 = [str(x) for x in input().split()];
Snames_1 = sorted(names_1, key=lambda x:x[:len(names_1)])
Snames_2 = sorted(names_2, key=lambda x:x[:len(names_2)])

it = True;
same = True;
for x in range(num_students):
    if Snames_1[x] == Snames_2[x]:
        same = True;
    else:
        same = False;
        break;

if(same is True and names_1[num_students-1] != names_2[num_students-1]):
    print("good");
else:
    print("bad");


##for x in range(num_students):
##    if(names[])
