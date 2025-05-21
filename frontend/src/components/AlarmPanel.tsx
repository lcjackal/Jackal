import React, { useState } from 'react'
import axios from 'axios'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { Box, Typography, TextField, Button, List, ListItem, ListItemText, IconButton, Alert } from '@mui/material'
import DeleteIcon from '@mui/icons-material/Delete'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function AlarmPanel() {
  const [symbol, setSymbol] = useState("")
  const [threshold, setThreshold] = useState("")
  const [direction, setDirection] = useState("above")
  const [msg, setMsg] = useState("")
  const queryClient = useQueryClient()

  const { data, refetch } = useQuery({
    queryKey: ["alarms"],
    queryFn: async () => (await api.get("/alarms")).data,
    refetchInterval: 20000,
  })

  const handleAdd = async () => {
    try {
      await api.post("/alarms", { symbol: symbol.trim().toLowerCase(), threshold: parseFloat(threshold), direction })
      setMsg("Alarm kaydedildi.")
      setSymbol("")
      setThreshold("")
      queryClient.invalidateQueries(["alarms"])
    } catch { setMsg("Alarm kaydedilemedi!") }
  }

  const handleDelete = async (id: number) => {
    await api.delete(`/alarms/${id}`)
    queryClient.invalidateQueries(["alarms"])
  }

  return (
    <Box>
      <Typography variant="h5">Fiyat Alarmı Sistemi</Typography>
      <Box sx={{ mb: 2 }}>
        <TextField label="Coin Sembolü" value={symbol} onChange={e => setSymbol(e.target.value)} sx={{ mr: 1 }} />
        <TextField label="Fiyat" value={threshold} onChange={e => setThreshold(e.target.value)} sx={{ mr: 1 }} />
        <Button onClick={() => setDirection("above")} variant={direction === "above" ? "contained" : "outlined"} sx={{ mr: 1 }}>Üstünde</Button>
        <Button onClick={() => setDirection("below")} variant={direction === "below" ? "contained" : "outlined"} sx={{ mr: 1 }}>Altında</Button>
        <Button onClick={handleAdd} variant="contained">Alarm Ekle</Button>
      </Box>
      {msg && <Alert severity="info">{msg}</Alert>}
      <List>
        {data?.alarms.map((a: any) =>
          <ListItem key={a.id} secondaryAction={
            <IconButton edge="end" onClick={() => handleDelete(a.id)}><DeleteIcon /></IconButton>
          }>
            <ListItemText
              primary={`${a.symbol.toUpperCase()} ${a.direction === "above" ? ">" : "<"} ${a.threshold}`}
              secondary={a.notified ? "Tetiklendi" : "Bekliyor"}
            />
          </ListItem>
        )}
      </List>
    </Box>
  )
}