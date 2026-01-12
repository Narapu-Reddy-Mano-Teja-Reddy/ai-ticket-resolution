# SupportAI Platform - Deployment Guide

This guide provides comprehensive instructions for deploying the SupportAI Knowledge Management Platform to various hosting services. The application is built as a single Streamlit app with integrated backend logic for simplified deployment.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- GitHub account
- Public repository

### Local Development
```bash
# Clone the repository
git clone <your-repo-url>
cd ai-ticket-resolution

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

## 📋 Supported Platforms

### 1. Streamlit Cloud (Recommended - Free)

**Best for:** Quick deployment, automatic scaling, community support

#### Deployment Steps:
1. **Prepare Repository:**
   - Ensure `app.py` is in the root directory
   - Make repository public on GitHub
   - Update `requirements.txt` with all dependencies

2. **Deploy:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect GitHub account
   - Select repository: `your-username/ai-ticket-resolution`
   - Set main file: `app.py`
   - Click "Deploy"

3. **Configuration:**
   - No additional configuration needed
   - App auto-detects settings

4. **Access:**
   - URL: `https://your-app-name.streamlit.app`

**Free Tier Limits:**
- 1 app per account
- Community support
- Automatic HTTPS
- 100 hours/month compute

### 2. Railway (Full Control)

**Best for:** Custom domains, persistent data, advanced configuration

#### Deployment Steps:
1. **Sign Up:**
   - Visit [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create Project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure:**
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - **Root Directory:** `/` (leave default)
   - **Environment:** Python

4. **Environment Variables (Optional):**
   ```
   STREAMLIT_SERVER_HEADLESS=true
   STREAMLIT_SERVER_PORT=$PORT
   STREAMLIT_SERVER_ADDRESS=0.0.0.0
   ```

5. **Access:**
   - Railway provides `https://your-project.up.railway.app`

**Free Tier:**
- $5 credit (expires)
- PostgreSQL database available
- Custom domains
- Environment variables

### 3. Render (Reliable Hosting)

**Best for:** Consistent performance, free SSL, webhooks

#### Deployment Steps:
1. **Sign Up:**
   - Visit [render.com](https://render.com)
   - Connect GitHub

2. **Create Web Service:**
   - Click "New" → "Web Service"
   - Connect repository
   - Configure:
     - **Runtime:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

3. **Environment:**
   - Add environment variables if needed

4. **Deploy:**
   - Click "Create Web Service"

5. **Access:**
   - URL: `https://your-service.onrender.com`

**Free Tier:**
- 750 hours/month
- Free SSL certificate
- Static IP
- Auto-deploys from Git

### 4. Vercel (Modern Platform)

**Best for:** Global CDN, edge functions, fast deployments

#### Deployment Steps:
1. **Sign Up:**
   - Visit [vercel.com](https://vercel.com)
   - Connect GitHub

2. **Import Project:**
   - Click "New Project"
   - Import GitHub repository
   - Configure:
     - **Framework:** Other
     - **Root Directory:** `./`
     - **Build Command:** `pip install -r requirements.txt`
     - **Output Directory:** `./`

3. **Environment Variables:**
   ```
   PYTHON_VERSION=3.9
   STREAMLIT_SERVER_PORT=8501
   ```

4. **Deploy:**
   - Vercel auto-detects and deploys

5. **Access:**
   - Vercel provides global CDN URL

**Free Tier:**
- 100GB bandwidth
- Global CDN
- Automatic HTTPS
- Edge functions

### 5. Heroku (Legacy but Reliable)

**Best for:** Enterprise features, add-ons ecosystem

#### Deployment Steps:
1. **Install Heroku CLI:**
   ```bash
   # Install Heroku CLI
   npm install -g heroku
   heroku login
   ```

2. **Prepare App:**
   - Create `Procfile` in root:
     ```
     web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
     ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

4. **Access:**
   - `https://your-app-name.herokuapp.com`

**Free Tier:**
- 550 hours/month
- Add-ons available
- Custom domains
- Sleeps after inactivity

## 🔧 Configuration

### Environment Variables

Create a `.env` file for local development:

```env
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Application Settings
APP_TITLE="SupportAI Platform"
APP_ICON="🛠️"

# Optional: For future enhancements
DATABASE_URL=your_database_url
API_KEY=your_api_key
```

### File Structure Requirements

Ensure your repository has:
```
ai-ticket-resolution/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── frontend/
│   ├── dashboard.py       # Dashboard components
│   ├── auth.py           # Authentication
│   └── styles.py         # CSS styling
├── backend/
│   └── rag.py            # Knowledge base engine
├── data/
│   ├── knowledge_base.json
│   └── users.json
└── DEPLOYMENT.md
```

## 🚨 Troubleshooting

### Common Issues

1. **Port Binding:**
   - Use `$PORT` environment variable
   - Set `--server.address=0.0.0.0`

2. **Memory Issues:**
   - Free tiers have memory limits (~512MB)
   - Optimize imports and data loading

3. **File Upload Limits:**
   - Check platform file size limits
   - Consider cloud storage for large files

4. **Session State:**
   - Some platforms don't persist session state
   - Use database for persistent data

5. **Dependencies:**
   - Ensure all packages in `requirements.txt`
   - Pin versions for reproducibility

### Performance Optimization

- **Lazy Loading:** Load data only when needed
- **Caching:** Use `@st.cache_data` for expensive operations
- **Pagination:** For large datasets
- **CDN:** Use for static assets

## 📊 Platform Comparison

| Platform | Free Hours | Custom Domain | Database | Auto SSL | Global CDN |
|----------|------------|---------------|----------|----------|------------|
| Streamlit Cloud | 100/month | ❌ | ❌ | ✅ | ✅ |
| Railway | Credit-based | ✅ | ✅ | ✅ | ✅ |
| Render | 750/month | ✅ | ✅ | ✅ | ❌ |
| Vercel | Bandwidth-based | ✅ | ✅ | ✅ | ✅ |
| Heroku | 550/month | ✅ | ✅ | ✅ | ❌ |

## 🔒 Security Considerations

- **HTTPS:** All platforms provide free SSL
- **Environment Variables:** Never commit secrets
- **User Data:** Implement proper authentication
- **Rate Limiting:** Consider implementing for production
- **Updates:** Keep dependencies updated

## 📞 Support

- **Streamlit Cloud:** Community forum
- **Railway:** Discord community
- **Render:** Documentation & Discord
- **Vercel:** Extensive documentation
- **Heroku:** Knowledge base

## 🎯 Recommended Deployment

For most users, **Streamlit Cloud** is recommended for its simplicity and integration with Streamlit apps. For more control and features, choose **Railway** or **Render**.

---

**Last Updated:** January 2026
**Version:** 1.2.0