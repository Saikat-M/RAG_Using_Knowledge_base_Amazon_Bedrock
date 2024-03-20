import boto3
import datetime
import streamlit as st

file_name = ''
s3_client = boto3.client('s3', region_name='us-east-1')

def process_file(document):
    name = document.name.split('.')[0]
    extension = document.name.split('.')[1]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{name}_{timestamp}.{extension}"
    # st.write(file_name)
    return file_name

def upload_file(file_name, renamed_file_name):
    bucket_name = 'knowledgebasesource'
    try:
        # Upload file to an S3 object from the specified local path
        s3_client.upload_file(file_name, bucket_name, renamed_file_name)
        # st.markdown(f"Object '{file_name}' uploaded to bucket '{bucket_name}'")
        st.markdown(f"Successfully uploaded the file!!! 😃", unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"Error: {str(e)}")

document = st.file_uploader("Upload Document", type=["pdf"])

if document:
    with open(document.name, 'wb') as f:
            f.write(document.getbuffer())
            
    modifed_file_name = process_file(document)
    upload_file(document.name, modifed_file_name)


