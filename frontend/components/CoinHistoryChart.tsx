import React, { useEffect, useState } from "react"
import { Line } from "react-chartjs-2"

export default function CoinHistoryChart({ coin }) {
  const [history, setHistory] = useState([])

  useEffect(() => {
    if (!coin) return
    const fetchHistory = () =>
      fetch(`/api/price-history/${coin}`)
        .then(r => r.json())
        .then(d => setHistory(d.history || []))
    fetchHistory()
    const timer = setInterval(fetchHistory, 60000) // her dakika güncelle
    return () => clearInterval(timer)
  }, [coin])

  if (!history.length) return <div>Veri yok</div>
  return (
    <Line
      data={{
        labels: history.map(h => new Date(h.time * 1000).toLocaleTimeString()),
        datasets: [{
          label: `${coin} Fiyatı`,
          data: history.map(h => h.price),
          borderColor: "#1d7ef2"
        }]
      }}
      options={{ responsive: true, plugins: { legend: { display: true } } }}
    />
  )
}