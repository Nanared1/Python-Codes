#Nana Abekah
#Strings and Loops Quiz
#February 15, 2017
#Mr. Veera
#ICS 4U0

user_input = input("Enter words to be translated: ");

#function to translate from American to Canadian
def Translate(string):
    #find = "or";
    replace = "our";
    #last_letters = string[len(string)-2:len(string)];
    return(string[0:len(string)-2] + replace);

def vowel(letter):
    if(letter is 'a' or letter is 'e' or letter is 'i' or letter is 'o' or letter is 'u' or letter is 'y'):
        return(False);
    else:
        return(True);
while True:
    if(len(user_input) > 4 and vowel(user_input[0]) and user_input[len(user_input)-2:len(user_input)] is not 'or'):
        print(Translate(user_input));
        user_input = input();
    elif user_input is "quit!":
        break;
    else:
        print(user_input);
        user_input = input();

    
