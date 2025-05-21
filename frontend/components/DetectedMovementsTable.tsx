import React from "react"

export default function DetectedMovementsTable({ movements }) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Coin</th>
          <th>Hareket Tipi</th>
          <th>Kaynaklar</th>
          <th>Skor</th>
          <th>Maks. Potansiyel Fiyat</th>
          <th>Beklenen Zaman</th>
          <th>Açıklama</th>
          <th>Başarı Oranı</th>
        </tr>
      </thead>
      <tbody>
        {movements.map((m, i) => {
          // Kısa gösterim ve detaylı tooltip metni hazırla
          const shortSummary = m.sources.map(s => s.type).join(", ");
          const fullDetailText = m.sources
            .map(s => `${s.type}${s.detail ? `: ${s.detail}` : ""}`)
            .join(" | ");
          return (
            <tr key={i}>
              <td>{m.coin}</td>
              <td>{m.movement_type}</td>
              <td title={fullDetailText}>
                {shortSummary}
                {m.sources.some(s => s.detail) && (
                  <span style={{fontSize:12, color:"#888"}}>
                    {" (" + m.sources.map(s => s.detail).filter(Boolean).join("; ") + ")"}
                  </span>
                )}
              </td>
              <td>{(m.score * 100).toFixed(0)}%</td>
              <td>{m.max_potential_price ? m.max_potential_price + " USDT" : "-"}</td>
              <td>{m.expected_time_window || "-"}</td>
              <td>{m.notes || m.rationale || "-"}</td>
              <td>{m.success_rate !== undefined ? (m.success_rate * 100).toFixed(0) + '%' : '-'}</td>
            </tr>
          )
        })}
      </tbody>
    </table>
  )
}