import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp { background: #06090F !important; }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp { background: #F8FAFC !important; }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        * { font-family: 'Plus Jakarta Sans', sans-serif !important; }

        #MainMenu, footer, header { visibility: hidden; }

        .block-container {
            padding-top: 1.5rem !important;
            max-width: 1100px !important;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #0F172A !important;
        }
        h1 { font-size: 1.75rem !important; font-weight: 800 !important; letter-spacing: -0.04em !important; }
        h2 { font-size: 1.3rem !important; font-weight: 700 !important; letter-spacing: -0.03em !important; }
        h3 { font-size: 1rem !important; font-weight: 600 !important; }

        p, label, span {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            color: #64748B !important;
        }

        /* ── Primary button ── */
        button[kind="primary"] {
            border-radius: 8px !important;
            background: #4F46E5 !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            font-size: 0.82rem !important;
            border: none !important;
            padding: 0.45rem 1rem !important;
            transition: background 0.15s, box-shadow 0.15s !important;
        }
        button[kind="primary"]:hover {
            background: #4338CA !important;
            box-shadow: 0 4px 12px rgba(79,70,229,0.25) !important;
            color: #FFFFFF !important;
        }

        /* ── Secondary button ── */
        button[kind="secondary"] {
            border-radius: 8px !important;
            background: white !important;
            color: #64748B !important;
            font-weight: 500 !important;
            font-size: 0.82rem !important;
            border: 1px solid #E2E8F0 !important;
            padding: 0.45rem 1rem !important;
            transition: background 0.15s, border-color 0.15s !important;
        }
        button[kind="secondary"]:hover {
            background: #F8FAFC !important;
            border-color: #CBD5E1 !important;
            color: #0F172A !important;
        }

        /* ── Tertiary button ── */
        button[kind="tertiary"] {
            border-radius: 8px !important;
            background: #FEF2F2 !important;
            color: #EF4444 !important;
            font-weight: 500 !important;
            font-size: 0.82rem !important;
            border: 1px solid #FECACA !important;
            padding: 0.45rem 1rem !important;
        }
        button[kind="tertiary"]:hover {
            background: #FEE2E2 !important;
        }

        /* ── Inputs — white ── */
        div[data-testid="stTextInput"] input {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 7px !important;
            color: #0F172A !important;
            font-size: 0.82rem !important;
            padding: 0.4rem 0.75rem !important;
            height: 36px !important;
        }
        div[data-testid="stTextInput"] input:focus {
            border-color: #4F46E5 !important;
            box-shadow: 0 0 0 3px rgba(79,70,229,0.12) !important;
        }
        div[data-testid="stTextInput"] input::placeholder {
            color: #CBD5E1 !important;
        }
        div[data-testid="stTextInput"] label {
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            color: #64748B !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
        }

        /* ── Selectbox ── */
        div[data-baseweb="select"] > div {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 7px !important;
            font-size: 0.82rem !important;
            color: #0F172A !important;
            min-height: 36px !important;
        }

        /* ── Divider ── */
        hr { border-color: #E2E8F0 !important; margin: 0.75rem 0 !important; }

        /* ── Dataframe ── */
        div[data-testid="stDataFrame"] {
            border-radius: 10px !important;
            border: 1px solid #E2E8F0 !important;
            overflow: hidden !important;
            background: white !important;
        }

        /* ── Alert ── */
        div[data-testid="stAlert"] {
            border-radius: 8px !important;
            font-size: 0.82rem !important;
        }

        /* ── Container border ── */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: white !important;
            border: 1px solid #E2E8F0 !important;
            border-radius: 12px !important;
        }

        /* ── Subheader color ── */
        div[data-testid="stHeading"] h2 {
            color: #0F172A !important;
        }

        </style>
    """, unsafe_allow_html=True)
