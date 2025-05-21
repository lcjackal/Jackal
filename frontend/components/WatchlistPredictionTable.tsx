import React from "react"

export default function WatchlistPredictionTable({ predictions }) {
  return (
    <table className="table">
      <thead>
        <tr>
          <th>Coin</th>
          <th>Mevcut Fiyat</th>
          <th>24s Maks. Tahmini Fiyat / Zaman</th>
          <th>24s Min. Tahmini Fiyat / Zaman</th>
          <th>Haftalık Fırsat</th>
        </tr>
      </thead>
      <tbody>
        {predictions.map((p, i) => (
          <tr key={i}>
            <td>{p.coin}</td>
            <td>{p.current_price}</td>
            <td>
              <span title={p.max_detail}>
                <b>{p.max_price_24h}</b>
                <br/>
                <span style={{fontSize:12, color:"#888"}}>{p.max_time_window_24h}</span>
              </span>
            </td>
            <td>
              <span title={p.min_detail}>
                <b>{p.min_price_24h}</b>
                <br/>
                <span style={{fontSize:12, color:"#888"}}>{p.min_time_window_24h}</span>
              </span>
            </td>
            <td>
              {p.weekly_opportunity
                ? <span style={{color:"#090"}} title={p.weekly_detail}>{p.weekly_opportunity}</span>
                : <span style={{color:"#888"}}>-</span>
              }
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}