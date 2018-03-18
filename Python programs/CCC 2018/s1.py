n = int(input());
v = [];
c = [];
for x in range(n):
    v.append(int(input()));
v.sort();

for x in range(1,(n-1)):
    count = ((v[(x-1)] - v[x])/2) +((v[x] - v[x+1])/2);
    c.append((count*-1));
c.sort();
print(c[0]);
