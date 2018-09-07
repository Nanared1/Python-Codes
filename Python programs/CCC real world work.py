##Nana Abekah
##Wednesday, May 5, 2018
##Mr. Veera
##ICS 4U0
##CCC 1998 Problem C

###########################################################
#   Category        Proposed Time       Actual Time       #
#   Concept         15:00.00              17:58.81        #
#   Design          15:00.00              13:30.94        #
#   Building        30:00.00              4:04:46.46      # 
#   Debugging       10:00.00              20:00:00        #
#   Testing         10:00.00                              #
###########################################################

#   key info
#   'move ahead' = 1; next line indicates distance to move forward; two line inputs
#   'turn right' = 2; 90 degree turns; single line inputs
#   'turn left' = 3; 90 degree turns; single line inputs

#####################   PLAN    #####################
# 1. Receive user input
# 2. Sort list out into 'turns' and 'distances'
#   -   Use a for loop to make 2D list. The length should be #of excursions.
#   -   If there is a distance before a turn in the 
# 3. Check for 2 turns next to each other. If this is true,
#    subtract next distance from previous distance.
# 4. Find the shortest distance back by adding the distances list.
# 4. Figure out the final direction of the rover.
# 5. Figure out the final coordinates of the rover.
# 6. Find the shortest path by making a set of conditions
# 7. Print out the shortest steps as well as the 

##Make lists and receive user input

excursions = int(input()); ##Get number of excursions;
sequences = []; ##List to keep sequence of each excursion;
for x in range(excursions):
    record_seq = []; # Temporary list to keep track to user_input
    user_in = int(input());
    # There should be no zeros in the sequences list
    if user_in is not 0:
        record_seq.append(user_in);
    while(user_in is not 0):
        user_in = int(input());
        if user_in is not 0:
            record_seq.append(user_in); ## add user inputs to the temporary list
    sequences.append(record_seq); ## add the temporary list to the sequence list.

##Sort the list for distances and turns

distances = [];
turns = [];

for x in range(excursions):
    xi = []; ##temporary list for turns list
    ix = []; ##temporary list for distances

    ## Sort out the turns and the distances
    for i in range(len(sequences[x])):
        if sequences[x][i] is 1:
            
            ## Prevent a compiler error if the index is out of range
            try:
                ix.append(sequences[x][i+1]);
                xi.append(4); ## '4' is a place holder to indicate that, there is a move before a turn
            except IndexError:
                continue;
        elif sequences[x][i-1] is not 1:
            xi.append(sequences[x][i]);

    ## Add the 'xi' and 'ix' temporary list to the main turn and distance list
    distances.append(ix); 
    turns.append(xi);

## check if 2 'right' or 2 'left' turns are next to each other.
## If they are remove them and add -2 to distances.

for x in range(len(turns)):
    for i in range(len(turns[x]) - 1):
        try:
            if(turns[x][i] is turns[x][i+1]):
                del turns[x][i+2];
                sub = distances[x][-2] - distances[x][-1];
                del distances[x][-2:];
                distances[x].append(sub);
        except Exception:
            continue;
            
## Add the distances and store it in each list added
for x in range(len(distances)):
    add = 0;
    for i in range(len(distances[x])):
        add += distances[x][i];
    if add < 0:
        add = 0;
    distances[x].append(add);

## Figure out short part and correct sequence
final_steps = []; origin = [0,0]; pos = [0,0]; direct = 0;

for x in range(len(turns)):
    origin = [0,0]; pos = [0,0]; direct = 0; dcount = 0;
    
    for i in range(len(turns[x])-1):
        if(turns[x][i] is 3):
            if(turns[x][i+1] is 4):
                if(direct is 0):
                    pos[0]-= distances[x][dcount];  dcount+=1;  direct = 270;
                elif(direct is 270):
                    direct = 180;   pos[1]-=distances[x][dcount];   dcount+=1;
                elif(direct is 180):
                    direct = 90;    pos[0]+=distances[x][dcount];   dcount+=1;
                elif(direct is 90):
                    direct = 0;     pos[1]+=distances[x][dcount];  dcount+=1;
            elif(turns[x][i+1] is 3):
                if(direct is 0):
                    direct = 180;
                elif(direct is 270):
                    direct = 90;
                elif(direct is 180):
                    direct = 0;
                elif(direct is 90):
                    direct = 270;
            elif(turns[x][i+1] is 2):
                direct = direct;
                
        elif(turns[x][i] is 2 and turns[x][i+1] is 4 and turns[x][i] is not 4):
            if(turns[x][i+1] is 4):
                if(direct is 0):
                    pos[0]+= distances[x][dcount];  dcount+=1;  direct = 90;
                elif(direct is 90):
                    direct = 180;   pos[1]-=distances[x][dcount];   dcount+=1;
                elif(direct is 180):
                    direct = 270;   pos[0]-=distances[x][dcount];   dcount+=1;
                elif(direct is 270):
                    direct = 0;     pos[1]+=distances[x][dcount];  dcount+=1;
            elif(turns[x][i+1] is 2):
                if(direct is 0):
                    direct = 180;
                elif(direct is 270):
                    direct = 90;
                elif(direct is 180):
                    direct = 0;
                elif(direct is 90):
                    direct = 270;
            elif(turns[x][i+1] is 3):
                direct = direct;
                
        elif(turns[x][0] is 4 and i is 0):
            direct = 0;     pos[1]+=distances[x][0];    dcount+=1;

    if(pos[0] > 0 and pos[1] < 0): ##(+,-)
        if(direct is 90):
            final_steps.append([3,1,abs(pos[1]),3,1,abs(pos[0])]);
        elif(direct is 180):
            final_steps.append([2,1,abs(pos[0]),2,1,abs(pos[1])]);
        elif(direct is 270):
            final_steps.append([2,1,abs(pos[1]),3,1,abs(pos[0])]);
        else:
            final_steps.append([1,abs(pos[1]),3,1,abs(pos[0])]);
    elif(pos[0] > 0 and pos[1] > 0): ##(+,+)
        if(direct is 90):
            final_steps.append([2,1,pos[1],2,1,pos[0]]);
        elif(direct is 180):
            final_steps.append([1,abs(pos[1]),2,1,abs(pos[0])]);
        elif(direct is 270):
            final_steps.append([1,abs(pos[0]),3,1,abs(pos[1])]);
        else:
            final_steps.append([3,1,abs(pos[0]),3,1,abs(pos[1])]);
    elif(pos[0] > 0 and pos[1] > 0): ##(-,+)
        if(direct is 90):
            final_steps.append([3,1,pos[1],2,1,pos[0]]);
        elif(direct is 180):
            final_steps.append([3,1,abs(pos[0]),3,1,abs(pos[1])]);
        elif(direct is 270):
            final_steps.append([2,1,abs(pos[1]),2,1,abs(pos[0])]);
        else:
            final_steps.append([1,abs(pos[1]),2,1,abs(pos[0])]);
    elif(pos[0] < 0 and pos[1] > 0): ##(-,+)
        if(direct is 90):
            final_steps.append([1,pos[0],2,1,pos[1]]);
        elif(direct is 180):
            final_steps.append([1,abs(pos[1]),3,1,abs(pos[0])]);
        elif(direct is 270):
            final_steps.append([3,1,abs(pos[1]),3,1,abs(pos[0])]);
        else:
            final_steps.append([2,1,abs(pos[0]),2,1,abs(pos[1])]);
    else:
        final_steps.append([0]);

for x in range(excursions):
    if(distances[x][-1] > 0):
        print("\nDistance is ", distances[x][-1]);
        for i in final_steps[x]:
            print(i);
    else:
        print("\nDistance is ", distances[x][-1])
                
