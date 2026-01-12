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

# Apply Global Styles
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

# Custom CSS for better text visibility
st.markdown("""
<style>
/* Ensure all text is visible */
.stApp {
    color: #1a202c !important;
}

[data-testid="stSidebar"] {
    color: #1a202c !important;
}

.stTextInput label, .stTextArea label, .stSelectbox label {
    color: #374151 !important;
    font-weight: 600 !important;
}

.stMarkdown p, .stMarkdown span, .stMarkdown div {
    color: #1a202c !important;
}

/* Form labels */
label {
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Help text */
.stTextInput [data-testid="stCaptionContainer"] p,
.stTextArea [data-testid="stCaptionContainer"] p {
    color: #6b7280 !important;
}

/* Tab text */
.stTabs [data-baseweb="tab"] {
    color: #6b7280 !important;
}

.stTabs [data-baseweb="tab"][aria-selected="true"] {
    color: white !important;
}

/* Metric labels */
[data-testid="stMetricLabel"] {
    color: #6b7280 !important;
}

/* Expander text */
.streamlit-expanderHeader p {
    color: #374151 !important;
}

/* Button text */
.stButton button p {
    color: inherit !important;
}

/* Success/Error text */
.stSuccess p, .stError p, .stInfo p, .stWarning p {
    color: inherit !important;
}
</style>
""", unsafe_allow_html=True)

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
