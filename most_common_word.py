import re

# Get Sentence and return as clean sorted word list
def get_clean_word_list():

    print('Welcome to the most common word finder! \nPlease enter a sentence '
          'below to find the most common word. \nPress "Enter" to submit.')
    # Create a list of words from input, using whitespace to split
    sentence = list(input().split(' '))
    # Use Reg Ex to remove punctuation and then sort to order in lowercase
    for i in range(len(sentence)):
        w = sentence[i]
        sentence[i] = re.sub(r'[^\w\s]', '',w)
    sentence.sort(key=str.lower)
    for i in range(len(sentence)):
        w = sentence[i]
        sentence[i] = w.lower()

    return sentence


# Find most common word in cleaned list, print and return as string
def get_most_common(word_list):
    # create a dictionary which stores the word and its frequency, and a counter
    # for most frequent, also the most_common word as a string
    totals = {}
    freq = 0
    most_common = str()

    for word in word_list:
        # for key:val in dict, make the val the number of times key appears
        # in dict with 0 as default
        totals[word] = totals.get(word, 0) + 1
    for val, count in totals.items():
        # Compare count in dict to counter for most frequent, if more change
        # the value of most_common, if equal, append to string
        if count > freq:
            freq = count
            most_common = val
        elif count == freq:
            most_common = str(val + ', ' + most_common)
    return most_common, freq


word_list = get_clean_word_list()
most_common, freq = get_most_common(word_list)
# Print output
print('The word(s) which appear the most are: ')
print(most_common.title())
print('Appearing ' + str(freq) + ' times')