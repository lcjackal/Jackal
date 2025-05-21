import React, { useState } from 'react'
import axios from 'axios'
import { Box, Typography, Tabs, Tab, TextField, Button, Table, TableHead, TableBody, TableRow, TableCell, Alert } from '@mui/material'
import { useQuery } from '@tanstack/react-query'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

function CoinTable({ coins }: { coins: any[] }) {
  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>Coin</TableCell>
          <TableCell>Sembol</TableCell>
          <TableCell>Fiyat</TableCell>
          <TableCell>24s Hacim</TableCell>
          <TableCell>Likidite</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {coins.map((c: any) =>
          <TableRow key={c.id || c.symbol}>
            <TableCell>{c.name}</TableCell>
            <TableCell>{c.symbol}</TableCell>
            <TableCell>{c.price || c.current_price || '-'}</TableCell>
            <TableCell>{c.volume_24h ? c.volume_24h.toLocaleString() : '-'}</TableCell>
            <TableCell>{c.liquidity ? c.liquidity.toLocaleString() : '-'}</TableCell>
          </TableRow>
        )}
      </TableBody>
    </Table>
  )
}

export default function VolumeLiquidityPanel() {
  const [tab, setTab] = useState(0)
  // Hacim filtre
  const [minVol, setMinVol] = useState("")
  const [maxVol, setMaxVol] = useState("")
  // Likidite filtre
  const [minLiq, setMinLiq] = useState("")
  const [maxLiq, setMaxLiq] = useState("")
  // API kullanımı
  const { data: vdata, error: verr, refetch: vfetch } = useQuery({
    queryKey: ["volumes", minVol, maxVol],
    queryFn: async () => (await api.get("/filter/volume", { params: { min_volume: minVol || 0, max_volume: maxVol || 1e20 } })).data,
    enabled: tab === 0,
  })
  const { data: ldata, error: lerr, refetch: lfetch } = useQuery({
    queryKey: ["liquidity", minLiq, maxLiq],
    queryFn: async () => (await api.get("/filter/liquidity", { params: { min_liquidity: minLiq || 0, max_liquidity: maxLiq || 1e20 } })).data,
    enabled: tab === 1,
  })

  return (
    <Box>
      <Typography variant="h5">Hacim &amp; Likidite Filtresi</Typography>
      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2 }}>
        <Tab label="Hacime Göre" />
        <Tab label="Likiditeye Göre" />
      </Tabs>
      {tab === 0 && (
        <>
          <Box sx={{ mb: 2 }}>
            <TextField label="Min Hacim" size="small" value={minVol} onChange={e => setMinVol(e.target.value)} sx={{ mr: 1 }} />
            <TextField label="Max Hacim" size="small" value={maxVol} onChange={e => setMaxVol(e.target.value)} sx={{ mr: 1 }} />
            <Button variant="contained" onClick={vfetch}>Filtrele</Button>
          </Box>
          {verr && <Alert severity="error">{verr.message}</Alert>}
          {vdata && <CoinTable coins={vdata.coins} />}
        </>
      )}
      {tab === 1 && (
        <>
          <Box sx={{ mb: 2 }}>
            <TextField label="Min Likidite" size="small" value={minLiq} onChange={e => setMinLiq(e.target.value)} sx={{ mr: 1 }} />
            <TextField label="Max Likidite" size="small" value={maxLiq} onChange={e => setMaxLiq(e.target.value)} sx={{ mr: 1 }} />
            <Button variant="contained" onClick={lfetch}>Filtrele</Button>
          </Box>
          {lerr && <Alert severity="error">{lerr.message}</Alert>}
          {ldata && <CoinTable coins={ldata.coins} />}
        </>
      )}
    </Box>
  )
}