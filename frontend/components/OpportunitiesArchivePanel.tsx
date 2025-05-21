import React, { useEffect, useState } from "react"
import DataQualityBadge from "./DataQualityBadge"

function formatTime(ts) {
  const d = new Date(ts * 1000)
  return d.toLocaleString()
}

export default function OpportunitiesArchivePanel() {
  const [opps, setOpps] = useState([])
  const [filter, setFilter] = useState("")
  const [status, setStatus] = useState("all")
  const [selected, setSelected] = useState(null)

  useEffect(() => {
    fetch("/api/opportunity-archive")
      .then(r => r.json())
      .then(d => setOpps(d.opportunities || []))
  }, [])

  let filtered = opps
  if (filter) {
    filtered = filtered.filter(opp =>
      opp.coin.toLowerCase().includes(filter.toLowerCase()) ||
      opp.current_prediction.toLowerCase().includes(filter.toLowerCase())
    )
  }
  if (status !== "all") {
    filtered = filtered.filter(opp => opp.status === status)
  }

  return (
    <div>
      <h3>Geçmiş Fırsat Arşivi</h3>
      <div style={{marginBottom: 10}}>
        <input
          type="text"
          placeholder="Coin veya tahmin ara"
          value={filter}
          onChange={e => setFilter(e.target.value)}
        />
        <select
          value={status}
          onChange={e => setStatus(e.target.value)}
          style={{marginLeft: 10}}
        >
          <option value="all">Durum: Tümü</option>
          <option value="iptal">İptal</option>
          <option value="gerçekleşti">Gerçekleşti</option>
        </select>
      </div>
      <table className="table">
        <thead>
          <tr>
            <th>Coin</th>
            <th>Tespit Edilen</th>
            <th>Son Tahmin</th>
            <th>Durum</th>
            <th>Gerekçe</th>
            <th>Son Güncelleme</th>
            <th>Veri Kalitesi</th>
            <th>Detay</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map(opp => (
            <tr key={opp.id}>
              <td>
                <button onClick={() => setSelected(opp)}>
                  {opp.coin}
                </button>
              </td>
              <td>{opp.initial_prediction}</td>
              <td>{opp.current_prediction}</td>
              <td>{opp.status}</td>
              <td>{opp.reason}</td>
              <td>{formatTime(opp.last_update)}</td>
              <td><DataQualityBadge quality={opp.quality || "Orta"} /></td>
              <td>
                <button onClick={() => setSelected(opp)}>Geçmiş</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {/* Detay modalı */}
      {selected &&
        <div style={{
          position: "fixed", top: 80, left: "10vw", width: "80vw", background: "#fff",
          border: "1px solid #bbb", zIndex: 100, maxHeight: 400, overflowY: "auto", padding: 20
        }}>
          <button onClick={() => setSelected(null)} style={{ float: "right" }}>Kapat</button>
          <h4>{selected.coin} Detay & Geçmiş</h4>
          <ul>
            {selected.history.map((h, i) => (
              <li key={i}>
                {formatTime(h.time)} - <b>{h.status}</b> - {h.prediction} ({h.reason})
              </li>
            ))}
          </ul>
        </div>
      }
    </div>
  )
}