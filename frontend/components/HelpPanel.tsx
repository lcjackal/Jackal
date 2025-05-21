import React, { useEffect, useState } from "react"

export default function HelpPanel({ onClose }) {
  const [text, setText] = useState("")
  useEffect(() => {
    fetch("/docs/USER_GUIDE.md")
      .then(r => r.text())
      .then(setText)
  }, [])
  return (
    <div style={{
      position: 'fixed', top: 60, right: 60, background: "#fff", border: "1px solid #aaa", zIndex: 100, padding: 20, width: 600, height: 500, overflowY: "auto"
    }}>
      <button onClick={onClose} style={{ float: "right" }}>Kapat</button>
      <h2>Kullanıcı Rehberi</h2>
      <pre style={{ whiteSpace: "pre-wrap" }}>{text}</pre>
    </div>
  )
}