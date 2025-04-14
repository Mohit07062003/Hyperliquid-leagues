

import streamlit as st
from leagues import create_league_ui, join_league_ui, leaderboard_ui, creator_controls_ui
from style import apply_custom_css

# Page config (must be first)
st.set_page_config(
    page_title="Hyperliquid Trading Leagues",
    page_icon="🌊",
    layout="wide"
)

apply_custom_css()

# Header
st.markdown("<h1>Hyperliquid Trading Platform</h1>", unsafe_allow_html=True)
st.image("image.png", width=100)

# Custom horizontal nav (using selectbox for better layout)
page = st.selectbox(
    "",
    ["🏠 Home", "📌 Create League", "🔑 Join League", "🏆 Leaderboard", "👑 Creator Controls"],
    key="nav",
    index=0
)

# Main content
if page == "🏠 Home":
    st.subheader("Welcome to the Hyperliquid Trading League Platform!")
    st.markdown("""
        Create and join competitive trading leagues powered by Hyperliquid.  
        📈 Track your PnL, 🧑‍🤝‍🧑 compete with friends, and 🥇 climb the leaderboard.
    """)
    st.success("Choose an option from the top menu to get started.")
elif page == "📌 Create League":
    create_league_ui()
elif page == "🔑 Join League":
    join_league_ui()
elif page == "🏆 Leaderboard":
    leaderboard_ui()
elif page == "👑 Creator Controls":
    creator_controls_ui()