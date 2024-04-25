import pandas as pd
import streamlit as st
import joblib
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('kidney_disease (1).csv')

st.markdown("<h1 style = 'color: #FF9800; text-align: center; font-size: 60px; font-family: Monospace'>KIDNEY DISEASE PREDICTION</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #FF204E; text-align: center; font-family: cursive '>Built by Rejoice Eze</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# Add an image
st.image('pngwing.com (5).png', caption = 'Built by Rejoice')   

#Add Project proble statement
st.markdown("<h2 style = 'color: #FF9800; text-align: center; font-family: montserrat '>Background Of Study</h2>", unsafe_allow_html = True)

st.markdown("Chronic Kidney Disease (CKD) is a significant global health issue affecting millions of people worldwide. It is characterized by the gradual loss of kidney function over time, often progressing silently until advanced stages are reached. Early detection and intervention are crucial for managing CKD effectively, preventing complications, and improving patient outcomes. Early identification of individuals at risk of developing CKD can enable timely interventions to slow disease progression, reduce complications, and improve quality of life. Predictive models for kidney disease can help healthcare providers identify high-risk patients, personalize treatment plans, and allocate resources more effectively.</p>", unsafe_allow_html=True)

# Sidebar design (to put what you want on the side)
st.sidebar.image('pngwing.com (6).png')

# markdown is for space
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.divider()
st.header('Project Data')
st.dataframe(data, use_container_width= True)

sel_cols = ['serum creatinine', 'hemoglobin', 'sodium', 'specific gravity', 'blood urea',
            'blood glucose random', 'albumin', 'classes']


serum = st.sidebar.number_input("serum creatinine", placeholder='insert a number...')
hemog = st.sidebar.number_input("hemoglobin", placeholder='insert a number...')
sodium = st.sidebar.number_input("sodium", placeholder='insert a number...')
spe_gra = st.sidebar.number_input("specific gravity", placeholder='insert a number...')
blood_urea = st.sidebar.number_input("blood urea", placeholder='insert a number...')
blood_glu = st.sidebar.number_input("blood glucose random", placeholder='insert a number...')
albumin = st.sidebar.number_input("albumin", placeholder='insert a number...')

#users input
input_var = pd.DataFrame()
input_var['serum creatinine'] = [serum]
input_var['hemoglobin'] = [hemog ]
input_var['sodium'] = [sodium]
input_var['specific gravity'] = [spe_gra]
input_var['blood urea'] = [blood_urea]
input_var['blood glucose random'] = [blood_glu]
input_var['albumin'] = [albumin]

st.markdown("<br>", unsafe_allow_html= True)
st.divider()
st.subheader('Users Inputs')
st.dataframe(input_var, use_container_width = True)

model = joblib.load('kidneydiseasepredictionmodel.pkl')
predict = model.predict(input_var)


if st.button('Check your Health Status'):
    if predict[0] == 0:
        st.error(f"Unfortunately, you have  chronic kidney disease. Please you need to see a doctor")
        st.image('pngwing.com (7).png', width = 300)
    else:
        st.success(f"Great!....You are fine, you do not have a chronic kidney disease")
        st.image('pngwing.com (8).png', width = 300)

        #Great!....You are fine, you do not have a chronic kidney disease

#Unfortunately, you have  chronic kidney disease. Please you need to see a doctor