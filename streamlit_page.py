import streamlit as st
from pathlib import Path
import tempfile
import os
from ultralytics import YOLO
import moviepy.editor as moviepy

# Page config and title
st.set_page_config(layout="wide")
st.title("Model Demonstration App")


# Create a temporary directory within the project directory
temp_dir = Path("temp_videos")
temp_dir.mkdir(parents=True, exist_ok=True)


# Initialize session state variables if they don't exist
if 'video_path' not in st.session_state:
    st.session_state['video_path'] = ""

if 'model' not in st.session_state:
    st.session_state['model'] = None


# Upload file section
uploaded_file = st.file_uploader("Upload a video...", type=["mp4", "mov", "avi", "asf", "m4v"])


# Prepare the model
if not st.session_state['model']:
    with st.spinner('Model preparation...'):
        # model weights for inference
        model_path = "best_yolov8s.pt"
        model = YOLO(model_path)
        st.session_state['model'] = model


# Upload the file and send it to the model
if uploaded_file is not None and not st.session_state['video_path']:
    with st.spinner('Extracting...'):
        # Upload a file
        tfile = tempfile.NamedTemporaryFile(delete=False, dir=temp_dir, suffix='.mp4')
        tfile.write(uploaded_file.read())
        video_path = tfile.name
        
        # loading video
        clip = moviepy.VideoFileClip(video_path)  
        video_path = video_path[:-4]+"_reduced"+video_path[-4:]
        
        # new clip with new fps 
        new_clip = clip.set_fps(10) 
        new_clip.write_videofile(video_path)

        tfile.close()

        # Process the file
        proc_filename = f"{os.path.split(video_path)[-1][:-4]}_processed"
        results = st.session_state['model'].predict(source=video_path, conf=0.3, save=True, project="temp_videos", name=proc_filename)
        clear_filename = os.path.split(video_path)[-1]

        output_path = f"temp_videos\\{proc_filename}\\{clear_filename[:-4]}.avi"

        # Convert to mp4 format so streamlit will show the vid
        clip = moviepy.VideoFileClip(output_path)
        clip.write_videofile(output_path.replace('avi', 'mp4'))

        # Set the output filepath to show (dataframe locations used)
        st.session_state["video_path"] = output_path.replace('avi', 'mp4')
        st.success('Sucessfully extracted!')



# Check if the video has been processed
if st.session_state['video_path']:
    st.header("Video")
    st.video(st.session_state['video_path'])