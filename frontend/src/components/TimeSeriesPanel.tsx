import React, { useState } from 'react'
import { Box, Typography, TextField, Button, Table, TableHead, TableRow, TableCell, TableBody, Alert } from '@mui/material'
import axios from 'axios'
import { useQuery } from '@tanstack/react-query'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function TimeSeriesPanel() {
  const [symbol, setSymbol] = useState("bitcoin")
  const [query, setQuery] = useState("bitcoin")
  const { data, error, isLoading } = useQuery({
    queryKey: ["summary", query],
    queryFn: async () => (await api.get(`/analysis/summary?symbol=${query}`)).data,
    enabled: !!query,
    refetchOnWindowFocus: false,
  })

  return (
    <Box>
      <Typography variant="h5">Zaman Serisi &amp; Geçmiş Karşılaştırmalı Özet</Typography>
      <Box sx={{ mt: 2, mb: 2 }}>
        <TextField label="Coin Sembolü" value={symbol} onChange={e => setSymbol(e.target.value)} sx={{ mr: 1 }} />
        <Button variant="contained" onClick={() => setQuery(symbol.trim().toLowerCase())}>Göster</Button>
      </Box>
      {isLoading && <Typography>Yükleniyor...</Typography>}
      {error && <Alert severity="error">{error.message}</Alert>}
      {data && !data.error && (
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Mevcut Fiyat</TableCell>
              <TableCell>1g %</TableCell>
              <TableCell>7g %</TableCell>
              <TableCell>30g %</TableCell>
              <TableCell>7g Hacim Ort.</TableCell>
              <TableCell>30g Hacim Ort.</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            <TableRow>
              <TableCell>{data.current_price?.toLocaleString()}</TableCell>
              <TableCell>{data.change_1d?.toFixed(2)}%</TableCell>
              <TableCell>{data.change_7d?.toFixed(2)}%</TableCell>
              <TableCell>{data.change_30d?.toFixed(2)}%</TableCell>
              <TableCell>{data.avg_vol_7d?.toLocaleString()}</TableCell>
              <TableCell>{data.avg_vol_30d?.toLocaleString()}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      )}
      {data && data.error && <Alert severity="warning">{data.error}</Alert>}
    </Box>
  )
}