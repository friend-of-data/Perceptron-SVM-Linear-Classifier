import project1 as p1
import pickle
import numpy as np # type: ignore

#load saved dictionary and trained model parameter
with open('dictionary.pk1','rb') as f:
    dictionary=pickle.load(f)

with open('best_theta.pk1','rb') as f:
    best_theta=pickle.load(f)



# if __name__=='__main__':
#      user_input=input('Enter a sentence: ')
#      user_input_list=[user_input]
#      print(len(user_input_list))
#      bow_feature=p1.extract_bow_feature_vectors(user_input_list,dictionary)
#      print(bow_feature.shape,len(user_input))
def predict_sentiment(sentence, dictionary,best_theta):
    bow_feature=p1.extract_bow_feature_vectors(sentence,dictionary)
    print(bow_feature)
    theta_vector,bias = best_theta
    prediction=np.dot(bow_feature,theta_vector) + bias
    print(prediction)
    if prediction > 0:
        sentiment='Positive'
    else:
        sentiment = 'Negative'

    return sentiment

if __name__=='__main__':
    try:
        while True:
            user_input=input('Enter a sentence (or type exit to quit): ')
            if user_input.lower()=='exit':
                print('Exit sentiment analysis')
                break
            input_list=[user_input]
            sentiment=predict_sentiment(input_list,dictionary,best_theta)
            print(f'Sentiment: {sentiment}')
    except KeyboardInterrupt:
        print('Exit sentiment analysis')

