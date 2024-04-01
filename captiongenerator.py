import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

key=os.getenv("My_HuggingFaceHub_Key")


API_URL_Semantics = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
API_URL_Capgen = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {key}"}

def generate_semantics(file):
    response = requests.post(API_URL_Semantics  , headers=headers, data=file)
    return response.json()[0]["generated_text"]
def generate_caption(payload):
	response = requests.post(API_URL_Capgen, headers=headers, json=payload)
	return response.json()[0]["generated_text"]
style= """
        <style>
        .rectangular-box {
            padding: 20px;
            background-color: #bbbbbb;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.5); /* Adjust the values for your desired shadow effect */
        }
        </style>
    """         
                        

st.title("Social Media Image Captioning with Generative AI")
st.image("Social Media Image Captioning-Generative AI.png")
file=st.file_uploader("Upload an Image", type=["jpg","jpeg","png","jfif"])


if file:
    with st.spinner("uploading image"):
        
        semantics=generate_semantics(file)
        with st.form("user input"):
            col1,col2,col3,col4=st.columns(4)
            with col1:
                Instabutton=st.form_submit_button("Instagram")
            with col2:
                TwitterButton=st.form_submit_button("Twitter")
            with col3:
                LinkedInButton=st.form_submit_button("LinkedIn")
            with col4:
                FacebookButton=st.form_submit_button("Facebook")

        col1,col2=st.columns([2,3])
        with col1:
            st.image(file,use_column_width=True)
        with col2:
            

            
            

            if Instabutton:
                    
                with st.spinner("generating Captions"):
                    prompt_dict1={"inputs":f"Question:convert the following image semantics"
                                            f"'{semantics}' to an intagram caption for my post. Make sure to add hash tags and emojis"
                                            f"Answer: " }
                    InstaCaption=generate_caption(prompt_dict1)
                        
                    Instagram_Caption= InstaCaption.split("Answer: ")[1]
                    rectangular_box1 = f"<div class='rectangular-box'>{Instagram_Caption}</div>"
                    st.markdown(style,unsafe_allow_html=True,
                    )
                    st.markdown(
                        rectangular_box1,unsafe_allow_html=True,
                    )

            elif TwitterButton:
                with st.spinner("generating Captions"):
                    prompt_dict2={"inputs":f"Question:convert the following image semantics"
                                            f"'{semantics}' to an twitter caption for my post. Keep it different from instagram caption, add social value to it. Make sure to add hash tags and emojis"
                                            f"Answer: " }
                    TwitterCaption=generate_caption(prompt_dict2)
                    
                    
                    Twitter_Caption= TwitterCaption.split("Answer: ")[1]
                    rectangular_box2 = f"<div class='rectangular-box'>{Twitter_Caption}</div>"
                    st.markdown(style,unsafe_allow_html=True,
                    )
                    st.markdown(
                        rectangular_box2,unsafe_allow_html=True,
                    )

            elif LinkedInButton:
                with st.spinner("generating Captions"):
                    prompt_dict3={"inputs":f"Question:convert the following image semantics"
                                            f"'{semantics}' to an LinkedIn caption for my post. Keep it professional, add social value to it. Make sure to add proper hash tags and emojis"
                                            f"Answer: " }
                    LinkedInCaption=generate_caption(prompt_dict3)
                    
                        
                    LinkedIn_Caption= LinkedInCaption.split("Answer: ")[1]
                    rectangular_box3 = f"<div class='rectangular-box'>{LinkedIn_Caption}</div>"
                    st.markdown(style,unsafe_allow_html=True,
                    )
                    st.markdown(
                        rectangular_box3,unsafe_allow_html=True,
                    )

            elif FacebookButton:
                with st.spinner("generating Captions"):
                    prompt_dict4={"inputs":f"Question:convert the following image semantics"
                                            f"'{semantics}' to an Facebook post .Add social value to it. Make sure to add proper hash tags and emojis"
                                            f"Answer: " }
                    FacebookCaption=generate_caption(prompt_dict4)          
                    
                
                
            
                    Facebook_Caption= FacebookCaption.split("Answer: ")[1]
                    rectangular_box4 = f"<div class='rectangular-box'>{Facebook_Caption}</div>"
                    st.markdown(style,unsafe_allow_html=True,
                    )
                    st.markdown(
                        rectangular_box4,unsafe_allow_html=True,
                    )
            else:
                rectangular_box = f"<div class='rectangular-box'>Click on the above buttons to see caption related to specific platform</div>"
                st.markdown(style,unsafe_allow_html=True,
                    )
                st.markdown(rectangular_box,unsafe_allow_html=True)
                