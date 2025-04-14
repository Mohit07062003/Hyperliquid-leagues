
import streamlit as st
import uuid
import pandas as pd
from tinydb import Query
from db import leagues_table
from hyperliquid_utils import fetch_pnl

def create_league_ui():
    st.subheader("📌 Create a New League")

    with st.form("create_league_form"):
        league_name = st.text_input("League Name")
        description = st.text_area("Description")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        creator_wallet = st.text_input("Your Wallet Address")

        submitted = st.form_submit_button("Create League")

        if submitted:
            if not (league_name and description and creator_wallet):
                st.warning("Please fill in all fields.")
                return

            join_code = str(uuid.uuid4())[:8]
            league_data = {
                "name": league_name,
                "description": description,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "creator_wallet": creator_wallet,
                "join_code": join_code,
                "participants": [creator_wallet]
            }

            leagues_table.insert(league_data)
            st.success("🎉 League Created Successfully!")
            st.code(f"Join Code: {join_code}")

def join_league_ui():
    st.subheader("🔑 Join a League")

    with st.form("join_league_form"):
        join_code = st.text_input("Enter Join Code")
        wallet_address = st.text_input("Your Wallet Address")

        submitted = st.form_submit_button("Join League")

        if submitted:
            if not (join_code and wallet_address):
                st.warning("Please fill in all fields.")
                return

            League = Query()
            league = leagues_table.get(League.join_code == join_code)

            if league:
                if wallet_address in league["participants"]:
                    st.info("You're already in this league.")
                else:
                    league["participants"].append(wallet_address)
                    leagues_table.update({"participants": league["participants"]}, League.join_code == join_code)
                    st.success("🎉 Successfully joined the league!")
                    st.write(f"Welcome to **{league['name']}**")
            else:
                st.error("Invalid join code. League not found.")

def leaderboard_ui():
    st.subheader("🏆 League Leaderboard")

    league_code = st.text_input("Enter League Join Code")
    league = leagues_table.get(Query().join_code == league_code)

    if league:
        leaderboard = []
        for participant in league["participants"]:
            pnl = fetch_pnl(participant)
            leaderboard.append({"wallet": participant, "pnl": pnl if pnl is not None else 0})

        leaderboard = sorted(leaderboard, key=lambda x: x["pnl"], reverse=True)

        df = pd.DataFrame(leaderboard)
        st.write(df)
    else:
        st.error("Invalid League Code")

def creator_controls_ui():
    st.subheader("👑 League Creator Controls")

    league_code = st.text_input("Enter League Join Code")
    wallet_address = st.text_input("Your Wallet Address")

    league = leagues_table.get(Query().join_code == league_code)

    if league:
        if league["creator_wallet"] == wallet_address:
            st.write(f"Managing League: **{league['name']}**")

            st.write("Participants:")
            for p in league["participants"]:
                st.write(f"- {p}")

            kick_wallet = st.text_input("Enter Wallet to Kick")
            if kick_wallet and kick_wallet in league["participants"]:
                if st.button("Kick Participant"):
                    league["participants"].remove(kick_wallet)
                    leagues_table.update({"participants": league["participants"]}, Query().join_code == league_code)
                    st.success(f"💥 Kicked {kick_wallet} from the league.")

            if st.button("End League Early"):
                st.warning(f"⚠️ Ending the league {league['name']} early!")
                leagues_table.remove(Query().join_code == league_code)
                st.success(f"🏁 League {league['name']} ended successfully.")
        else:
            st.error("You are not the creator of this league.")
    else:
        st.error("Invalid League Code")
