import streamlit as st


def footer_home():
    st.markdown("""
        <div style="
            margin-top: 2rem;
            text-align: center;
            padding-top: 1.25rem;
            border-top: 1px solid #1E293B;
        ">
            <p style="
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 0.72rem;
                font-weight: 600;
                color: #1E293B;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin: 0;
            ">AttendX · AI-Powered Attendance System</p>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top: 2rem;
            text-align: center;
            padding-top: 1.25rem;
            border-top: 1px solid #E2E8F0;
        ">
            <p style="
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 0.72rem;
                font-weight: 600;
                color: #CBD5E1;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                margin: 0;
            ">AttendX · AI-Powered Attendance System</p>
        </div>
    """, unsafe_allow_html=True)
