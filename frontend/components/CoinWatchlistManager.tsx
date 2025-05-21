import React, { useState } from "react"

export default function CoinWatchlistManager({ allCoins, watchlist, setWatchlist, selected, setSelected, addAlert }) {
  const [search, setSearch] = useState("")
  const filtered = allCoins.filter(c => c.toLowerCase().includes(search.toLowerCase()))

  function addCoin(coin) {
    if (watchlist.length >= 10) {
      addAlert && addAlert("error", "En fazla 10 coin izlenebilir!")
      return
    }
    if (!watchlist.includes(coin)) setWatchlist([...watchlist, coin])
  }

  function toggleSelect(c) {
    setSelected(
      selected.includes(c)
        ? selected.filter(x => x !== c)
        : [...selected, c]
    )
  }

  return (
    <div style={{marginBottom: 16}}>
      <input
        type="text"
        placeholder="Coin ara (örn: RACA)"
        value={search}
        onChange={e => setSearch(e.target.value)}
        style={{marginRight:8, padding:4}}
      />
      <div style={{marginBottom:8}}>
        {filtered.slice(0,10).map(c => (
          <button
            key={c}
            onClick={() => addCoin(c)}
            disabled={watchlist.includes(c)}
            style={{
              marginRight:6,
              marginBottom:4,
              background: watchlist.includes(c) ? "#b2ffb2" : "#f0f0f0",
              border: "1px solid #bbb",
              borderRadius: 4,
              cursor: watchlist.includes(c) ? "default" : "pointer"
            }}
          >
            {c} {watchlist.includes(c) ? "✓" : "+"}
          </button>
        ))}
      </div>
      <div>
        <b>İzleme Listesi:</b>
        {watchlist.length === 0 ? <span style={{color:"#888"}}> yok</span> :
        watchlist.map(c => (
          <span key={c} style={{marginRight:8}}>
            <input
              type="checkbox"
              checked={selected.includes(c)}
              onChange={() => toggleSelect(c)}
            />
            {c}
            <button
              title="Listeden çıkar"
              style={{
                marginLeft:2,
                color:"red",
                border:"none",
                background:"transparent",
                cursor:"pointer"
              }}
              onClick={() => setWatchlist(watchlist.filter(x => x !== c))}
            >✕</button>
          </span>
        ))}
      </div>
      <div style={{fontSize:13, marginTop:5}}>
        <b>Tarama:</b>
        <button onClick={() => setSelected([...watchlist])} style={{marginRight:6}}>Tümünü Tara</button>
        <button onClick={() => setSelected([])}>Seçimi Temizle</button>
      </div>
      <div style={{fontSize:12, color:"#888", marginTop:4}}>
        Not: Sadece seçili coinler için tahmin tablosu oluşturulur. En fazla 10 coin izlenebilir.
      </div>
    </div>
  )
}