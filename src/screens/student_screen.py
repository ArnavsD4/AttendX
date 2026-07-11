import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {student_data['name']}")
        if st.button("Logout", type='secondary', key='logoutbtn'):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('＋ Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']
        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button(sub=sub, sid=sid):
            if st.button("🗑️ Unenroll", type='tertiary', width='stretch', key=f"unenroll_{sid}"):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f"Unenrolled from {sub['name']} successfully!")
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    # Back button — top left
    if st.button("← Back to Home", type='secondary', key='student_back'):
        st.session_state['login_type'] = None
        if 'show_reg' in st.session_state:
            del st.session_state['show_reg']
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    header_dashboard()
    st.markdown("<br>", unsafe_allow_html=True)
    st.header('Student Login', anchor=False)
    st.markdown("""
        <p style="font-family:'Plus Jakarta Sans',sans-serif;
           font-size:0.85rem; color:#64748B; margin-bottom:1.5rem;">
            Position your face in the camera to log in. New here? You'll be prompted to register.
        </p>
    """, unsafe_allow_html=True)

    # 1. Initialize registration state if not present
    if "show_reg" not in st.session_state:
        st.session_state.show_reg = False

    photo_source = st.camera_input("Position your face in the center")

    if photo_source and not st.session_state.show_reg:
        img = np.array(Image.open(photo_source))
        with st.spinner('AI is scanning your face...'):
            detected, all_ids, num_faces = predict_attendance(img)
            if num_faces == 0:
                st.warning('No face detected. Please try again with better lighting.')
            elif num_faces > 1:
                st.warning('Multiple faces detected. Please ensure only your face is visible.')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if int(s['student_id']) == int(student_id)), None)
                    
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f"Welcome back, {student['name']}!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        # Face was "detected" by ML model but doesn't exist in DB
                        st.info("Face not recognized in our system. Register below.")
                        st.session_state.show_reg = True
                        st.rerun()
                else:
                    # Model explicitly didn't recognize the face
                    st.info("Face not recognized. You may be a new student — register below.")
                    st.session_state.show_reg = True
                    st.rerun()

    # 2. Render registration UI based on the persistent session state
    if st.session_state.show_reg:
        st.divider()
        st.markdown("""
            <div style="font-family:'Plus Jakarta Sans',sans-serif;
                font-size:1rem; font-weight:700; color:#0F172A; margin-bottom:0.75rem;">
                Create your profile
            </div>
        """, unsafe_allow_html=True)
        
        new_name = st.text_input("Your full name", placeholder='e.g. Riya Sharma')
        
        if st.button('Create Account', type='primary'):
            if new_name and photo_source:
                with st.spinner('Creating your profile...'):
                    img = np.array(Image.open(photo_source))
                    encodings = get_face_embeddings(img)
                    if encodings:
                        face_emb = encodings[0].tolist()
                        response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=None)
                        if response_data:
                            train_classifier()
                            st.session_state.is_logged_in = True
                            st.session_state.user_role = 'student'
                            st.session_state.student_data = response_data[0]
                            
                            # Clean up the registration flag before moving to dashboard
                            del st.session_state.show_reg 
                            
                            st.toast(f"Profile created! Welcome, {new_name}!")
                            time.sleep(1)
                            st.rerun()
                    else:
                        st.error('Could not capture your face clearly. Please try again.')
            elif not new_name:
                st.warning('Please enter your name.')
            elif not photo_source:
                st.warning('Please provide a camera image first.')

    footer_dashboard()
