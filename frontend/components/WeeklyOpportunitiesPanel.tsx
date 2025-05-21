import React from "react"
export default function WeeklyOpportunitiesPanel({ opportunities }) {
  if (!opportunities.length) return null
  return (
    <div className="opportunity-panel" style={{marginTop:16}}>
      <h3>Haftalık Potansiyel Fırsatlar</h3>
      <ul>
        {opportunities.map((o, i) => (
          <li key={i} title={o.detail}>
            <b>{o.coin}</b>: {o.opportunity}
          </li>
        ))}
      </ul>
    </div>
  )
}