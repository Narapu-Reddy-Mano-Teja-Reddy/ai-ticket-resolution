import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

        :root {
            --primary: #6366f1;
            --primary-gradient: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
            --secondary: #4f46e5;
            --bg-color: #f8fafc;
            --card-bg: rgba(255, 255, 255, 0.9);
            --text-main: #1e293b;
            --text-secondary: #64748b;
        }

        /* --------------------------------------
           Global & Background
           -------------------------------------- */
        .stApp {
            background: #f0f4f8;
            background-image: 
                radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
            background-size: 100% 100%;
            background-attachment: fixed;
            font-family: 'Outfit', sans-serif;
            color: var(--text-main);
        }
        
        /* Dark mode overrides if needed, but we'll force a specific look here for consistency */
        .stApp > header {
            background: rgba(255, 255, 255, 0.7) !important;
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        /* --------------------------------------
           Typography
           -------------------------------------- */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Outfit', sans-serif;
        }

        h1 {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800 !important;
            letter-spacing: -0.02em;
            text-shadow: 0 2px 10px rgba(99, 102, 241, 0.2);
        }

        /* --------------------------------------
           Containers & Cards (Glassmorphism)
           -------------------------------------- */
        [data-testid="stVerticalBlockBorderWrapper"],
        .stContainer, 
        .stForm {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 
                0 4px 6px -1px rgba(0, 0, 0, 0.05), 
                0 10px 15px -3px rgba(0, 0, 0, 0.05),
                inset 0 0 0 1px rgba(255, 255, 255, 0.5);
            padding: 2rem;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }

        /* --------------------------------------
           Inputs & Controls
           -------------------------------------- */
        .stTextInput>div>div>input, 
        .stTextArea>div>div>textarea, 
        .stSelectbox>div>div>select {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 12px 16px;
            font-size: 0.95rem;
            transition: all 0.2s;
            box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05);
        }

        .stTextInput>div>div>input:focus, 
        .stTextArea>div>div>textarea:focus, 
        .stSelectbox>div>div>select:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
            transform: scale(1.005);
        }

        /* --------------------------------------
           Buttons
           -------------------------------------- */
        .stButton>button {
            background: var(--primary-gradient);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            font-family: 'Outfit', sans-serif;
            letter-spacing: 0.02em;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
            text-transform: uppercase;
            font-size: 0.85rem;
        }

        .stButton>button:hover {
            transform: translateY(-2px) scale(1.02);
            box-shadow: 0 8px 16px rgba(99, 102, 241, 0.4);
        }

        .stButton>button:active {
            transform: translateY(0);
        }

        /* Secondary buttons (use a different style if we can target them, 
           default streamlit buttons are all similar class, relying on primary attribute) */

        /* --------------------------------------
           Tabs
           -------------------------------------- */
        .stTabs [data-baseweb="tab-list"] {
            background: rgba(255,255,255,0.6);
            backdrop-filter: blur(10px);
            padding: 8px;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.4);
            gap: 8px;
            margin-bottom: 24px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 10px;
            padding: 8px 20px;
            font-weight: 500;
            color: #64748b;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .stTabs [data-baseweb="tab"]:hover {
            color: var(--primary);
            background: rgba(99, 102, 241, 0.05);
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: white;
            color: var(--primary);
            font-weight: 600;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        /* --------------------------------------
           Metrics & Stats
           -------------------------------------- */
        [data-testid="stMetric"] {
            background: white;
            padding: 16px;
            border-radius: 12px;
            border: 1px solid #f1f5f9;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        
        [data-testid="stMetricValue"] {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            font-size: 2.2rem;
        }

        /* --------------------------------------
           Expanders
           -------------------------------------- */
        .streamlit-expanderHeader {
            background: white;
            border-radius: 10px;
            border: 1px solid #e2e8f0;
            color: #1e293b;
        }

        /* --------------------------------------
           Animations
           -------------------------------------- */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .element-container {
            animation: fadeIn 0.5s ease-out forwards;
        }

        /* --------------------------------------
           Custom Scrollbar
           -------------------------------------- */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        /* Hide branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
    </style>
    """, unsafe_allow_html=True)
