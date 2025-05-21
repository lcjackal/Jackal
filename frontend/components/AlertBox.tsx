import React from "react"

export default function AlertBox({ type, msg, onClose }) {
  const colors = {
    error: "#f8d7da",
    info: "#e2e3e5",
    warn: "#fff3cd",
    success: "#d4edda"
  }
  return (
    <div style={{
      background: colors[type] || "#eee",
      border: "1px solid #bbb",
      borderRadius: 5,
      padding: 8,
      marginBottom: 10,
      color: "#333",
      position: "relative"
    }}>
      <span>{msg}</span>
      {onClose && (
        <button onClick={onClose} style={{
          position: "absolute", right: 8, top: 8,
          border: "none", background: "transparent", fontSize: 16, cursor: "pointer"
        }}>✕</button>
      )}
    </div>
  )
}