import React from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Box, Typography, List, ListItem, ListItemText, Divider } from '@mui/material'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function AdvancedPanel() {
  const { data, error, isLoading } = useQuery({
    queryKey: ["advanced"],
    queryFn: async () => (await api.get("/analysis/advanced")).data,
    refetchInterval: 25000,
  })
  if (isLoading) return <Typography>Yükleniyor...</Typography>
  if (error) return <Typography color="error">{error.message}</Typography>

  return (
    <Box>
      <Typography variant="h5" sx={{mb:1}}>İleri Analiz Özeti</Typography>
      <Typography>
        Toplam coin: <b>{data.stats.coin_count}</b> | Fiyat ortalaması: <b>${data.stats.price_avg?.toFixed(2)}</b>
      </Typography>
      <Typography>
        En yüksek fiyat: <b>${data.stats.price_max?.toFixed(2)}</b> | En düşük fiyat: <b>${data.stats.price_min?.toFixed(2)}</b>
      </Typography>
      <Typography>
        Günlük ort. değişim: <b>{data.stats.change_avg?.toFixed(2)}%</b>
      </Typography>
      <Divider sx={{my:1}} />
      <Typography variant="subtitle1">En çok yükselenler:</Typography>
      <List dense>
        {data.top_gainers.map((c: any) =>
          <ListItem key={c.symbol}>
            <ListItemText primary={`${c.name} (${c.symbol})`} secondary={`Değişim: ${(c.change_24h || c.price_change_percentage_24h || 0).toFixed(2)}%`} />
          </ListItem>)}
      </List>
      <Typography variant="subtitle1">En çok düşenler:</Typography>
      <List dense>
        {data.top_losers.map((c: any) =>
          <ListItem key={c.symbol}>
            <ListItemText primary={`${c.name} (${c.symbol})`} secondary={`Değişim: ${(c.change_24h || c.price_change_percentage_24h || 0).toFixed(2)}%`} />
          </ListItem>)}
      </List>
      <Divider sx={{my:1}} />
      <Typography variant="subtitle1">Büyük hareketli coin(ler) (&gt;10%):</Typography>
      <List dense>
        {data.big_movers.length === 0
          ? <ListItem><ListItemText primary="Yok" /></ListItem>
          : data.big_movers.map((c: any) =>
              <ListItem key={c.symbol}>
                <ListItemText primary={`${c.name} (${c.symbol})`} secondary={`Değişim: ${(c.change_24h || c.price_change_percentage_24h || 0).toFixed(2)}%`} />
              </ListItem>)
        }
      </List>
      <Divider sx={{my:1}} />
      <Typography variant="subtitle1" color="error">Anomali/Uyarılar (&gt;20% değişim):</Typography>
      <List dense>
        {data.anomalies.length === 0
          ? <ListItem><ListItemText primary="Anomali yok" /></ListItem>
          : data.anomalies.map((a: any) =>
              <ListItem key={a.symbol}>
                <ListItemText primary={`${a.name} (${a.symbol})`} secondary={`Fiyat: $${a.price} | Değişim: ${a.change.toFixed(2)}%`} />
              </ListItem>)
        }
      </List>
      <Divider sx={{my:1}} />
      <Typography variant="caption" color="gray">Tüm analizler arka planda otomatik yapılır ve sade şekilde özetlenir.</Typography>
    </Box>
  )
}