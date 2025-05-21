import React, { useState, useEffect } from "react"
import CoinWatchlistManager from "../components/CoinWatchlistManager"
import WatchlistPredictionTable from "../components/WatchlistPredictionTable"
import WeeklyOpportunitiesPanel from "../components/WeeklyOpportunitiesPanel"

// Örnek coin listesi
const allCoins = ["BTC", "ETH", "RACA", "DOGE", "SOL", "AVAX", "SHIB", "ADA", "XRP", "BNB"]

export default function WatchlistDashboard() {
  const [watchlist, setWatchlist] = useState(["RACA"])
  const [selected, setSelected] = useState(["RACA"])
  const [predictions, setPredictions] = useState([])
  const [weeklyOpps, setWeeklyOpps] = useState([])

  useEffect(() => {
    if (!selected.length) { setPredictions([]); setWeeklyOpps([]); return }
    fetch("/api/watchlist-predictions", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ coins: selected })
    }).then(r => r.json()).then(data => {
      setPredictions(data.predictions)
      setWeeklyOpps(data.weekly_opportunities)
    })
  }, [selected])

  return (
    <div>
      <h2>İzleme Listesi Paneli</h2>
      <CoinWatchlistManager
        allCoins={allCoins}
        watchlist={watchlist}
        setWatchlist={setWatchlist}
        selected={selected}
        setSelected={setSelected}
      />
      <WatchlistPredictionTable predictions={predictions} />
      <WeeklyOpportunitiesPanel opportunities={weeklyOpps} />
    </div>
  )
}