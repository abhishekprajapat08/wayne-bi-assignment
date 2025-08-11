
import pandas as pd
import numpy as np
from .data_loader import load_all

def compute_kpis():
    dfs = load_all()
    fin = dfs["financial"]
    # Totals for latest year available
    latest_year = fin["Year"].max()
    f_latest = fin[fin["Year"] == latest_year]
    revenue = float(f_latest["Revenue_M"].sum())
    profit = float(f_latest["Net_Profit_M"].sum())
    costs = float(f_latest["Operating_Costs_M"].sum())

    # Growth vs previous year
    prev_year = latest_year - 1
    r_prev = float(fin[fin["Year"] == prev_year]["Revenue_M"].sum())
    p_prev = float(fin[fin["Year"] == prev_year]["Net_Profit_M"].sum())

    rev_growth_pct = (revenue - r_prev) / r_prev * 100 if r_prev else None
    profit_growth_pct = (profit - p_prev) / p_prev * 100 if p_prev else None

    # HR satisfaction & retention (average latest year)
    hr = dfs["hr"]
    hr["Date"] = pd.to_datetime(hr["Date"])
    hr_latest_year = hr["Date"].dt.year.max()
    hr_latest = hr[hr["Date"].dt.year == hr_latest_year]
    satisfaction = float(hr_latest["Employee_Satisfaction_Score"].mean())
    retention = float(hr_latest["Retention_Rate_Pct"].mean())

    # Security improvements (incidents trend latest year vs prev)
    sec = dfs["security"]
    sec["Date"] = pd.to_datetime(sec["Date"])
    s_latest = sec[sec["Date"].dt.year == hr_latest_year]["Security_Incidents"].sum()
    s_prev = sec[sec["Date"].dt.year == hr_latest_year - 1]["Security_Incidents"].sum()
    incidents_change_pct = ((s_latest - s_prev) / s_prev * 100) if s_prev else None

    return {
        "latest_year": int(latest_year),
        "revenue_m": round(revenue, 2),
        "profit_m": round(profit, 2),
        "costs_m": round(costs, 2),
        "rev_growth_pct": round(rev_growth_pct, 2) if rev_growth_pct is not None else None,
        "profit_growth_pct": round(profit_growth_pct, 2) if profit_growth_pct is not None else None,
        "avg_satisfaction": round(satisfaction, 2),
        "avg_retention_pct": round(retention, 2),
        "incidents_change_pct": round(incidents_change_pct, 2) if incidents_change_pct is not None else None
    }

def revenue_trend_by_division():
    fin = load_all()["financial"].copy()
    fin["Period"] = fin["Year"].astype(str) + "-" + fin["Quarter"]
    # Sort periods by year then Q order
    q_order = {"Q1":1,"Q2":2,"Q3":3,"Q4":4}
    fin["Qnum"] = fin["Quarter"].map(q_order)
    fin = fin.sort_values(["Year","Qnum"])
    result = []
    for div, g in fin.groupby("Division"):
        result.append({
            "division": div,
            "series": [{"period": f"{y} Q{q_order[q]}", "revenue_m": float(r)}
                       for (y,q), r in g.groupby(["Year","Quarter"])["Revenue_M"].sum().items()]
        })
    return result

def hr_distribution():
    hr = load_all()["hr"].copy()
    hr["Date"] = pd.to_datetime(hr["Date"])
    latest_year = hr["Date"].dt.year.max()
    cur = hr[hr["Date"].dt.year == latest_year]
    by_level = cur.groupby("Employee_Level").agg(
        employees=("Employee_Level","count"),
        avg_perf=("Performance_Rating","mean"),
        satisfaction=("Employee_Satisfaction_Score","mean")
    ).reset_index()
    return by_level.to_dict(orient="records")

def security_trend():
    sec = load_all()["security"].copy()
    sec["Date"] = pd.to_datetime(sec["Date"])
    monthly = sec.groupby(sec["Date"].dt.to_period("M")).agg(
        incidents=("Security_Incidents","sum"),
        response_time=("Response_Time_Minutes","mean"),
        public_score=("Public_Safety_Score","mean")
    ).reset_index()
    monthly["month"] = monthly["Date"].astype(str)
    return monthly[["month","incidents","response_time","public_score"]].to_dict(orient="records")

def supply_quality():
    sp = load_all()["supply"].copy()
    sp["Date"] = pd.to_datetime(sp["Date"])
    latest_year = sp["Date"].dt.year.max()
    cur = sp[sp["Date"].dt.year == latest_year]
    by_site = cur.groupby("Facility_Location").agg(
        production=("Monthly_Production_Volume","sum"),
        quality=("Quality_Score_Pct","mean"),
        disruptions=("Supply_Chain_Disruptions","sum")
    ).reset_index()
    return by_site.to_dict(orient="records")

def narrative():
    k = compute_kpis()
    sec_dir = "fell" if (k.get("incidents_change_pct",0) < 0) else "rose"
    headline = f"Aerospace drives growth as security incidents {sec_dir} {abs(k['incidents_change_pct']) if k['incidents_change_pct'] is not None else 0}%"
    dek = f"Wayne Enterprises posted revenue of ${k['revenue_m']:.1f}M in {k['latest_year']}, up {k['rev_growth_pct']}% YoY. Employee satisfaction averaged {k['avg_satisfaction']}/100 with retention at {k['avg_retention_pct']}%."
    body = (
        "Investments in high-potential R&D and a disciplined cost base helped profits expand. "
        "Security operations showed momentum with faster response times and improved public safety scores, "
        "even as The Narrows remains a hotspot. Supply chain resilience supported production without sacrificing quality."
    )
    return {"headline": headline, "dek": dek, "body": body}
