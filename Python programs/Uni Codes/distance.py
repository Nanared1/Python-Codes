#Nana Abekah
#November 02, 2018
#Distance Assignment
#Comp 1001


'''
Distance function
returns decimal value calculated from xyz input
'''
def distance(a,b):
    x = (b[0] - a[0])**2;
    y = (b[1] - a[1])**2;
    z = (b[2] - a[2])**2;
    return((x+y+z)**(1/2));

'''
Sort a given list in descending order
and remove an occurrences of numbers
'''
def inSort(num):
    ## Loop through the given list starting from index 1
    for x in range(1, len(num)):
        keep = num[x]; ## Number to be checked through the list
        cursor = x-1; ## The index of the number being compared
        while(cursor >= 0 and keep > num[cursor]): ## check if the number next to keep is smaller
            ## if it is, swap the values
            num[cursor+1] = num[cursor];
            cursor -= 1;
        num[cursor+1] = keep;

    ## Remove occurrences of numbers in the sorted list
    x = 0;
    while(x < len(num)-1):
        if(num[x] == num[x+1]):
            del num[x];
        else:
            x += 1;
    return(num[:len(num)-1]);

def main():
    points = [[4,2,1],[-1,3,5],[6,9,-2],[8,-1,5]];
    lengths = [];
    close = [[],[]];
    closeD = distance(points[0], points[1]);
    '''
    Find the distance between every single point
    find the closest distance and retrieve the points of it.
    '''
    for x in range(len(points)):
        for i in range(len(points[x])):
            dis = distance(points[x], points[i]);
            lengths.append(dis);
            if((dis < closeD) and (dis != 0)):
                closeD = dis;
                close[0] = points[x];
                close[1] = points[i];

    '''
    Round distances to 2 decimal places and print them.
    '''
    sDistance = inSort(lengths);
    print("Sorted Distances: ");
    for x in sDistance:
        print("%.2f" % (x));
    print("Closest points were:");
    print(close[1], " and ", close[0], " with distance = %.2f" % closeD);

main();
