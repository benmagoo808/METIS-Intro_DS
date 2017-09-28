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


### Multiplying Matrices
We can multiply any two matrices that share the Y value of the left matrix and the X value of the right matrix, or simply put
the inner pair of values. i.e. 3x2 and 2x4 or 4x2 and 2x3 but not 2x3 and 2x4. X being the rows and Y being the columns. To do
so, you work left to right on the left matrix and top to bottom on the right matrix multiplying each pair of values and 
finding the sum of each series. That sum becomes the top left number of the answer matrix and we work left to right across
each row, then again for the next column. The answer matrix will always be of the shape of the outside pair of values, or the
X of the left and the Y of the right matrix. So,
![alt text](https://curiousbensite.files.wordpress.com/2017/09/img_1616.jpg)
