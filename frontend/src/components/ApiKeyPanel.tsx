import React, { useState } from 'react'
import axios from 'axios'
import { TextField, Button, Typography, Alert } from '@mui/material'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function ApiKeyPanel() {
  const [provider, setProvider] = useState("")
  const [key, setKey] = useState("")
  const [msg, setMsg] = useState("")
  const [err, setErr] = useState("")
  const handleSave = async () => {
    try {
      const res = await api.post("/settings/provider", { provider, api_key: key })
      setMsg(res.data.notification)
      setErr("")
    } catch (e: any) {
      setErr(e.response?.data?.detail?.error || "Bilinmeyen hata")
      setMsg("")
    }
  }
  return (
    <>
      <Typography variant="h5">API Key Ayarı</Typography>
      <TextField label="Provider (örn: coinmarketcap)" value={provider} onChange={e => setProvider(e.target.value)} fullWidth sx={{ my: 1 }} />
      <TextField label="API Key" value={key} onChange={e => setKey(e.target.value)} fullWidth sx={{ my: 1 }} />
      <Button onClick={handleSave} variant="contained">Kaydet</Button>
      {msg && <Alert severity="success" sx={{ mt: 2 }}>{msg}</Alert>}
      {err && <Alert severity="error" sx={{ mt: 2 }}>{err}</Alert>}
    </>
  )
}