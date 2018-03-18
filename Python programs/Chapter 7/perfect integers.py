def perfect(num):
    account = 0;
    for x in range(1,num):
        if num%x == 0 and x is not num: 
            account+=x;
    if(account == num):
        return(True);
    else:
        return(False);

for i in range(1, 101):
    if perfect(i):
        print(i);

    
