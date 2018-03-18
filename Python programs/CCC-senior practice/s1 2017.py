k = int(input());
swift = [int(x) for x in input().split()];
semaphores = [int(x) for x in input().split()];
acc = 0;
a = 0;
b = 0;
for x in range(0,k):
    a += swift[x];
    b += semaphores[x];
    if(a is b):
        acc = x+1;
print(acc);
