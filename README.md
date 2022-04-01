# Hack_darwin
<h3 align="center">Hackathon output for the Charles Darwin Correspondence Project, University of Cambridge, April 2022</h3>

- the problem ❓ : find new insights into the 15000+ archived correspondence data of Charles Darwin 

- our solution 💡 : apply nlp techniques to predict characteristics about the sender of a letter

- our question 🤔 : how much can we tell about who is writing just from the languages they use?


Contained mostly within the Jupyter notebook, our code predicts the gender and occupation of Darwin's correspondences

We began our code by looking to predict the sex of the author of the letter based on the text within the letter. The data is very skewed, with Darwin writing more extensively to males, and males writing more frequently to Darwin, as to probably be expected from the correspondence of a 19c scientist.

Our code was adapted to try predict occupation of the letter author based on the language, but due to problems with the storing of the occupation in the data set, we have not managed to make as much progress on this problem as initially hoped. 

In conclusion, sex prediction can be done fairly accurately, but how useful of a solution this is is questionable, due to the heavy imbalance in the data. We provide a proof of concept for occupation inference. Though accuracy is limited, it could be taken further with a more thorough extraction of occupancy information from the data and with a more sophisticated language model.

