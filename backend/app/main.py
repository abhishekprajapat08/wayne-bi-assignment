
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import analytics

app = FastAPI(title="Wayne BI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/kpis")
def kpis():
    return analytics.compute_kpis()

@app.get("/charts/revenue")
def revenue_chart():
    return analytics.revenue_trend_by_division()

@app.get("/charts/hr")
def hr_chart():
    return analytics.hr_distribution()

@app.get("/charts/security")
def sec_chart():
    return analytics.security_trend()

@app.get("/charts/supply")
def supply_chart():
    return analytics.supply_quality()

@app.get("/narrative")
def news_style_narrative():
    return analytics.narrative()
