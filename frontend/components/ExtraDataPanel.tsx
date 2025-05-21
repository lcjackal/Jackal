import React, { useState } from "react"

export default function ExtraDataPanel({ coin, apiKeys }) {
  const [data, setData] = useState(null)
  const [err, setErr] = useState("")
  const [loading, setLoading] = useState(false)

  function fetchData() {
    setLoading(true)
    setErr("")
    fetch("/api/extra-data", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ coin, api_keys: apiKeys })
    })
      .then(r => r.json())
      .then(d => { setData(d); setLoading(false) })
      .catch(e => { setErr(e.message); setLoading(false) })
  }

  return (
    <div style={{marginTop:12, marginBottom:12, padding:10, border:"1px solid #abc", borderRadius:6}}>
      <b>Zincir Üstü ve Sentiment Verisi</b>
      <button onClick={fetchData} disabled={loading} style={{marginLeft:8}}>
        {loading ? "Yükleniyor..." : "Verileri Getir"}
      </button>
      {err && <div style={{color:"red"}}>{err}</div>}
      {data && (
        <div style={{marginTop:8, fontSize:13}}>
          {data.onchain && (
            <div>
              <b>On-chain (ETH):</b> USD: {data.onchain.ethusd}, BTC: {data.onchain.ethbtc}
            </div>
          )}
          {data.sentiment && (
            <div>
              <b>Sentiment:</b> Galaxy Score: {data.sentiment.galaxy_score}, AltRank: {data.sentiment.alt_rank}, Social Volume: {data.sentiment.social_volume}
            </div>
          )}
          {data.news && (
            <div>
              <b>Haber:</b> {JSON.stringify(data.news)}
            </div>
          )}
        </div>
      )}
    </div>
  )
}