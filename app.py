import streamlit as st
import pickle 
import pandas as pd 
import numpy as np  
from PIL import Image 


pickle_in = open("classifier.pk1","rb")
classifier=pickle.load(pickle_in)

def predict_depression(Gender, Age, Education, Interest,
       Energy, Self_Worth, Concentration, Restlessness,
        Job,  Study_Hours,
       Gadgets_Count, Social_Media_Hours):
    
    prediction=classifier.predict([[Gender, Age, Education, Interest,
       Energy, Self_Worth, Concentration, Restlessness,
        Job,  Study_Hours,
       Gadgets_Count, Social_Media_Hours]])
    
    print(prediction)

    return prediction

def main():
 st.title("Depression Analyser")
 st.write("Please feel free to enter rhe data")
 st.write("[Data is end to end encrypted >](https://google.com)")
 html_temp = """
    <div style="background-color:tomato;padding:10px;margin:20px   .radio-placeholder > .stRadio > label > span {
        color: #999999;
    }">
    <h2 style="color:white;text-align:center;">Depression Analyser </h2>
    </div>
    
    """
 st.markdown(html_temp,unsafe_allow_html=True)
 st.subheader("Enter the data:")
 name=st.text_input("Name","Type here")
 Gender = st.radio("Select your gender", ("Male", "Female"), key="gender")
 Age=st.radio("Select age group",("18 years or less","19 to 24 years","25 years and above"),key="age")
 Education=st.radio("Education",("College - Bachelor's","High School","Master"),key="education")
 Interest=st.radio("Rate your interest",(1,2,3,4),key="interest")
 Energy=st.radio("Energy level",(1,2,3,4),key="energy")
 Self_Worth=st.radio("Feeling bad about yourself or that you are a failure or not have let yourself or your family down",(1,2,3,4),key="self_worth")
 Concentration=st.radio("Trouble concentrating on things, such as reading the newspaper or watching television",(1,2,3,4),key="concentration")

 Restlessness=st.radio("Moving or speaking so slowly that other people could have noticed Or being so restless   that you have been moving around a lot more than usual",(1,2,3,4),key="Restlessness")
 #Accommodation=st.radio("Which of the following best describes your term-time accommodation?",("Home (with parents)","Private rented accommodation","University hall of residence"),key="Accommodation")
 Job=st.radio("Do you have part-time or full-time job?",("Full time","No","Part time"),key="Job")
 Study_Hours=st.radio("How many hours do you spend studying each day?",("1 - 2 hours","2 - 4 hours","More than 4 hours"),key="Study_Hours")
 Gadgets_Count=st.radio("How many of the electronic gadgets  (e.g. mobile phone, computer, laptop, PSP, PS4, Wii, etc.)",("1 - 3","4 - 6","More than 6","None"),key="Gadgets_count")
 Social_Media_Hours=st.radio("How many hours do you spend on social media per day?",('1 - 2 Hours','2 - 4 Hours','More than 4 Hours','Not Applicable'),key="Social_Media_Hours")
 
 result="" 

 if(Gender=='Male'):
    Gender=1
 else:
    Gender=0

 if(Age=='18 years or less'):
    Age=0
 elif Age=='19 to 24 years':
    Age=1
 else:
    Age=2  

 if(Education=="College - Bachelor's"):
    Education=0
 elif Education=='High School':
    Education=1
 else:
    Education=2      

 if (Job=='Full time'):
    Job=0
 elif (Job=='No'):
    Job=1
 else: 
    Job=2    
    

 if Study_Hours=='1 - 2 hours':
    Study_Hours=0
 elif (Study_Hours=='2 - 4 Hours'):
    Study_Hours=1
 else:
    Study_Hours=2 

 if Gadgets_Count=='1 - 3':
    Gadgets_Count=0
 elif (Gadgets_Count=='4 - 6'):
    Gadgets_Count=1
 elif (Gadgets_Count=='More than 6'):
    Gadgets_Count=2
 else:
    Gadgets_Count=3       

 if Social_Media_Hours=='1 - 2 hours':
    Social_Media_Hours=0
 elif (Social_Media_Hours=='2 - 4 Hours'):
    Social_Media_Hours=1
 elif Social_Media_Hours=='More than 4 Hours':
    Social_Media_Hours=2  
 else:
    Social_Media_Hours=3   
    
      
     
 
  
 if st.button("Predict"):
    result=predict_depression(Gender, Age, Education, Interest,
       Energy, Self_Worth, Concentration, Restlessness,
        Job,  Study_Hours,
       Gadgets_Count, Social_Media_Hours)
    st.success("Depression level:")    
    if(result==0):
       res="Not depressed "   
    else:
       res="Depressed"   
    st.subheader(res)   
if __name__ == "__main__": 
 main()

