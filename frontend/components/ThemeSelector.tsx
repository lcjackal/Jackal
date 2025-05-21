import React from "react"
const THEMES = [
  { name: "Açık", key: "light" },
  { name: "Koyu", key: "dark" },
  { name: "Deniz", key: "sea" },
  { name: "Galaksi", key: "galaxy" },
  { name: "Mistik", key: "mystic" },
  { name: "Retro", key: "retro" }
]
export default function ThemeSelector({ theme, setTheme }) {
  return (
    <div style={{ marginBottom: 10 }}>
      <b>Tema:</b>
      {THEMES.map(t => (
        <button
          key={t.key}
          style={{
            marginLeft: 8,
            background: theme === t.key ? "#1d7ef2" : "#eee",
            color: theme === t.key ? "#fff" : "#222",
            borderRadius: 4,
            padding: "4px 10px",
            border: theme === t.key ? "2px solid #1d7ef2" : "1px solid #ccc"
          }}
          onClick={() => setTheme(t.key)}
        >{t.name}</button>
      ))}
    </div>
  )
}