import { useState } from "react"
import { Box, TextField, Switch, Button, Typography, Alert, Select, MenuItem } from "@mui/material"
import axios from "axios"
const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function ExchangeSettingsPanel({ exchangesSettings, onChange }) {
  const [status, setStatus] = useState({})
  const handleApiTest = async (ex, key, secret) => {
    setStatus({...status, [ex]: "Doğrulanıyor..."})
    const res = await api.post("/exchange/test_api", { exchange: ex, api_key: key, api_secret: secret })
    setStatus({...status, [ex]: res.data.ok ? "Başarılı" : `Hata: ${res.data.msg}` })
  }
  return (
    <Box>
      {Object.entries(exchangesSettings).map(([ex, exdata]) => (
        <Box key={ex} sx={{ mb: 3, border: "1px solid #ccc", p: 2, borderRadius: 2 }}>
          <Typography variant="h6">{ex.toUpperCase()}</Typography>
          <Select
            value={exdata.mode}
            onChange={e => onChange(ex, { ...exdata, mode: e.target.value })}
            sx={{ minWidth: 120, mr: 2 }}
          >
            <MenuItem value="public">Public Mode (API keysiz, genel veri)</MenuItem>
            <MenuItem value="full">Full Mode (API key ile, tüm özellikler)</MenuItem>
          </Select>
          <TextField
            label="API Key"
            value={exdata.api_keys.key || ""}
            onChange={e => onChange(ex, { ...exdata, api_keys: { ...exdata.api_keys, key: e.target.value } })}
            sx={{ mr: 1, width: 250 }}
            disabled={exdata.mode !== "full"}
          />
          <TextField
            label="API Secret"
            value={exdata.api_keys.secret || ""}
            onChange={e => onChange(ex, { ...exdata, api_keys: { ...exdata.api_keys, secret: e.target.value } })}
            sx={{ width: 250 }}
            disabled={exdata.mode !== "full"}
          />
          <Button
            variant="outlined"
            onClick={() => handleApiTest(ex, exdata.api_keys.key, exdata.api_keys.secret)}
            disabled={exdata.mode !== "full" || !exdata.api_keys.key || !exdata.api_keys.secret}
            sx={{ ml: 2 }}
          >API Test</Button>
          {status[ex] && <Alert severity={status[ex].startsWith("Hata") ? "error" : "success"} sx={{ mt: 1 }}>{status[ex]}</Alert>}
          {exdata.mode === "public" && <Alert severity="info" sx={{ mt: 1 }}>Sadece genel veri çekilir. Portföy/emir/kişisel işlemler kapalıdır.</Alert>}
          {exdata.mode === "full" && (!exdata.api_keys.key || !exdata.api_keys.secret) &&
            <Alert severity="warning" sx={{ mt: 1 }}>API key/secret eksik! Private işlemler devre dışı, sadece public veri çekilecek.</Alert>}
        </Box>
      ))}
    </Box>
  )
}