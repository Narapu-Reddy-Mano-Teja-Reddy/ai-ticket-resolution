import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        /* Main Container & Background */
        .stApp {
            background: #f8fafc;
            font-family: 'Inter', sans-serif;
            color: #1a202c;
        }

        /* Header Styling */
        .stApp header {
            background: #ffffff;
            border-bottom: 1px solid #e5e7eb;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: #ffffff;
            border-radius: 8px;
            padding: 4px;
            border: 1px solid #e5e7eb;
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 6px;
            color: #6b7280;
            font-weight: 500;
            padding: 8px 16px;
            transition: all 0.2s;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background: #f3f4f6;
            color: #374151;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: #3b82f6;
            color: white;
            font-weight: 600;
        }

        /* Card/Container Styling */
        [data-testid="stVerticalBlockBorderWrapper"], .stContainer {
            background: #ffffff;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            padding: 24px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            margin: 8px 0;
            transition: box-shadow 0.2s;
        }

        [data-testid="stVerticalBlockBorderWrapper"]:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        /* Inputs (Text Area, Text Input) */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea, .stSelectbox>div>div>select {
            background: #ffffff;
            color: #1a202c;
            border-radius: 8px;
            padding: 12px 16px;
            border: 1px solid #d1d5db;
            transition: border-color 0.2s, box-shadow 0.2s;
            font-size: 14px;
        }

        .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus, .stSelectbox>div>div>select:focus {
            border-color: #3b82f6;
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
            outline: none;
        }

        /* Labels */
        .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
            color: #374151;
            font-weight: 600;
            font-size: 14px;
            margin-bottom: 8px;
        }

        /* Buttons */
        .stButton>button {
            background: #3b82f6;
            color: white;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            transition: all 0.2s;
            font-size: 14px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }

        .stButton>button:hover {
            background: #2563eb;
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }

        .stButton>button:active {
            transform: translateY(0);
        }

        /* Primary buttons */
        .stButton>button[data-testid="stBaseButton-primary"] {
            background: #3b82f6;
        }

        .stButton>button[data-testid="stBaseButton-primary"]:hover {
            background: #2563eb;
        }

        /* Headlines */
        h1, h2, h3, h4 {
            color: #1a202c;
            font-weight: 700;
            margin-bottom: 16px;
        }

        h1 {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 8px;
        }

        h2 {
            font-size: 1.8rem;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 8px;
            margin-top: 32px;
        }

        h3 {
            font-size: 1.4rem;
            color: #374151;
        }

        h4 {
            font-size: 1.2rem;
            color: #4b5563;
        }

        /* Metrics */
        [data-testid="stMetricValue"] {
            color: #1a202c;
            font-weight: 700;
            font-size: 2rem;
        }

        [data-testid="stMetricDelta"] {
            color: #059669;
            font-weight: 600;
        }

        [data-testid="stMetricDelta"][data-testid="stMetricDelta-negative"] {
            color: #dc2626;
        }

        /* Success/Error Messages */
        .stSuccess {
            background: #dcfce7;
            color: #166534;
            border: 1px solid #bbf7d0;
            border-radius: 8px;
            padding: 16px;
        }

        .stError {
            background: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
            border-radius: 8px;
            padding: 16px;
        }

        .stInfo {
            background: #eff6ff;
            color: #1e40af;
            border: 1px solid #bfdbfe;
            border-radius: 8px;
            padding: 16px;
        }

        .stWarning {
            background: #fffbeb;
            color: #92400e;
            border: 1px solid #fed7aa;
            border-radius: 8px;
            padding: 16px;
        }

        /* Expander */
        .streamlit-expanderHeader {
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 12px 16px;
            font-weight: 600;
            color: #374151;
        }

        .streamlit-expanderHeader:hover {
            background: #f3f4f6;
        }

        /* Progress Bar */
        .stProgress > div > div {
            background: #3b82f6;
        }

        /* File Uploader */
        .stFileUploader > div > div > div > div {
            border: 2px dashed #d1d5db;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            transition: border-color 0.2s;
        }

        .stFileUploader > div > div > div > div:hover {
            border-color: #3b82f6;
        }

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }

        /* Spinner */
        .stSpinner > div > div {
            border-color: #3b82f6;
        }

        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        /* Custom spacing */
        .element-container {
            margin-bottom: 16px;
        }

        /* Form styling */
        .stForm {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 24px;
        }

    </style>
    """, unsafe_allow_html=True)
