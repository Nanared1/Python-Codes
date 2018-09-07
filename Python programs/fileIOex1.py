##Nana Abekah
##May 09 2018
words = '';
length = 0;
sentence = '';
count = 0;
with open('data.txt', 'r') as file:
    for line in file:
        words = line;
words = list(words);
for i in range(len(words)):
    if(not words[i].isalpha()):
        words[i] = ' ';
    else:
        count += len(words[i]);
for i in range(len(words)):
    sentence += words[i];   
print('Average Word Count is: ', count/len(sentence.split(' ')),'\nNumber of words are: ', len(sentence.split(' ')));
