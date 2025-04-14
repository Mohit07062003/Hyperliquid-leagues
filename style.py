
import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Global Theme */
        html, body, [class*="css"] {
            background-color: #081c1a !important;
            color: #E6FFF6 !important;
            font-family: 'Segoe UI', sans-serif;
        }

        h1, h2, h3 {
            color: #6EF3C5;
            text-align: center;
        }

        .stButton>button, .stRadio>div {
            background-color: #0f3e36 !important;
            color: white !important;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            font-weight: 500;
        }

        /* Navigation bar radio buttons */
        .custom-radio {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 30px;
        }

        .custom-radio label {
            background-color: #0f3e36;
            color: #E6FFF6;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }

        .custom-radio input:checked + label {
            background-color: #6EF3C5;
            color: #0f3e36;
            font-weight: bold;
        }

        .stAlert {
            background-color: #0f3e36 !important;
            color: #6EF3C5 !important;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

