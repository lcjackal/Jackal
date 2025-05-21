import React, { useState, useEffect } from "react"

// API anahtarı localStorage'da şifreli tutulur (örnek için Base64, üretim için encrypt önerilir)
function getKey(key) {
  const v = localStorage.getItem(key)
  return v ? atob(v) : ""
}
function setKey(key, value) {
  if (value) localStorage.setItem(key, btoa(value))
  else localStorage.removeItem(key)
}

export default function ApiKeyManager({ keys, setKeys, supportedApis }) {
  const [edit, setEdit] = useState(false)
  const [form, setForm] = useState(keys)

  useEffect(() => setForm(keys), [keys])

  function handleSave() {
    setKeys(form)
    Object.entries(form).forEach(([k, v]) => setKey("api_" + k, v))
    setEdit(false)
  }
  function handleChange(k, v) {
    setForm({ ...form, [k]: v })
  }

  return (
    <div style={{
      border: "1px solid #ccc", borderRadius: 6, background: "#f4f8fc",
      padding: 10, marginBottom: 12
    }}>
      <b>API Ayarları</b>
      {!edit && (
        <div>
          {supportedApis.map(k => (
            <div key={k}>
              {k}: {form[k] ? "•••••••" : <span style={{ color: "#d33" }}>Eksik</span>}
            </div>
          ))}
          <button onClick={() => setEdit(true)} style={{ marginTop: 5 }}>Düzenle</button>
        </div>
      )}
      {edit && (
        <div>
          {supportedApis.map(k => (
            <div key={k} style={{ marginBottom: 6 }}>
              <label style={{ width: 120, display: "inline-block" }}>{k} API Key:</label>
              <input
                type="password"
                value={form[k] || ""}
                onChange={e => handleChange(k, e.target.value)}
                style={{ width: 180 }}
                placeholder="Anahtar girin"
              />
            </div>
          ))}
          <button onClick={handleSave} style={{ marginRight: 8 }}>Kaydet</button>
          <button onClick={() => setEdit(false)}>İptal</button>
        </div>
      )}
      <div style={{ fontSize: 12, color: "#777", marginTop: 4 }}>
        API anahtarınız yalnızca bu cihazda saklanır, sunucuya gönderilmez.
      </div>
    </div>
  )
}

// Kullanımı örnek:
// <ApiKeyManager keys={apiKeys} setKeys={setApiKeys} supportedApis={["binance", "etherscan", "lunarcrush"]}/>