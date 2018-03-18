original_sentence = input("Enter a sentence: ");
remove_word = input("Enter a string: ");

if remove_word in original_sentence:
    print(original_sentence[0:original_sentence.index(remove_word) - 1]+
          original_sentence[(original_sentence.index(remove_word) + len(remove_word)):]);
else:
    print("Can't remove string");
