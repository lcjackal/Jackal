import React, { useState, useEffect } from "react"

export default function UserSettingsPanel({ onClose }) {
  const [theme, setTheme] = useState("default")
  const [refresh, setRefresh] = useState(60000)
  const [apiKey, setApiKey] = useState("")
  const [saved, setSaved] = useState(false)

  useEffect(() => {
    fetch("/api/user-settings")
      .then(r => r.json())
      .then(d => {
        setTheme(d.theme || "default")
        setRefresh(Number(d.refresh) || 60000)
        setApiKey(d.apiKey || "")
      })
  }, [])

  function save() {
    fetch("/api/user-settings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ theme, refresh, apiKey })
    })
      .then(() => setSaved(true))
      .then(() => setTimeout(() => setSaved(false), 2000))
  }

  return (
    <div style={{
      position: "fixed", top: 50, right: 50, background: "#fff", border: "1px solid #aaa", padding: 16, zIndex: 99
    }}>
      <h4>Ayarlar</h4>
      <div>
        <label>Tema:
          <select value={theme} onChange={e => setTheme(e.target.value)}>
            <option value="default">Varsayılan</option>
            <option value="dark">Koyu</option>
            <option value="blue">Mavi</option>
            <option value="green">Yeşil</option>
            <option value="yellow">Sarı</option>
            <option value="pink">Pembe</option>
          </select>
        </label>
      </div>
      <div>
        <label>Otomatik Yenileme (sn):
          <input type="number" min={10} max={600} value={refresh / 1000} onChange={e => setRefresh(Number(e.target.value) * 1000)} />
        </label>
      </div>
      <div>
        <label>API Key:
          <input type="text" value={apiKey} onChange={e => setApiKey(e.target.value)} />
        </label>
      </div>
      <button onClick={save}>Kaydet</button>
      <button onClick={onClose} style={{ marginLeft: 8 }}>Kapat</button>
      {saved && <span style={{ color: "green", marginLeft: 12 }}>Kaydedildi!</span>}
    </div>
  )
}