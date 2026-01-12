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
        .stTextInput>div>div>input, 
        .stTextArea>div>div>textarea, 
        .stSelectbox>div>div>select {
            background-color: #ffffff !important;
            color: #0f172a !important; /* Dark text in inputs */
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-weight: 500;
        }

        /* Input Labels */
        .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
            color: #334155 !important; /* Slate-700 */
            font-weight: 600 !important;
            font-size: 0.95rem;
        }

        /* --------------------------------------
           Buttons
           -------------------------------------- */
        /* Primary Keys */
        .stButton>button {
            border: 1px solid #e2e8f0;
            background-color: #ffffff;
            color: #1e293b !important; /* Dark slate for secondary buttons */
            border-radius: 8px;
            padding: 0.6rem 1.25rem;
            font-weight: 600;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
            transition: all 0.2s;
        }

        .stButton>button:hover {
            border-color: #cbd5e1;
            background-color: #f8fafc;
            color: #0f172a !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        /* Specifically target Primary Buttons to keep them distinct */
        .stButton>button[data-testid="stBaseButton-primary"] {
            background: var(--primary-gradient);
            color: #ffffff !important;
            border: none;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        }

        .stButton>button[data-testid="stBaseButton-primary"]:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
        }
        
        /* Button text specific override */
        .stButton>button p {
            font-weight: 600;
        }

        /* --------------------------------------
           Helper Text & Captions
           -------------------------------------- */
        .stCaption, [data-testid="stCaptionContainer"], .stMarkdown small {
            color: #475569 !important; /* Slate-600 - much darker than before */
            font-size: 0.9rem;
        }

        /* --------------------------------------
           Tabs
           -------------------------------------- */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #ffffff;
            border-bottom: 2px solid #e2e8f0;
            padding: 0;
            gap: 20px;
            margin-bottom: 24px;
            border-radius: 0;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: transparent;
            border: none;
            color: #64748b !important;
            font-weight: 600;
            padding-bottom: 12px;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            color: #4f46e5 !important;
            border-bottom: 3px solid #4f46e5;
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
