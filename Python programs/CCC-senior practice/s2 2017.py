n = int(input());
tides = [int(x) for x in input().split()];
low_tide = tides[0];
high_tide = tides[1];
newLowTide = [];
newHighTide = [];
finalTide = [];
for x in range(n):
    if(tides[x] <= low_tide):
        newLowTide.append(tides[x]);
    else:
        newHighTide.append(tides[x]);

newHighTide.sort();
newLowTide.sort(reverse = True);

##print(newHighTide);
##print(newLowTide);

for x in range(len(newHighTide)):
    finalTide.extend([newLowTide[x], newHighTide[x]]);

print(finalTide);
