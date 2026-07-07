import streamlit as st
from src.components.footer import footer_home


def home_screen():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        * { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        .stApp { background: #06090F !important; }

        #MainMenu, footer, header { visibility: hidden; }

        .block-container {
            padding-top: 2rem !important;
            max-width: 780px !important;
        }

        button[kind="primary"] {
            background: #4F46E5 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            border: none !important;
            transition: background 0.15s ease !important;
        }
        button[kind="primary"]:hover {
            background: #4338CA !important;
            box-shadow: 0 4px 12px rgba(79,70,229,0.35) !important;
        }
        button[kind="secondary"] {
            background: transparent !important;
            color: #64748B !important;
            border-radius: 8px !important;
            font-weight: 500 !important;
            font-size: 0.8rem !important;
            border: 1px solid #1E293B !important;
        }
        button[kind="secondary"]:hover {
            color: #E2E8F0 !important;
            border-color: #334155 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Grid + glow
    st.markdown("""
        <div style="
            position: fixed; inset: 0;
            background-image:
                linear-gradient(rgba(79,70,229,0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(79,70,229,0.05) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none; z-index: 0;
        "></div>
        <div style="
            position: fixed;
            width: 500px; height: 200px;
            background: radial-gradient(ellipse, rgba(79,70,229,0.15) 0%, transparent 70%);
            top: 0; left: 50%; transform: translateX(-50%);
            pointer-events: none; z-index: 0;
        "></div>
    """, unsafe_allow_html=True)

    # Logo + title
    st.markdown("""
        <div style="
            display: flex; flex-direction: column;
            align-items: center; justify-content: center;
            padding: 1.5rem 0 2rem 0; gap: 0.75rem;
            position: relative; z-index: 1;
        ">
            <div style="
                width: 64px; height: 64px; background: #4F46E5;
                border-radius: 18px;
                display: flex; align-items: center; justify-content: center;
                font-size: 2rem;
                box-shadow: 0 8px 24px rgba(79,70,229,0.35);
            ">🎓</div>
            <div style="text-align: center;">
                <p style="
                    font-family: 'Plus Jakarta Sans', sans-serif;
                    font-size: 2rem; font-weight: 800;
                    color: #F1F5F9; letter-spacing: -0.04em;
                    margin: 0; line-height: 1.1;
                ">AttendX</p>
                <p style="
                    font-family: 'Plus Jakarta Sans', sans-serif;
                    font-size: 0.72rem; font-weight: 500;
                    color: #475569; letter-spacing: 0.1em;
                    text-transform: uppercase; margin: 0.3rem 0 0 0;
                ">AI-Powered Attendance</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Portal cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="
                background: #0D1117; border-radius: 16px;
                padding: 1.75rem 1.25rem 1.25rem;
                border: 1px solid #1E293B; text-align: center;
                margin-bottom: 0.75rem; position: relative; z-index: 1;
            ">
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png"
                     style="height: 120px; margin-bottom: 1rem;" />
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:1.1rem;
                   font-weight:700; color:#E2E8F0; margin:0 0 0.25rem 0;">Student Portal</p>
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:0.72rem;
                   color:#475569; margin:0 0 1.25rem 0; font-weight:400;">
                   Log in with Face ID & track attendance</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button('Student Portal ↗', type='primary', key='student_btn', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="
                background: #0D1117; border-radius: 16px;
                padding: 1.75rem 1.25rem 1.25rem;
                border: 1px solid #1E293B; text-align: center;
                margin-bottom: 0.75rem; position: relative; z-index: 1;
            ">
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png"
                     style="height: 120px; margin-bottom: 1rem;" />
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:1.1rem;
                   font-weight:700; color:#E2E8F0; margin:0 0 0.25rem 0;">Teacher Portal</p>
                <p style="font-family:'Plus Jakarta Sans',sans-serif; font-size:0.72rem;
                   color:#475569; margin:0 0 1.25rem 0; font-weight:400;">
                   Manage subjects & take AI attendance</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button('Teacher Portal ↗', type='primary', key='teacher_btn', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    # About button
    st.markdown("<br>", unsafe_allow_html=True)
    col_center = st.columns([1, 2, 1])
    with col_center[1]:
        if st.button('About AttendX →', type='secondary', key='about_btn', use_container_width=True):
            st.session_state['show_about'] = True
            st.rerun()

    footer_home()
