
 #import the library
import streamlit as st
import pickle
#from pyngrok import ngrok
import os

pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
  
# add title to your app
st.title("Know-Your-Internship-chances")
#st.markdown("Designed by **Neesham**")

#st.subheader("Fork Me!")
#st.header("https://github.com/Neeshamraghav012/Placements-Prediction")



def prediction(Age, CGPA, Hostel, Gender, HistoryOfBacklogs, Internships):


	if Gender == 'Male':
		Gender = 1

	elif Gender == 'Female':
		Gender = 0

	if (HistoryOfBacklogs == 'Yes'):
		HistoryOfBacklogs = 1 

	elif (HistoryOfBacklogs == 'No'):
		HistoryOfBacklogs = 0


	ans = ""
	predict = classifier.predict([[Age, Gender, Internships, CGPA, Hostel, HistoryOfBacklogs]])

	if predict == 1:

		ans = 1

	else:

		ans = 0

	return ans

#print(prediction(19, 5, 'No', 'Male', 'No', 0))

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 




Gender = st.selectbox('Gender', ("Male","Female"))

Age = st.selectbox('Age', [17, 18, 19, 20, 21, 22, 23, 24])

CGPA = st.selectbox('CGPA', [5, 6, 7, 8, 9, 10])

#Hostel = st.selectbox('Hostel', ["Yes", "No"])

HistoryOfBacklogs = st.selectbox('Any Backlogs?', ['Yes', 'No'])

Internships = st.selectbox('Internships', [0, 1, 2, 3])

if st.button("Predict"): 
    result =  prediction(Age, CGPA, 0, Gender, HistoryOfBacklogs, Internships)

    if result == 1:
    	st.success("Yeah Sure! You Will Get Internship.")

    else:
    	st.warning("Oops, Not Yet.")

st.write("Go Back to Hire Easi [link](https://hire-easy.herokuapp.com/)")