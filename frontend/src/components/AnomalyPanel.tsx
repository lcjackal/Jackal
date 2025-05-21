import React from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { List, ListItem, ListItemText, Typography, Alert } from '@mui/material'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function AnomalyPanel() {
  const { data, error, isLoading } = useQuery({
    queryKey: ["anomaly"],
    queryFn: async () => (await api.get("/analysis/anomaly")).data,
    refetchInterval: 20000,
  })
  if (isLoading) return <Typography>Yükleniyor...</Typography>
  if (error) return <Alert severity="error">{error.message}</Alert>
  return (
    <>
      <Typography variant="h5">Anomali Analizi</Typography>
      {data.anomalies.length === 0
        ? <Typography color="success.main">Anomali Tespit Edilmedi</Typography>
        : <List>
          {data.anomalies.map((a: any) =>
            <ListItem key={a.symbol}>
              <ListItemText
                primary={`${a.name} (${a.symbol})`}
                secondary={`Fiyat: ${a.price} | Değişim: ${a.change.toFixed(2)}%`}
              />
            </ListItem>
          )}
        </List>}
    </>
  )
}