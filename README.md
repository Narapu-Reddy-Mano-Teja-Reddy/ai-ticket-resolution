# SupportAI Knowledge Management Platform

An enterprise-grade AI-powered ticket resolution and knowledge management system built with Streamlit. This integrated application provides intelligent ticket analysis, knowledge base management, and comprehensive analytics for IT support teams.

## ✨ Features

### 🎫 Intelligent Ticket Resolution
- **AI-Powered Analysis**: Automatic ticket categorization using advanced NLP
- **Smart Solutions**: Context-aware solution generation from knowledge base
- **Fallback Search**: Robust keyword-based search when AI models unavailable
- **Real-time Processing**: Instant analysis and recommendations

### 📊 Analytics Dashboard
- **Performance Metrics**: Ticket resolution rates, response times, and trends
- **Knowledge Insights**: Content gap analysis and recommendation engine
- **Usage Analytics**: User activity and system performance monitoring
- **Interactive Charts**: Visual data representation with filtering capabilities

### 🔐 User Management
- **Secure Authentication**: JSON-based user management with password hashing
- **Role-Based Access**: Different permission levels for users and admins
- **Session Management**: Secure session handling with automatic timeouts
- **User Profiles**: Personalized dashboards and preferences

### 🧠 Knowledge Base Engine
- **Vector Search**: FAISS-powered semantic search (with fallback)
- **Dynamic Updates**: Real-time knowledge base expansion
- **Content Management**: Easy article addition and categorization
- **Quality Assurance**: Automated content validation and deduplication

### 🎨 Professional UI/UX
- **Modern Design**: Clean, responsive interface with professional styling
- **Dark/Light Themes**: User preference-based theming
- **Mobile Responsive**: Optimized for all device sizes
- **Accessibility**: WCAG-compliant design patterns

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd ai-ticket-resolution
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   ```

4. **Access the app:**
   - Open [http://localhost:8501](http://localhost:8501) in your browser

## 🏗️ Architecture

### Integrated Design
- **Single Process**: Monolithic Streamlit application for simplified deployment
- **Direct Integration**: Backend logic embedded in frontend for better performance
- **Fallback Mechanisms**: Graceful degradation when external services unavailable
- **Modular Components**: Clean separation of concerns with reusable modules

### Technology Stack
- **Frontend**: Streamlit with custom CSS and components
- **AI/ML**: LangChain, FAISS, sentence-transformers
- **Data Storage**: JSON-based storage (easily replaceable with databases)
- **Authentication**: Secure session-based auth with password hashing
- **Styling**: Professional CSS with Inter font and responsive design

## 📁 Project Structure

```
ai-ticket-resolution/
├── app.py                 # Main application entry point with routing
├── start.py              # Alternative launcher script
├── requirements.txt      # Python dependencies
├── DEPLOYMENT.md         # Comprehensive deployment guide
├── README.md            # This file
├── backend/
│   ├── __init__.py
│   └── rag.py           # Knowledge base engine with AI logic
├── frontend/
│   ├── dashboard.py     # Main dashboard with tabs and analytics
│   ├── auth.py          # Authentication pages and user management
│   └── styles.py        # Professional CSS styling
└── data/
    ├── knowledge_base.json  # IT support articles (20 articles)
    └── users.json          # User authentication data
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file for custom configuration:

```env
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Application Settings
APP_TITLE="SupportAI Platform"
APP_ICON="🛠️"
```

### Knowledge Base
The application includes a pre-populated knowledge base with 20 IT support articles covering:
- Hardware troubleshooting
- Software installation
- Network connectivity
- Security best practices
- System optimization
- User account management

## 📊 Usage Examples

### Ticket Analysis
1. Navigate to the "Ticket Assistant" tab
2. Enter ticket details (title, description, priority)
3. Click "Analyze Ticket"
4. Review AI-generated category and solution
5. Save or export the analysis

### Knowledge Management
1. Access "Knowledge Insights" tab
2. View analytics and content gaps
3. Add new articles to the knowledge base
4. Monitor search effectiveness

### User Management
1. Register new accounts or login
2. Access personalized dashboard
3. View ticket history and analytics
4. Update profile preferences

## 🚀 Deployment

The application is optimized for deployment to free hosting platforms. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

### Supported Platforms
- **Streamlit Cloud** (Recommended) - Native Streamlit hosting
- **Railway** - Full control with custom domains
- **Render** - Reliable hosting with auto-scaling
- **Vercel** - Global CDN with edge functions
- **Heroku** - Enterprise features and add-ons

### Quick Deploy to Streamlit Cloud
1. Push code to public GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect repository and deploy

## 🔍 Troubleshooting

### Common Issues
- **Port conflicts**: Use `--server.port` flag to specify port
- **Memory limits**: Free tiers have ~512MB limits
- **AI model loading**: Fallback to keyword search if Ollama unavailable
- **File permissions**: Ensure write access to data directory

### Performance Tips
- Use caching for expensive operations
- Optimize imports and data loading
- Implement pagination for large datasets
- Monitor memory usage in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- Vector search by [FAISS](https://github.com/facebookresearch/faiss)
- Embeddings from [sentence-transformers](https://www.sbert.net/)

---

**Version:** 1.2.0
**Last Updated:** January 2026
**Python Version:** 3.8+
