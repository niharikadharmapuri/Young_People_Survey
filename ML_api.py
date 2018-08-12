
from flask import Flask, request,jsonify, abort
import pandas as pd
import numpy as np
import json
import pickle
import os

app = Flask(__name__)

model_pkl=open('youngpeoplemodel.pkl','rb')
clf=pickle.load(model_pkl)
columns=['Music', 'Slow songs or fast songs', 'Dance', 'Folk', 'Country', 'Classical music', 'Musical', 'Pop', 'Rock', 'Metal or Hardrock', 'Punk', 'Hiphop, Rap', 'Reggae, Ska', 'Swing, Jazz', 'Rock n roll', 'Alternative', 'Latino', 'Techno, Trance', 'Opera', 'Movies', 'Horror', 'Thriller', 'Comedy', 'Romantic', 'Sci-fi', 'War', 'Fantasy/Fairy tales', 'Animated', 'Documentary', 'Western', 'Action', 'History', 'Psychology', 'Politics', 'Mathematics', 'Physics', 'Internet', 'PC', 'Economy Management', 'Biology', 'Chemistry', 'Reading', 'Geography', 'Foreign languages', 'Medicine', 'Law', 'Cars', 'Art exhibitions', 'Religion', 'Countryside, outdoors', 'Dancing', 'Musical instruments', 'Writing', 'Passive sport', 'Active sport', 'Gardening', 'Celebrities', 'Shopping', 'Science and technology', 'Theatre', 'Fun with friends', 'Adrenaline sports', 'Pets', 'Flying', 'Storm', 'Darkness', 'Heights', 'Spiders', 'Snakes', 'Rats', 'Ageing', 'Dangerous dogs', 'Fear of public speaking', 'Healthy eating', 'Daily events', 'Prioritising workload', 'Writing notes', 'Workaholism', 'Thinking ahead', 'Final judgement', 'Reliability', 'Keeping promises', 'Loss of interest', 'Friends versus money', 'Funniness', 'Fake', 'Criminal damage', 'Decision making', 'Elections', 'Self-criticism', 'Judgment calls', 'Hypochondria', 'Eating to survive', 'Giving', 'Compassion to animals', 'Borrowed stuff', 'Loneliness', 'Cheating in school', 'Health', 'Changing the past', 'God', 'Dreams', 'Charity', 'Number of friends', 'Waiting', 'New environment', 'Mood swings', 'Appearence and gestures', 'Socializing', 'Achievements', 'Responding to a serious letter', 'Children', 'Assertiveness', 'Getting angry', 'Knowing the right people', 'Public speaking', 'Unpopularity', 'Life struggles', 'Happiness in life', 'Energy levels', 'Small - big dogs', 'Personality', 'Finding lost valuables', 'Getting up', 'Interests or hobbies', "Parents' advice", 'Questionnaires or polls', 'Finances', 'Shopping centres', 'Branded clothing', 'Entertainment spending', 'Spending on looks', 'Spending on gadgets', 'Spending on healthy eating', 'Age', 'Height', 'Weight', 'Number of siblings', 'sm_current smoker', 'sm_former smoker', 'sm_never smoked', 'sm_tried smoking', 'al_drink a lot', 'al_never', 'al_social drinker', 'pu_i am always on time', 'pu_i am often early', 'pu_i am often running late', 'ly_everytime it suits me', 'ly_never', 'ly_only to avoid hurting someone', 'ly_sometimes', 'internet_few hours a day', 'internet_less than an hour a day', 'internet_most of the day', 'internet_no time at all', 'gender_female', 'gender_male', 'handedness_left handed', 'handedness_right handed', 'edu_college/bachelor degree', 'edu_currently a primary school pupil', 'edu_doctorate degree', 'edu_masters degree', 'edu_primary school', 'edu_secondary school', 'onlychild_no', 'onlychild_yes', 'town_city', 'town_village', 'house_block of flats', 'house_house/bungalow']


@app.route('/api', methods=['POST'])
def make_prediction():
    data=json.dumps(request.get_json(force=True))# read json obj n convert to json #string
    df=pd.read_json(data)#create pandas df using json string
    X=df[columns].as_matrix().astype('float')
    predictions=clf.predict(X)
    return predictions.to_json()

    
    return 'hello'
if __name__ == '__main__':
    # host flask app at port 10001
    app.run(port=9000, debug=True)
