# Wayne BI Fullstack Dashboard

A modern Business Intelligence dashboard for Wayne Enterprises built with FastAPI (backend) and Next.js (frontend).

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 16+
- npm or yarn

### Backend Setup (FastAPI)

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the backend server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

6. **Verify backend is running:**
   - API will be available at: http://localhost:8000
   - API documentation at: http://localhost:8000/docs
   - Health check at: http://localhost:8000/health

### Frontend Setup (Next.js)

1. **Open a new terminal and navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Create environment file (optional):**
   ```bash
   echo "NEXT_PUBLIC_API_BASE=http://localhost:8000" > .env.local
   ```

4. **Run the frontend development server:**
   ```bash
   npm run dev
   ```

5. **Open the application:**
   - Dashboard will be available at: http://localhost:3000

## 📊 Features

### Backend API Endpoints
- `GET /health` - Health check
- `GET /kpis` - Key Performance Indicators
- `GET /charts/revenue` - Revenue trends by division
- `GET /charts/hr` - HR distribution data
- `GET /charts/security` - Security incidents and response times
- `GET /charts/supply` - Supply chain quality metrics
- `GET /narrative` - AI-generated business narrative

### Frontend Components
- **Metric Cards** - Display key KPIs
- **Revenue Chart** - Line chart showing revenue trends
- **Security Chart** - Bar chart of security incidents
- **Supply Chart** - Production vs quality metrics
- **Narrative Section** - Business insights summary

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Pandas** - Data manipulation and analysis
- **Uvicorn** - ASGI server

### Frontend
- **Next.js 14** - React framework
- **Tailwind CSS** - Utility-first CSS framework
- **Recharts** - Charting library
- **React 18** - UI library

## 📁 Project Structure

```
wayne_bi_fullstack/
├── backend/
│   ├── app/
│   │   ├── analytics.py      # Business logic and data processing
│   │   ├── data/             # CSV data files
│   │   ├── data_loader.py    # Data loading utilities
│   │   └── main.py          # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Backend-specific instructions
├── frontend/
│   ├── components/          # React components
│   ├── pages/              # Next.js pages
│   ├── styles/             # CSS files
│   ├── package.json        # Node.js dependencies
│   └── README.md          # Frontend-specific instructions
└── README.md              # This file
```

## 🔧 Development

### Backend Development
- The backend uses hot reloading with `--reload` flag
- API documentation is auto-generated at `/docs`
- Data is stored in CSV files in `backend/app/data/`

### Frontend Development
- Next.js provides hot reloading by default
- Tailwind CSS is configured for utility classes
- Charts are built with Recharts library

## 🐛 Troubleshooting

### Common Issues

1. **Backend won't start:**
   - Ensure virtual environment is activated
   - Check if port 8000 is available
   - Verify all dependencies are installed

2. **Frontend can't connect to backend:**
   - Ensure backend is running on port 8000
   - Check CORS settings in backend
   - Verify `NEXT_PUBLIC_API_BASE` environment variable

3. **Module resolution errors:**
   - The `@` path alias is configured in `jsconfig.json`
   - Ensure you're using the correct import paths

4. **Data loading errors:**
   - Verify CSV files exist in `backend/app/data/`
   - Check column names match the expected format

## 📈 Data Sources

The application uses sample data from Wayne Enterprises divisions:
- **Financial Data** - Revenue, profit, costs by division
- **HR Data** - Employee satisfaction, retention, performance
- **Security Data** - Incidents, response times, safety scores
- **Supply Chain Data** - Production volumes, quality metrics
- **R&D Data** - Research projects, budgets, timelines

## 🚀 Deployment

### Backend Deployment
- Can be deployed to any platform supporting Python/FastAPI
- Consider using Gunicorn for production
- Set up proper CORS configuration for production

### Frontend Deployment
- Can be deployed to Vercel, Netlify, or any static hosting
- Build with `npm run build`
- Set environment variables for API endpoints

## 📝 License

This is a demonstration project for Wayne Enterprises BI dashboard.
