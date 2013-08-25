hackU
=====
README

The basic purpose of this application is to analyse the moods of a person over a certain period of time. Based on this, it will plot a graph of the person’s mood swings against time (the chart was made using YUI). It can also be used to determine the playlist (of songs) of a person according to his/her mood.
What differentiates this app from the standard ones used in sentiment analysis is the fact that it is individual centric instead of being used for determination of the general sentiment towards a particular product, movie, etc.
For this, we extracted the social networking data of a person (like Facebook posts) using FQL. This data is then run through the LibSVM algorithm which predicts the mood of a person (happy, sad, excited and angry were the four broad categories that we used). For this, we created a training corpus. Since we didn’t have a ready-made dataset for such a purpose, we used Twitter tweets, which we categorized into the above four categories. Thereafter we identified words that could be used as features for creating the input vector (we used nltk’s pos tagging for the same). So now each tweet is converted into a vector using these features.
Then LibSVM categorises the input into the aforementioned categories. Then it passes on this data to a web app. This web app then gives as output the mood of the person and the time frame. This data keeps getting refreshed every few seconds, and this is achieved using crontab.
