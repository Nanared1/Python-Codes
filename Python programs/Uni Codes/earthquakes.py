#Nana Abekah
#October 5, 2018
#Earthquake Assignment
#Comp 1001


country = input("Name of country ('DONE' to stop): ")
micro = 0;
vm = 0;
lm = 0;
sm = 0;
gr = 0;
met = 0;

while(country != 'DONE'):
    high = 0;
    avg = 0;
    eqCount = 0;
    mag = float(input("Enter magnitude of earthquake (-1 to stop): "));
    low = mag;
    while(mag != -1):
        avg = avg+mag;
        eqCount = eqCount+1;

        if(mag < 2.0):
            micro = micro + 1;
        elif((mag >= 2.0) and (mag < 4.0)):
            vm = vm+1;
        elif((mag >= 4.0) and (mag < 6.0)):
            lm = lm+1;
        elif((mag >= 6.0) and (mag < 8.0)):
            sm = sm+1;
        elif((mag >= 8.0) and (mag < 10.0)):
            gr = gr+1;
        elif((mag >= 10.0)):
            met = met+1;


        if(mag > high):
            high = mag;
        elif((mag < low)):
            low = mag;
        mag = float(input("Enter magnitude of earthquake (-1 to stop): "));
    if(eqCount != 0): ## This is to prevent a division by zero error
        avg = avg/eqCount;
    print("========================");
    print("Statistics for ", country);
    print("THe average magnitude earthquake for ", country, "is %.1f" % avg);
    print("THe lowest magnitude earthquake for ", country, "is ", low);
    print("THe highest magnitude earthquake for ", country, "is ", high);
    print("========================");
    country = input("Name of country ('DONE' to stp): ");

print("========================");
print("Total Earthquakes per category: ");
print("%-20s %7s" % ("Micro", micro));
print("%-20s %7s" % ("Very minor to minor", vm));
print("%-20s %7s" % ("Light to moderate", lm));
print("%-20s %7s" % ("Strong to major", sm));
print("%-20s %7s" % ("Great", gr));
print("%-20s %7s" % ("Meteoric", met));
