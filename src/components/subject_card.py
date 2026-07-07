import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="
            background: white;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 1.25rem 1.5rem 1rem 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        ">
            <h3 style="
                margin: 0 0 0.35rem 0;
                color: #0F172A;
                font-size: 1rem;
                font-weight: 700;
                font-family: 'Plus Jakarta Sans', sans-serif;
            ">{name}</h3>
            <p style="
                color: #64748B;
                margin: 0 0 0.85rem 0;
                font-size: 0.8rem;
                font-family: 'Plus Jakarta Sans', sans-serif;
            ">
                <span style="
                    background: #EEF2FF;
                    color: #4F46E5;
                    padding: 1px 8px;
                    border-radius: 4px;
                    font-weight: 600;
                    font-size: 0.72rem;
                ">{code}</span>
                <span style="color:#E2E8F0; margin:0 6px;">·</span>Section {section}
            </p>
    """

    if stats:
        html += '<div style="display:flex; gap:0.5rem; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += f"""
                <div style="
                    background: #F8FAFC;
                    border: 1px solid #E2E8F0;
                    padding: 3px 10px;
                    border-radius: 6px;
                    font-size: 0.75rem;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                    color: #64748B;
                ">{icon} <b style="color:#0F172A">{value}</b> {label}</div>
            """
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
