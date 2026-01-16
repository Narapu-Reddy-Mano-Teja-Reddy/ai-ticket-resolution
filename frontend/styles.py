import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --primary: #4f46e5;
            --primary-gradient: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            --bg-color: #f1f5f9;
            --text-main: #0f172a; /* Darker for better contrast */
            --text-secondary: #334155;
            --card-bg: #ffffff; /* Solid white for readability */
        }

        /* --------------------------------------
           Global & Background
           -------------------------------------- */
        .stApp {
            background-color: #f8fafc;
            /* Subtle background pattern that doesn't interfere with text */
            background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
            background-size: 20px 20px;
            font-family: 'Inter', sans-serif;
            color: var(--text-main);
        }

        /* Enforce high contrast for all general text */
        p, li, span, div {
            color: #0f172a !important; /* Slate-900 */
        }
        
        /* --------------------------------------
           Typography
           -------------------------------------- */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Outfit', sans-serif;
            color: #1e1b4b !important; /* Very dark indigo */
        }

        h1 {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
            padding-bottom: 0.2em; /* Prevent clip cut-off */
        }
        
        /* --------------------------------------
           Containers & Cards
           -------------------------------------- */
        /* Make containers solid and distinct */
        [data-testid="stVerticalBlockBorderWrapper"],
        .stContainer, 
        .stForm {
            background: #ffffff !important;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            padding: 2rem;
        }

        /* --------------------------------------
           Inputs & Controls
           -------------------------------------- */
        /* Force white background and dark text for all text inputs */
        .stTextInput input, .stTextArea textarea, .stSelectbox select, .stNumberInput input {
            color: #1e293b !important;
            background-color: #ffffff !important;
        }

        /* Target the specific heavy grouping divs Streamlit uses for inputs */
        .stTextInput>div>div>input, 
        .stTextArea>div>div>textarea,
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #1e293b !important;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
        }

        /* Fix Selectbox dropdown arrow and text */
        div[data-baseweb="select"] span {
            color: #1e293b !important;
        }
        
        /* Dropdown menu items */
        div[data-baseweb="popover"] div, div[data-baseweb="menu"] div {
            background-color: #ffffff !important;
            color: #1e293b !important;
        }

        /* File Uploader */
        .stFileUploader > div > div {
            background-color: #ffffff !important;
            border: 2px dashed #cbd5e1;
        }
        
        .stFileUploader small {
            color: #64748b !important;
        }

        /* Input Labels */
        .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
            color: #334155 !important;
            font-weight: 600 !important;
            font-size: 0.95rem;
        }

        /* --------------------------------------
           Buttons
           -------------------------------------- */
        /* Default/Secondary Buttons - Force White Background */
        .stButton > button {
            background-color: #ffffff !important;
            color: #1e293b !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 8px;
            padding: 0.6rem 1.25rem;
            font-weight: 600;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            transition: all 0.2s;
        }

        .stButton > button:hover {
            border-color: #6366f1 !important;
            color: #4338ca !important;
            background-color: #f8fafc !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Button Text Paragraphs */
        .stButton > button p {
            color: inherit !important;
        }

        /* Primary Buttons - Black Box */
        .stButton > button[data-testid="stBaseButton-primary"] {
            background: #000000 !important;
            color: #ffffff !important;
            border: 1px solid #000000 !important;
        }

        .stButton > button[data-testid="stBaseButton-primary"] p {
             color: #ffffff !important;
        }

        .stButton > button[data-testid="stBaseButton-primary"]:hover {
            opacity: 0.95;
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
            transform: translateY(-1px);
        }

        /* --------------------------------------
           Tabs
           -------------------------------------- */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #ffffff !important;
            border-radius: 12px;
            padding: 4px;
            border: 1px solid #e2e8f0;
            gap: 8px;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: transparent !important;
            border: none !important;
            color: #64748b !important;
            font-weight: 500;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #eff6ff !important;
            color: #4f46e5 !important;
            font-weight: 600;
            border-radius: 8px;
        }

        /* --------------------------------------
           Metrics
           -------------------------------------- */
        [data-testid="stMetric"] {
            background: #ffffff;
            padding: 16px;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        [data-testid="stMetricValue"] {
            color: #0f172a !important;
        }
        
        [data-testid="stMetricLabel"] {
            color: #64748b !important;
        }

        /* --------------------------------------
           Sidebars & Navigation
           -------------------------------------- */
        [data-testid="stSidebar"] {
            background-color: #f8fafc;
            border-right: 1px solid #e2e8f0;
        }
        
        [data-testid="stSidebar"] p, [data-testid="stSidebar"] span {
            color: #334155 !important;
        }

        /* Hide branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
    </style>
    """, unsafe_allow_html=True)
