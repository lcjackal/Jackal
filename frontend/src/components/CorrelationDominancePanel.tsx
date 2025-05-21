import React, { useState } from 'react'
import { Box, Typography, TextField, Button, Table, TableBody, TableCell, TableHead, TableRow, Divider, Alert } from '@mui/material'
import axios from 'axios'
import { useQuery } from '@tanstack/react-query'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function CorrelationDominancePanel() {
  const [symbols, setSymbols] = useState("bitcoin,ethereum,solana")
  const [querySymbols, setQuerySymbols] = useState("bitcoin,ethereum,solana")

  const { data: corr, error: err1, isLoading: loading1 } = useQuery({
    queryKey: ["correlation", querySymbols],
    queryFn: async () => (await api.get(`/analysis/correlation?symbols=${querySymbols}`)).data,
    enabled: !!querySymbols,
  })
  const { data: dom, error: err2, isLoading: loading2 } = useQuery({
    queryKey: ["dominance", querySymbols],
    queryFn: async () => (await api.get(`/analysis/dominance?symbols=${querySymbols}`)).data,
    enabled: !!querySymbols,
  })

  const handleQuery = () => setQuerySymbols(symbols.replace(/\s/g, ""))

  return (
    <Box>
      <Typography variant="h5">Korelasyon & Market Dominance</Typography>
      <Box sx={{ mt: 2, mb: 2 }}>
        <TextField
          label="Coin Sembolleri (virgül ile, örn: bitcoin,ethereum,solana)"
          value={symbols}
          onChange={e => setSymbols(e.target.value)}
          sx={{ mr: 1, width: 400 }}
        />
        <Button variant="contained" onClick={handleQuery}>Göster</Button>
      </Box>
      <Divider sx={{ my: 1 }} />
      <Typography variant="subtitle1">Korelasyon Matrisi (1: aynı, -1: zıt hareket):</Typography>
      {loading1 && <Typography>Yükleniyor...</Typography>}
      {err1 && <Alert severity="error">{err1.message}</Alert>}
      {corr && corr.matrix && (
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell />
              {Object.keys(corr.matrix).map(s => <TableCell key={s}>{s.toUpperCase()}</TableCell>)}
            </TableRow>
          </TableHead>
          <TableBody>
            {Object.keys(corr.matrix).map(s1 =>
              <TableRow key={s1}>
                <TableCell>{s1.toUpperCase()}</TableCell>
                {Object.keys(corr.matrix[s1]).map(s2 =>
                  <TableCell key={s2}>{corr.matrix[s1][s2]?.toFixed(2)}</TableCell>
                )}
              </TableRow>
            )}
          </TableBody>
        </Table>
      )}
      <Divider sx={{ my: 2 }} />
      <Typography variant="subtitle1">Market Dominance (%):</Typography>
      {loading2 && <Typography>Yükleniyor...</Typography>}
      {err2 && <Alert severity="error">{err2.message}</Alert>}
      {dom && dom.dominance && (
        <>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Coin</TableCell>
                <TableCell>Dominance (%)</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {Object.entries(dom.dominance).map(([sym, val]) =>
                <TableRow key={sym}>
                  <TableCell>{sym.toUpperCase()}</TableCell>
                  <TableCell>{val}</TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
          <Typography variant="body2" color="gray" sx={{ mt: 1 }}>
            Toplam Market Cap: ${dom.total_cap?.toLocaleString()}
          </Typography>
        </>
      )}
    </Box>
  )
}