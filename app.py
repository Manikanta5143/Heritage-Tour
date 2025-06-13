import streamlit as st
from gtts import gTTS
from PIL import Image
import os

# --- Configuration ---
image_files = ['image5.jpg', 'image6.jpg', 'image7.jpg']
narration_file='narration_texts.txt'
audio_folder = 'audio'

# --- Prepare Directories ---
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# --- Load Narrations ---
with open(narration_file, 'r', encoding='utf-8') as f:
    descriptions = [line.strip() for line in f.readlines() if line.strip()]

# --- Generate Audio Files if Needed ---
for idx, text in enumerate(descriptions):
    audio_path = f"{audio_folder}/narration_{idx}.mp3"
    if not os.path.exists(audio_path):
        tts = gTTS(text)
        tts.save(audio_path)

# --- Web Interface ---
st.set_page_config(page_title="Heritage Tour", layout="centered")
st.title("🏛️ AI-Powered Cultural Heritage Tour")

# Optional Background Sound (looped)
background_audio = "background.mp3"
if os.path.exists(background_audio):
    st.audio(background_audio, format='audio/mp3', start_time=0)

# Navigation
if 'index' not in st.session_state:
    st.session_state.index = 0

def go_previous():
    if st.session_state.index > 0:
        st.session_state.index -= 1

def go_next():
    if st.session_state.index < len(image_files) - 1:
        st.session_state.index += 1

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("⬅️ Previous", on_click=go_previous)
with col3:
    st.button("Next ➡️", on_click=go_next)

# Display current image and narration
idx = st.session_state.index
image_path = image_files[idx]
audio_path = f"{audio_folder}/narration_{idx}.mp3"
caption = descriptions[idx]

st.image(Image.open(image_path), use_column_width=True, caption=caption)
st.audio(audio_path)
