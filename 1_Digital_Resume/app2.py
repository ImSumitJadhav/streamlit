import streamlit as st
import requests
from streamlit_lottie import st_lottie
import webbrowser
import pandas as pd

##############################################################################################################################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt5(course, institute, details):
    return {'Course': course, 'Institute': institute, 'Details': details}
##############################################################################################################################

# 1.to add gif
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding1 = load_lottieurl("https://lottie.host/a75942d5-bf23-4cc1-a6b1-dbd0749b605d/xCKJuDroS7.json")
lottie_coding2 = load_lottieurl("https://lottie.host/6008acfd-aacc-422e-95da-8526dd9fdd19/4TWvQSUWkO.json")
lottie_coding3 = load_lottieurl("https://lottie.host/bb488315-c54a-4efe-9e5b-4496410ce3c3/FeDusLCHyK.json")
lottie_coding4 = load_lottieurl("https://lottie.host/278504bd-a8e6-4aa1-9659-429473146744/FbR81V5ilh.json")
lottie_coding5 = load_lottieurl("https://lottie.host/b32e98c0-48d0-4ffc-a5b8-67242c02626a/uoM93XB6gw.json")
lottie_coding6 = load_lottieurl("https://lottie.host/9a26ec3b-ab24-4bf9-979f-ce96118972d7/nhNNEawQH7.json")


#2.Header 
left_column, right_column = st.columns(2)
with left_column:
    st.write('''# Sumit Jadhav ''')
    st.write('''# Jr. Data Scientist''')
    st.write("Email : ","imsumitjadhav9696@gmail.com")
    st.write("Contact No : ","9325766962")
with right_column:
    st_lottie(lottie_coding1,height=200,key="tech")

# Define the links
links = {
    "LinkedIn": "https://www.linkedin.com/in/sumitjadhav9696/",
    "GitHub": "https://github.com/ImSumitJadhav",
    "Medium": "https://medium.com/@sj47452",
    "E-mail" : "imsumitjadhav9696@gmail.com",
    "Contact No." : "9325766962"
}

# Display buttons in a single line
button_col1, button_col2, button_col3,button_col4,button_col5 = st.columns(5)
with button_col1:
    if st.button('LinkedIn'):
        webbrowser.open_new_tab(links["LinkedIn"])
with button_col2:
    if st.button('GitHub'):
        webbrowser.open_new_tab(links["GitHub"])
with button_col3:
    if st.button('Medium'):
        webbrowser.open_new_tab(links["Medium"])
   
st.text("---------------------------------------------------------------------------------------------------------")

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
As a Data Scientist, I have a total experience of  around 2 years. I am familiar with cleaning, mining and organising data for use by technical and non-technical personnel. Advanced understanding of statistical, algebraic, and other analytical techniques. Highly organised, motivated, and diligent in Machine Learning and Deep Learning. As well as adopt new technology like generative AI, LLM, PLM, computer vision and DevOps. Highly motivated engineering graduate seeking challenging opportunities in IT and technical fields.
''')

st_lottie(lottie_coding2,height=220,width=700,key="we")

#####################
st.markdown('''
## Work Experience
''')

txt('**Jr. Data Scientist** , Techstawarts, Mumbai.',
'Aug 2023 - Ongoing')
st.info('''
- Working on project "Jarvis" which is available for markets like Australia and Saudi Arabia. This project related to stock market analysis and stock suggestion project. With the help of various indicators, data analysis techniques and machine learning algorithms we suggest stock calls like buy, sell or hold. 
- I working on data analysis for the past 10 years of data. As well as analysis of machine learning algorithms according to calls. Also working on stage 2 of this project, so mostly working on NER generation, news sentiment analysis and getting summaries related to stock from news using different open-source LLMs like Bart.
- Also working on other demo projects like Face, Age and Gender detection for billing counters for malls, 3D object detection with LiDAR dataset, building a question-answering chatbot with LLM, and model building for insurance dataset to predict frequency and severity.
- Learn new tech stacks like deployment with Amazon Web Services(AWS) and MLFlow, data generation with web scrapping, the building user interface for ML model with Flask, Fast API, Gradio and Streamlit, working with generative AI like Gemini, Bard and other open source LLM includes train and build our own trained LLM.
''')

txt('**Trainee Engineer** , Meticulous, Pune.',
'July 2021-July 2022')
st.info('''
- I working as a trainee engineer for 1 year. My primary work on excel to the analysis of data to get more improvement of the company based on material handling cost-cutting and prioritising products according to importance. Make dashboards with MS Excel, Tableau and Power BI. 
- As well as working on programming and research and development department. Research of new product and build demo piece, calculate time for it, how much cost should be required for product and manpower.
''')

st_lottie(lottie_coding3,height=220,width=700,key="intern")

#####################
st.markdown('''
## Internship
''')

txt('**Data Scientist Intern**, BSG.',
'December 2022')
st.info('''
- Data Science Virtual Internship. I used Python for visualization, model building and predicting the output. I have developed predictive models utilizing machine learning algorithms to identify potential customer segments and potential customer conversions enabling the team to improve their targeting with 15% accuracy. 
''')

txt('**Data Analyst Intern**, Accenture.',
'February 2023')
st.info('''
- Data analytics and visualization virtual internship. I used Python to analyze datasets and programmatically generate reports on machine learning algorithms. Working in Excel and Python to analyze data and find required insights. Using Matplotlib, Seaborn and Plotly to plot some graphs
''')

txt('**Projects**, Almabetter Institute, Bangalore',
'Feb 2022 - Feb 2023')
st.info('''
- Analysis Projects: I use Seaborn, Matplotlib and Plotly as well as Pandas and Numpy Python libraries. With the help of that plot some graphs and find insights. Analysis projects done by Python, Tableau and Power BI desktop. 
- Example, 1)EDA on Play Store data  2)EDA on telecom churn  3)Analysis on road accidents 4)Analysis of IPL  5)HR yearly analysis   6) Covid-19 analysis. 
- Machine Learning Projects: Build 3 types of Machine Learning projects: Regression, Classification and Natural Language Processing.
- Example:  1) Bike Sharing Demand Prediction: The regression type of the project and Behaviour data were found to be non-linear so I used RandomForestRegressor. 2)Mobile Price Range Prediction: A machine-learning Classification project. For classification used XGBoost a n d SVM algorithms. 3)Netflix Movies and TV Shows Clustering and Recommendation System:  The conclusion is, to form 18 clusters and build a recommendation system which recommends 5 Movies or TV Shows with the help of tags associated with them.    
''')

# st_lottie(lottie_coding4,height=220,width=700,key="edu")

#####################
st.markdown('''
## Education
''')

# Define your data
data = [
    txt5('Bachelor of Engineering', 'University of Mumbai', '2020, 7.7 CGPA'),
    txt5('Data Science', 'Almabetter Institute', '2023'),
    txt5('HSC', 'L.K.Jr.College,Palus', '2016 , 70%'),
    txt5('SSC', 'Janata Vidyalaya, Angawali', '2014 , 90%')

]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame as a table using Streamlit
st.write(df)


st_lottie(lottie_coding5,height=220,width=700,key="sk")

#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `SQL`, `HTML`')
txt3('Data processing frameworks', '`MySQL`, `Postgresql`, `pandas`, `numpy`, `Advance Excel`')
txt3('Data processing', '`Data Visualization`, `Data Analytics`, `Data Cleaning`, ` Data pre-processing`, `Data Preparation`,`Data Wrangling`, ` Data Generation`, ` Data Scrapping`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
txt3('Data visualization tools', '`Power BI`, `Tableau`')
txt3('Machine Learning and Deep Learning', '`scikit-learn`, `Natural Language Processing`,`Computer vision`, `Object Detection`')
txt3('Web development', '`Flask`, `HTML`, `Fast API`')
txt3('UI tools', '`streamlit`, `gradio`, `Falsk`, ` Fast API`, `tikinter`')
txt3('Model deployment', '`MLOps`, `MLFlow`, `AWS EC2 Instance`, `AWS Sagemaker`, `AWS`')
txt3('Generative AI', '`LLM`, `PLM`, `LLM training`, `Prompt Engineering.`')

st.markdown('''
## Achivements
''')

st.markdown('''
- [Gold badge in SQL on Hackerrank](https://www.hackerrank.com/sj47452)
- [Gold badge in Python on Hackerrank](https://www.hackerrank.com/sj47452)
- [Article on Machine Learning end-to-end on Medium](https://medium.com/@sj47452)
- [Article on Data Visualization Basic to Advanced on Medium](https://medium.com/@sj47452)
- [Article on PGAdmin4 and psql on Medium](https://medium.com/@sj47452)
''')

st.markdown('''
## Certification
''')

# List of image URLs
image_urls = [
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\0.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\1.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\2.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\3.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\4.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\5.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\6.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\7.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\8.jpg",
    r"C:\Users\Admin\Desktop\Personal Work\Streamlit\CER\9.jpg"
    # Add more image URLs as needed
]

# Number of images per row
images_per_row = 3

# Calculate number of rows
num_rows = len(image_urls) // images_per_row
if len(image_urls) % images_per_row != 0:
    num_rows += 1

# Display images in a grid
for i in range(num_rows):
    cols = st.columns(images_per_row)
    for j in range(images_per_row):
        index = i * images_per_row + j
        if index < len(image_urls):
            cols[j].image(image_urls[index], use_column_width=True, caption=f"Image {index+1}")



st_lottie(lottie_coding6,height=150,width=700,key="ty")

st.sidebar.write("Sumit Jadhav")
st.sidebar.image('my_pic.png', width=170)

st.sidebar.write("#Content")
st.sidebar.write("1.Contact Details")
st.sidebar.write("2.Summary")
st.sidebar.write("3.Work Experience")
st.sidebar.write("4.Internship")
st.sidebar.write("5.Education")
st.sidebar.write("6.Skills")
st.sidebar.write("7.Achivements")
st.sidebar.write("8.Certification")



