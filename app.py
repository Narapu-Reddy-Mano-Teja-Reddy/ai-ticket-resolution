import streamlit as st
from frontend.styles import apply_custom_styles
from frontend.auth import login_register_page
from frontend.dashboard import dashboard_ui
import time

# Page Config
st.set_page_config(
    page_title="SupportAI Platform",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Global Styles (Now centrally managed in styles.py)
apply_custom_styles()

# Initialize session state
def init_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'name' not in st.session_state:
        st.session_state.name = ""
    if 'user_role' not in st.session_state:
        st.session_state.user_role = "User"
    if 'current_time' not in st.session_state:
        st.session_state.current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'page' not in st.session_state:
        st.session_state.page = "dashboard"

init_session_state()

# Main routing logic
def main():
    # Check if user is logged in
    if not st.session_state.logged_in:
        # Show authentication page
        login_register_page()
    else:
        # Show main dashboard
        dashboard_ui()

if __name__ == "__main__":
    main()
