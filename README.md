# METIS-Intro_DS
## Projects for the Metis Intro to Data Science course

# Pre Course Problems
### See most_common_word.py for my solution to the most common word in a sentence.
This script is fairly well understood by the comments but the general theory behind my solution was:
1. Create and clean a list of words from the input.
* create a list of the words in the sentence using spaces as breaks
* clean any punctuation marks or numbers from the list using reg ex
* convert to all lower case
2. Find the most common word (mode)
* create a dictionary with the words as key and frequency in list as value
* iterate through dict to compare frequency with a counter variable and if greatest frequency set mode as the key (the word)
* if more than one word, append word to answer variable as a comma seperated value
3. Print Answer


### Difference between Correlation and Co-variance
