import React from "react"

export default function PotentialOpportunitiesPanel({ opportunities }) {
  if (!opportunities || !opportunities.length) return null
  return (
    <div className="opportunity-panel">
      <h3>Potansiyel Fırsatlar</h3>
      <ul>
        {opportunities.map((o, i) => (
          <li key={i} style={{marginBottom:10}}>
            <b>{o.coin}</b>: {o.sources.join(", ")} kaynaklarına göre
            <b> {o.expected_time}</b> içinde <b>{o.price_target} USDT</b> potansiyeli.
            <span style={{marginLeft:8, color:"#4a4"}}>
              [Skor: {(o.score*100).toFixed(0)}%]
            </span>
            <div style={{fontSize:13, color:"#666"}}>{o.rationale}</div>
            {o.success_rate !== undefined && (
              <div style={{fontSize:12, color:"#126"}}>
                Son 30 benzer tahminin başarı oranı: <b>{(o.success_rate*100).toFixed(1)}%</b>
              </div>
            )}
          </li>
        ))}
      </ul>
      <div style={{fontSize:12, color:"#888"}}>
        <i>
          Bu panelde algoritmanın en güçlü bulduğu fırsatlar özetlenir. Tüm kaynaklar algoritmanın içinde değerlendirilmiştir.
        </i>
      </div>
    </div>
  )
}