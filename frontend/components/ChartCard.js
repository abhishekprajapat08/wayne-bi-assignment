import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar, CartesianGrid, Legend } from 'recharts';

export function RevenueChart({ data }){
  return (
    <div className="bg-white rounded-2xl shadow p-5 h-80">
      <div className="font-semibold mb-2">Revenue by Division</div>
      <ResponsiveContainer width="100%" height="100%">
        <LineChart>
          <XAxis dataKey="period" type="category" allowDuplicatedCategory={false} />
          <YAxis />
          <Tooltip />
          {data.map((d,i)=>(
            <Line key={i} dataKey="revenue_m" name={d.division} data={d.series} dot={false} />
          ))}
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}

export function SecurityChart({ data }){
  return (
    <div className="bg-white rounded-2xl shadow p-5 h-80">
      <div className="font-semibold mb-2">Security Incidents & Response</div>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="incidents" name="Incidents" />
          <Bar dataKey="response_time" name="Avg Response (min)" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}

export function SupplyChart({ data }){
  return (
    <div className="bg-white rounded-2xl shadow p-5 h-80">
      <div className="font-semibold mb-2">Supply: Production vs Quality</div>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Facility_Location" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="production" name="Production" />
          <Bar dataKey="quality" name="Quality %" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
