import streamlit as st
import pandas as pd
import numpy as np
#from numpy import random

# streamlit run ./app.py to run the streamlit app 
# 1. USING COMMENTS TO DISPLAY in app
"""
### Block comments

you can use pythons block comment syntax in order to put some tx on app
* test1
* test2

1 Hi \n
2 Hello \n
3 Hi \n


"""

#2 DISPLAYING PANDAS DATAFRAM AS TABLE is as easy as below
df = pd.DataFrame({'first':[1,2,3,4],'second':[10,20,30,40]})
df


#3 WRITE METHOD
st.write("A method to write stings")
st.write(df)
st.table(df)

# FOR LINE CHAT
st.write("### You can use streamlit to draw scharts and maps")
df_chart = pd.DataFrame(data=np.random.randn(20,3), columns=['a','b','c'])
st.line_chart(df_chart)

map_data = pd.DataFrame( 
    np.random.randn(1000,2)/[50,50] + [36.76,-122.4], columns = ['lat','lon'])
st.map(map_data)



#STREAMLIT widgets
st.write("### Streamlit Widgets:")
st.write("# SLider")

slider = st.slider (label = "Number x", min_value = 1,max_value=100,
                    value = 3, step =1)
st.write(f'{slider} suqared is {slider*slider}')

# Any interaction with the widget in the screen. streamlit runs entire script from top to bottom


# Button
button = st.button(label="A button")
if button:
    st.write("button was clicked")

#select box
selectbox = st.selectbox(label ="A selection",
                         options = ['option 1','option2', 'option3'])
if selectbox == "option2":
    st.write("option 1 was selected")


#Every widget with a key is automatically added to Session State:
st.text_input ("Please enter your name", key="name")
st.session_state.name

text= st.text_input ("Please enter your name")
if text:
    st.write(text)


# Check box
if st.checkbox("show chart data"):
    st.line_chart(chart_data)

add_selectobx = st.sidebar.selectbox(
    "Options?",options =["email","phone"])

add_slider =  st.sidebar.slider (label = "Number x", min_value = 1,max_value=100,value = (3,20))


# use st.columns to layout app