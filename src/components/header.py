import streamlit as st


def header_home():
    pass


def header_dashboard():
    st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 0.25rem 0;
        ">
            <div style="
                width: 34px; height: 34px;
                background: #4F46E5;
                border-radius: 9px;
                display: flex; align-items: center; justify-content: center;
                font-size: 1rem; flex-shrink: 0;
                box-shadow: 0 4px 12px rgba(79,70,229,0.2);
            ">🎓</div>
            <span style="
                font-family: 'Plus Jakarta Sans', sans-serif;
                font-size: 1.1rem;
                font-weight: 800;
                color: #0F172A;
                letter-spacing: -0.03em;
            ">AttendX</span>
        </div>
    """, unsafe_allow_html=True)
