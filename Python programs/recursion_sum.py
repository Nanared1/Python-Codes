#Nana Abekah
#Recursion - addition of a list of numbers

def add_num(num_list):
    if(len(num_list) == 1):
        return(num_list[0]);
    else:
        return(num_list[0] + add_num(num_list[1:]));

print(add_num([2,4,5,6,7]));
