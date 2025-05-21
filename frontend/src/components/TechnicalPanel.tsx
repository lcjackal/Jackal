import React, { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Box, Typography, TextField, Button, Alert } from '@mui/material'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function TechnicalPanel() {
  const [symbol, setSymbol] = useState("bitcoin")
  const [query, setQuery] = useState("bitcoin")
  const { data, error, isLoading } = useQuery({
    queryKey: ["technical", query],
    queryFn: async () => (await api.get(`/analysis/technical/${query}`)).data,
    enabled: !!query,
    refetchOnWindowFocus: false,
  })

  return (
    <Box>
      <Typography variant="h5">Teknik Analiz Göstergeleri</Typography>
      <Box sx={{ mt: 2, mb: 2 }}>
        <TextField label="Coin Sembolü" value={symbol} onChange={e => setSymbol(e.target.value)} sx={{ mr: 1 }} />
        <Button variant="contained" onClick={() => setQuery(symbol)}>Göster</Button>
      </Box>
      {isLoading && <Typography>Yükleniyor...</Typography>}
      {error && <Alert severity="error">{error.message}</Alert>}
      {data && !data.error && (
        <Box>
          <Typography>RSI: <b>{data.rsi && data.rsi.toFixed(2)}</b></Typography>
          <Typography>Volatilite: <b>{data.volatility && (data.volatility * 100).toFixed(2)}%</b></Typography>
          <Typography>MACD: <b>{data.macd && data.macd.toFixed(4)}</b></Typography>
          <Typography>MACD Sinyal: <b>{data.macd_signal && data.macd_signal.toFixed(4)}</b></Typography>
        </Box>
      )}
      {data && data.error && <Alert severity="warning">{data.error}</Alert>}
    </Box>
  )
}