import { useEffect, useState } from 'react'
import MetricCard from '@/components/MetricCard'
import { RevenueChart, SecurityChart, SupplyChart } from '@/components/ChartCard'
import { API_BASE } from '@/components/api'

export default function Home(){
  const [kpis,setKpis]=useState(null)
  const [rev,setRev]=useState([])
  const [sec,setSec]=useState([])
  const [sup,setSup]=useState([])
  const [news,setNews]=useState(null)

  useEffect(()=>{
    fetch(`${API_BASE}/kpis`).then(r=>r.json()).then(setKpis)
    fetch(`${API_BASE}/charts/revenue`).then(r=>r.json()).then(setRev)
    fetch(`${API_BASE}/charts/security`).then(r=>r.json()).then(setSec)
    fetch(`${API_BASE}/charts/supply`).then(r=>r.json()).then(setSup)
    fetch(`${API_BASE}/narrative`).then(r=>r.json()).then(setNews)
  },[])

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto p-6 space-y-6">
        <header className="flex items-end justify-between">
          <div>
            <h1 className="text-3xl font-bold">Wayne Enterprises — Executive Dashboard</h1>
            <p className="text-gray-500">Proof-of-concept BI app (FastAPI + Next.js)</p>
          </div>
          <div className="text-sm text-gray-400">API: {process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000'}</div>
        </header>

        {kpis && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <MetricCard title={`Revenue ${kpis.latest_year}`} value={`$${kpis.revenue_m}M`} subtitle={`${kpis.rev_growth_pct}% YoY`} />
            <MetricCard title="Net Profit" value={`$${kpis.profit_m}M`} subtitle={`${kpis.profit_growth_pct}% YoY`} />
            <MetricCard title="Avg. Satisfaction" value={kpis.avg_satisfaction} subtitle="HR Score" />
            <MetricCard title="Security Incidents" value={`${kpis.incidents_change_pct}%`} subtitle="YoY change" />
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <RevenueChart data={rev} />
          <SecurityChart data={sec} />
          <SupplyChart data={sup} />
        </div>

        {news && (
          <article className="bg-white rounded-2xl shadow p-6">
            <div className="text-xs uppercase text-gray-400">Plain Facts</div>
            <h2 className="text-2xl font-extrabold tracking-tight">{news.headline}</h2>
            <p className="text-gray-600 mt-1">{news.dek}</p>
            <p className="mt-4 leading-7">{news.body}</p>
          </article>
        )}
      </div>
    </div>
  )
}
