import React, { useState, useEffect } from "react"

export default function OpportunitiesArchive() {
  const [opps, setOpps] = useState([])

  useEffect(() => {
    fetch("/api/opportunity-archive")
      .then(r => r.json())
      .then(data => setOpps(data.opportunities || []))
  }, [])

  return (
    <div>
      <h2>Geçmiş Fırsatlar Arşivi</h2>
      <table>
        <thead>
          <tr>
            <th>Coin</th>
            <th>Tahmin</th>
            <th>Durum</th>
            <th>Gerekçe</th>
            <th>Bitirme Zamanı</th>
            <th>Geçmiş</th>
          </tr>
        </thead>
        <tbody>
          {opps.map(opp => (
            <tr key={opp.id}>
              <td>{opp.coin}</td>
              <td>{opp.initial_prediction}</td>
              <td>{opp.status}</td>
              <td>{opp.reason}</td>
              <td>{new Date(opp.last_update * 1000).toLocaleString()}</td>
              <td>
                <details>
                  <summary>Geçmiş</summary>
                  <ul>
                    {opp.history.map((h, i) => (
                      <li key={i}>
                        {new Date(h.time * 1000).toLocaleString()} - {h.status} - {h.prediction} - {h.reason}
                      </li>
                    ))}
                  </ul>
                </details>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}