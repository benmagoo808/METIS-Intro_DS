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


### Difference between Correlation and Covariance
It is my understanding that correlation and covariance are two similar ways of showing relationships between variables in a statistical sample or population. 
Two variables that are correlated are influenced by each other, either positively or negatively. This
is shown by a coeffecient of -1 to 1. -1 being perfectly negatively correlated and for every increase in x, we will see an
exact relative decrease in y. This is true regardless of scale. 0 being absolutely no influence on each other. 
Covariance is a similar relationship where two variables move together, although the relationship is shown by any positive or
negative number. The higher the variable values, the higher the number, but for variables of the same scale, the higher the
covariance, the more closely related the variables are. Correlation makes it easy to compare relationships, whereas covariance
is more specific to a pair of variables. To find correlation from covariance, you divide the covariance by the product of the
standard distribution of the two variables. To find covariance you find the product of the mean and each data point for each
variable and divide by the number of data points in the population or number of data points in the sample minus one. 
