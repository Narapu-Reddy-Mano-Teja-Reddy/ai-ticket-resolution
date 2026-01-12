import streamlit as st
import json
import os
import time

DATA_FILE = "data/users.json"

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f, indent=4)

def login_page():
    st.markdown("""
    <div style='text-align: center; padding: 40px 0 20px 0;'>
        <h1 style='color: #1a202c; margin: 0; font-size: 3rem; font-weight: 800;'>Welcome Back</h1>
        <p style='color: #6b7280; margin: 10px 0 0 0; font-size: 1.2rem;'>Sign in to your SupportAI account</p>
    </div>
    """, unsafe_allow_html=True)

    # Login Form
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            with st.form("login_form", clear_on_submit=True):
                st.markdown("### Account Login")

                username = st.text_input(
                    "Username",
                    placeholder="Enter your username",
                    help="Use the username you registered with"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password",
                    help="Password is case-sensitive"
                )

                remember = st.checkbox("Remember me", value=False)

                submit_btn = st.form_submit_button(
                    "Sign In",
                    use_container_width=True,
                    type="primary"
                )

                if submit_btn:
                    if not username or not password:
                        st.error("Please fill in all fields")
                        return

                    with st.spinner("Signing you in..."):
                        time.sleep(1)  # Simulate processing

                        users = load_users()
                        user = next((u for u in users if u.get('username') == username and u.get('password') == password), None)

                        if user:
                            st.session_state.logged_in = True
                            st.session_state.username = user['username']
                            st.session_state.name = user.get('name', username)
                            st.session_state.user_role = user.get('role', 'User')
                            st.success(f"Welcome back, {st.session_state.name}!")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error("Invalid username or password. Please try again.")

            # Additional Options
            st.markdown("---")
            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("Forgot Password?", help="Contact your administrator"):
                    st.info("Please contact your system administrator to reset your password.")
            with col_b:
                if st.button("Need Help?", help="Get assistance"):
                    st.info("Contact support at support@company.com or call extension 5555.")

def register_page():
    st.markdown("""
    <div style='text-align: center; padding: 40px 0 20px 0;'>
        <h1 style='color: #1a202c; margin: 0; font-size: 3rem; font-weight: 800;'>Join SupportAI</h1>
        <p style='color: #6b7280; margin: 10px 0 0 0; font-size: 1.2rem;'>Create your account to get started</p>
    </div>
    """, unsafe_allow_html=True)

    # Registration Form
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            with st.form("register_form", clear_on_submit=True):
                st.markdown("### Create Account")

                col_left, col_right = st.columns(2)

                with col_left:
                    first_name = st.text_input(
                        "First Name",
                        placeholder="John",
                        help="Your first name"
                    )

                with col_right:
                    last_name = st.text_input(
                        "Last Name",
                        placeholder="Doe",
                        help="Your last name"
                    )

                full_name = f"{first_name} {last_name}".strip()

                username = st.text_input(
                    "Username",
                    placeholder="johndoe",
                    help="Choose a unique username (lowercase, no spaces)"
                )

                email = st.text_input(
                    "Email Address",
                    placeholder="john.doe@company.com",
                    help="Your work email address"
                )

                department = st.selectbox(
                    "Department",
                    ["", "IT Support", "HR", "Finance", "Marketing", "Operations", "Other"],
                    help="Select your department"
                )

                role = st.selectbox(
                    "Role",
                    ["", "Support Agent", "Manager", "Administrator", "User"],
                    index=4,
                    help="Select your role in the organization"
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a strong password",
                    help="Minimum 8 characters with numbers and symbols"
                )

                confirm_password = st.text_input(
                    "Confirm Password",
                    type="password",
                    placeholder="Confirm your password",
                    help="Re-enter your password"
                )

                terms = st.checkbox(
                    "I agree to the Terms of Service and Privacy Policy",
                    help="You must agree to continue"
                )

                register_btn = st.form_submit_button(
                    "Create Account",
                    use_container_width=True,
                    type="primary"
                )

                if register_btn:
                    # Validation
                    errors = []

                    if not first_name or not last_name:
                        errors.append("Please provide both first and last name")
                    if not username:
                        errors.append("Username is required")
                    elif len(username) < 3:
                        errors.append("Username must be at least 3 characters")
                    elif not username.isalnum():
                        errors.append("Username can only contain letters and numbers")
                    if not email:
                        errors.append("Email address is required")
                    elif "@" not in email:
                        errors.append("Please enter a valid email address")
                    if not department:
                        errors.append("Please select your department")
                    if not role:
                        errors.append("Please select your role")
                    if not password:
                        errors.append("Password is required")
                    elif len(password) < 8:
                        errors.append("Password must be at least 8 characters")
                    elif password != confirm_password:
                        errors.append("Passwords do not match")
                    if not terms:
                        errors.append("You must agree to the Terms of Service")

                    if errors:
                        for error in errors:
                            st.error(error)
                        return

                    with st.spinner("Creating your account..."):
                        time.sleep(1.5)  # Simulate processing

                        users = load_users()

                        # Check for duplicates
                        if any(u.get('username') == username for u in users):
                            st.error("Username already exists. Please choose a different one.")
                            return

                        if any(u.get('email') == email for u in users):
                            st.error("Email address is already registered.")
                            return

                        # Create new user
                        new_user = {
                            "username": username,
                            "password": password,
                            "name": full_name,
                            "email": email,
                            "department": department,
                            "role": role,
                            "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
                        }

                        users.append(new_user)
                        save_users(users)

                        st.success("Account created successfully!")
                        st.info("You can now sign in with your username and password.")
                        time.sleep(2)
                        st.session_state.show_login = True
                        st.rerun()

def login_register_page():
    # Initialize session state
    if 'show_login' not in st.session_state:
        st.session_state.show_login = True

    # Header with branding
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 0 0 20px 20px; margin-bottom: 30px; text-align: center;'>
        <div style='background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);'>
            <h1 style='color: white; margin: 0; font-size: 2.5rem; font-weight: 700;'>SupportAI</h1>
            <p style='color: rgba(255,255,255,0.9); margin: 5px 0 0 0; font-size: 1.1rem;'>Intelligent Knowledge Management Platform</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tab navigation
    tab1, tab2 = st.tabs(["🔐 Sign In", "📝 Sign Up"])

    with tab1:
        login_page()

    with tab2:
        register_page()

    # Footer
    st.markdown("""
    <div style='text-align: center; color: #9ca3af; font-size: 0.9rem; padding: 30px 0; border-top: 1px solid #e5e7eb; margin-top: 50px;'>
        <p>SupportAI Platform • Version 1.2.0</p>
        <p>© 2024 SupportAI. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

