# def test():
#     import streamlit as st
#     import pandas as pd
#     from datetime import datetime

#     # Define the questions and options
#     questions = [
#         "What is your favorite color?",
#         "What is your favorite animal?",
#         "What is your favorite food?",
#         "What is your favorite hobby?",
#         "What is your favorite season?"
#     ]

#     options = [
#         ["Red", "Blue", "Green", "Yellow"],
#         ["Cat", "Dog", "Bird", "Fish"],
#         ["Pizza", "Burger", "Pasta", "Salad"],
#         ["Reading", "Traveling", "Gaming", "Cooking"],
#         ["Spring", "Summer", "Fall", "Winter"]
#     ]

#     # Streamlit app title
#     st.title("Survey Form")

#     # Get the username
#     username = st.text_input("Enter your username:")

#     # Dictionary to store the responses
#     responses = {}

#     # Loop through the questions and display them with radio buttons
#     for i, question in enumerate(questions):
#         responses[question] = st.radio(question, options[i])

#     # Save the responses to a CSV file when the submit button is clicked
#     if st.button("Submit"):
#         df=pd.read_csv("responses.csv")
#         username_list=df["Username"].to_list()
#         if username in username_list:
#             st.error("Rsponse already exist 🚧")
#             pass                
#         else:       
#             if username:
#                 # Ensure no empty values
#                 if all(value for value in responses.values()):
#                     responses["Username"] = username
#                     responses["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                     df = pd.DataFrame([responses])
#                     # Save to CSV
#                     csv_file = "responses.csv"
                    
#                     try:
#                         existing_df = pd.read_csv(csv_file)
#                         df = pd.concat([existing_df, df], ignore_index=True)
#                     except FileNotFoundError:
#                         pass
                    
#                     df.to_csv(csv_file, index=False)
                    
#                     st.success("Responses saved successfully!")
#                 else:
#                     st.error("Please answer all the questions.")
#             else:
#                 st.error("Please enter your username before submitting.")

# test()
import streamlit as st

st.title("Video Upload and Display with Streamlit")

# Allow users to upload a video file
uploaded_video = st.file_uploader("Upload a video", type=["mp4", "mov", "avi", "mkv"])

if uploaded_video is not None:
    # Display the uploaded video
    st.video(uploaded_video)
else:
    st.write("Please upload a video file.")