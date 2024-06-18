## General information
The codes in this repository demonstrates concepts and use case of linear classifier, specifically perceptron algorithm, average perceptron and one of perceptron's variation, Pegasos algorithm.<br>
<br>
It starts with implementing the necessary unit of the algorithm, hinge loss (first for a single data point and then for the wholde datasets), parameters update (also first single data point and then the whole datasets).<br>
<br>
In the end, the whole project checks a dataset consisting of website reviews and use the best performing algorithms among perceptron, average perceptron and Pegasos to do a sentiment analysis or classification. Namely, whether the review is positive or negative.<br>
<br>
## Key knowledge/ techniques applied
- Hinge loss function
- Perceptron algorithm
- Pegasos algorithm
- Support vector machine
- Large margin classifier
- Bag of words
- Unigram, bigrams, trigrams etc

## How to use
First run the the main.py (if you don't want to fine tune again or change other parameters in project1.py). The best model parameters and dictionary will be saved. \
Then run deploy.py. It deploys the best trained model and ask for your input to give a sentiment evaluation. Pretty cool, right?
## Disclaimer
Please note, this project is based on one of the homework of MIT online course MITx 6.86x. So you should not simply copy the code (where #your code here is designated in project1.py and main.py) and submit it as your own answer if you are also taking this course.
