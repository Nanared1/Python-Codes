## This does not fully work. I need to work on next day and previous day. Also St.Johns needs the correct minute


hour =  int(input("Hour: "));
minute = int(input("Minute: "));
day = input("Day: ");
hour1= hour*100;
mil_time = hour1+minute;

Victoria = mil_time-300;
Edmonton = mil_time-200;
Winnipeg = mil_time-100;
Toronto = mil_time;
Halifax = mil_time+100;

day = "Same Day";
def clock(city):
    if(city > 2359):
        city-=2359;
        day = "Next Day";
        return(city);
    elif(city < 0000):
        city+=2359;
        day = "Previous Day"
        return(city);
    else:
        day = "Same day";
        return(city);
st_day = "same day";
st_min = minute+30;
st_hr = hour+1;
if(st_min >= 60):
    st_min-=60;
    st_hr+=1;
if(st_hr > 23):
    st_hr-=23;
    st_day = "Next Day";
elif(st_hr < 0):
    st_hr+= 23;
    st_day = "Previous Day";
St_Johns = (st_hr*100)+st_min;

print(day, "%04d" % (clock(mil_time)), "in Ottawa");
print(day, "%04d" % (clock(Victoria)), "in Victoria");
print(day, "%04d" % (clock(Edmonton)), "in Edmonton");
print(day, "%04d" % (clock(Winnipeg)), "in Winnipeg");
print(day, "%04d" % (clock(Toronto)), "in Toronto");
print(day, "%04d" % (clock(Halifax)), "in Halifax");
print(day, "%04d" % (clock(St_Johns)), "in St.Johns");



