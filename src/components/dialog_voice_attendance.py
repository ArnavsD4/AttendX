import streamlit as st
from src.database.config import supabase
import pandas as pd
from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime

@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):
    st.info("Voice attendance is currently unavailable. Please use Face Recognition attendance instead.")
    if st.button('Close', type='primary'):
        st.rerun()
