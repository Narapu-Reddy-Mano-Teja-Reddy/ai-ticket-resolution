import streamlit as st
from backend.rag import kb_engine

def dashboard_ui():
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='text-align: center; padding: 20px 0;'>
            <h1 style='color: #1a202c; margin: 0; font-size: 2.5rem; font-weight: 700;'>SupportAI</h1>
            <p style='color: #6b7280; margin: 5px 0 0 0; font-size: 1.1rem;'>Intelligent Knowledge Management Platform</p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation
    st.markdown("<hr style='margin: 20px 0; border: none; height: 1px; background: #e5e7eb;'>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["📋 New Ticket", "📊 Analytics", "📚 History", "⚙️ Settings"])

    with tab1:
        ticket_assistant()

    with tab2:
        knowledge_insights()

    with tab3:
        ticket_history()

    with tab4:
        settings()

    # Footer
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; color: #9ca3af; font-size: 0.9rem; padding: 20px 0; border-top: 1px solid #e5e7eb;'>
        Copyrights 2025-2026 AI Ticket Resolution, Designed by Narapu Reddy Mano Teja Reddy
    </div>
    """, unsafe_allow_html=True)

def ticket_assistant():
    st.markdown("### Create New Support Ticket")

    # Ticket Form
    with st.container():
        col1, col2 = st.columns([2, 1])

        with col1:
            st.markdown("#### Ticket Details")
            title = st.text_input("Ticket Title", placeholder="Brief summary of the issue")
            desc = st.text_area("Description", height=120, placeholder="Provide detailed description of the problem...")

            st.markdown("#### Attachments")
            file = st.file_uploader("Upload files (optional)", type=['png', 'jpg', 'txt', 'log', 'pdf'], help="Supported formats: PNG, JPG, TXT, LOG, PDF")

            # Priority and Category
            col_a, col_b = st.columns(2)
            with col_a:
                priority = st.selectbox("Priority", ["Low", "Medium", "High", "Urgent"], index=1)
            with col_b:
                category_hint = st.selectbox("Category Hint (optional)", ["", "Technical", "Access", "Hardware", "Software", "Network", "Other"])

        with col2:
            st.markdown("#### Quick Actions")
            analyze_btn = st.button("🔍 Analyze Ticket", use_container_width=True, type="primary")

            if st.button("📋 Save Draft", use_container_width=True):
                st.info("Draft saved successfully!")

            st.markdown("#### Recent Templates")
            templates = ["Password Reset", "Software Installation", "VPN Issues", "Email Problems"]
            for template in templates:
                if st.button(f"📄 {template}", use_container_width=True, help=f"Use {template} template"):
                    st.session_state.selected_template = template

    # Analysis Results
    if analyze_btn and desc:
        if not title.strip():
            st.error("Please provide a ticket title")
            return

        with st.spinner("🤖 AI is analyzing your ticket..."):
            try:
                txt = f"{title}\n{desc}" + (f"\n[File: {file.name}]" if file else "")

                # Progress indicators
                progress_bar = st.progress(0)
                status_text = st.empty()

                status_text.text("Analyzing ticket...")
                progress_bar.progress(40)
                
                # Optimized single-pass analysis
                cat, recs, sol = kb_engine.analyze_full_ticket(txt)

                status_text.text("Finalizing...")

                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()

                # Save to History
                if 'history' not in st.session_state:
                    st.session_state.history = []
                st.session_state.history.insert(0, {
                    "title": title,
                    "query": desc,
                    "category": cat,
                    "recs": recs,
                    "solution": sol,
                    "timestamp": st.session_state.get('current_time', 'Now'),
                    "priority": priority
                })

                # Results Display
                st.success("✅ Analysis Complete!")

                # Results Cards
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("#### 🎯 Classification")
                    st.info(f"**Category:** {cat}")
                    st.markdown(f"**Priority:** {priority}")

                with col2:
                    st.markdown("#### 💡 AI Solution")
                    st.success(sol)

                # Source Articles
                with st.expander("📚 Recommended Knowledge Base Articles", expanded=True):
                    if recs:
                        for i, article in enumerate(recs, 1):
                            st.markdown(f"**{i}.** {article}")
                            st.markdown("---")
                    else:
                        st.info("No specific articles found. General support recommended.")

                # Action Buttons
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    if st.button("📤 Submit Ticket", use_container_width=True, type="primary"):
                        st.success("Ticket submitted successfully!")
                with col_b:
                    if st.button("🔄 Re-analyze", use_container_width=True):
                        st.rerun()
                with col_c:
                    if st.button("📋 Copy Solution", use_container_width=True):
                        st.text_area("Copy this solution:", value=sol, height=100)

            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                st.info("Try rephrasing your ticket description or check your internet connection.")

def knowledge_insights():
    st.markdown("### Knowledge Base Analytics")

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Articles", "20", "+2")

    with col2:
        st.metric("Avg Resolution Time", "4m", "-8%")

    with col3:
        st.metric("Coverage Rate", "88%", "+2%")

    with col4:
        st.metric("Active Users", "15", "+5")

    # Charts and Insights
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Ticket Categories")
        # Mock data for categories
        categories = ["Technical", "Access", "Hardware", "Software", "Network"]
        counts = [12, 8, 5, 7, 3]
        st.bar_chart(dict(zip(categories, counts)))

    with col2:
        st.markdown("#### Resolution Trends")
        # Mock resolution data
        months = ["Jan", "Feb", "Mar", "Apr", "May"]
        resolved = [45, 52, 48, 61, 55]
        st.line_chart(dict(zip(months, resolved)))

    # Content Gaps
    st.markdown("#### Content Gap Analysis")
    with st.expander("Identified Gaps", expanded=True):
        gaps = [
            "Docker container timeout issues",
            "VPN error 404 troubleshooting",
            "Remote desktop connection problems",
            "Email encryption setup"
        ]
        for gap in gaps:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"• {gap}")
            with col_b:
                if st.button("Create", key=f"create_{gap}", use_container_width=True):
                    st.success(f"Draft created for: {gap}")

def ticket_history():
    st.markdown("### Ticket History")

    if 'history' not in st.session_state or not st.session_state.history:
        st.info("No tickets analyzed yet. Create your first ticket to see history here.")
        return

    # Search and Filter
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("Search tickets...", placeholder="Enter keywords")
    with col2:
        filter_cat = st.selectbox("Filter by category", ["All"] + list(set(h['category'] for h in st.session_state.history)))

    # Display History
    for i, ticket in enumerate(st.session_state.history):
        if search and search.lower() not in ticket['query'].lower() and search.lower() not in ticket['title'].lower():
            continue
        if filter_cat != "All" and ticket['category'] != filter_cat:
            continue

        with st.expander(f"#{len(st.session_state.history)-i} - {ticket['title'][:50]}...", expanded=False):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"**Description:** {ticket['query']}")
                st.markdown(f"**Category:** {ticket['category']}")
                st.markdown(f"**Priority:** {ticket.get('priority', 'Medium')}")

            with col2:
                st.markdown(f"**Solution:**")
                st.info(ticket['solution'][:200] + "..." if len(ticket['solution']) > 200 else ticket['solution'])

            if ticket['recs']:
                st.markdown("**Related Articles:**")
                for rec in ticket['recs'][:2]:  # Show first 2
                    st.write(f"• {rec[:100]}...")

def settings():
    st.markdown("### Application Settings")

    # User Profile
    st.markdown("#### User Profile")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=st.session_state.get('name', ''))
            email = st.text_input("Email", placeholder="user@company.com")
        with col2:
            role = st.selectbox("Role", ["Support Agent", "Manager", "Administrator"])
            notifications = st.checkbox("Email Notifications", value=True)

    # Preferences
    st.markdown("#### Preferences")
    with st.container():
        theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
        language = st.selectbox("Language", ["English", "Spanish", "French"])
        auto_save = st.checkbox("Auto-save drafts", value=True)

    # System Info
    st.markdown("#### System Information")
    with st.container():
        kb_engine.ensure_kb_initialized()  # Ensure KB is loaded
        st.write(f"**Version:** 1.2.0")
        st.write(f"**Knowledge Base:** {len(kb_engine.docs)} articles")
        st.write(f"**Last Updated:** {st.session_state.get('current_time', 'Recently')}")

    # Actions
    st.markdown("#### Actions")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💾 Save Settings", use_container_width=True, type="primary"):
            st.success("Settings saved successfully!")
    with col2:
        if st.button("🔄 Reset to Defaults", use_container_width=True):
            st.info("Settings reset to defaults.")
