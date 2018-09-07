#Nana Abekah
#MadLib - File Reading

import math
from random import randint

story = [];
nouns = [];
verbs = [];
sentence = [];
with open('story.txt', 'r') as file:
    for line in file:
        story.append(line);

with open('nouns.txt', 'r') as file:
    for line in file:
        nouns.append(line);

with open('verbs.txt', 'r') as file:
    for line in file:
        verbs.append(line);

for x in range(len(story)):
    story[x] = list(story[x]);

def random_words(letter):
    if(letter == '#'):
        num = randint(0,len(nouns)-2)
        rand = nouns[num];
        del nouns[num];
        return(rand[0:len(rand)-1]);
    elif(letter == '%'):
        num = randint(0,len(verbs)-2);
        rand = verbs[num];
        del verbs[num];
        return(rand[0:len(rand)-1]);
    else:
        return(letter);
    
for x in range(len(story)):
    temp = [];
    for i in range(len(story[x])):
        if(story[x][i] != '\n'):
            temp.append(random_words(story[x][i]));
    sentence.append(''.join(temp));

for x in sentence:
    print(x);
            
    
