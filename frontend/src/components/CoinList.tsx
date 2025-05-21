import React from 'react'
import { useQuery } from '@tanstack/react-query'
import axios from 'axios'
import { Table, TableHead, TableBody, TableRow, TableCell, Typography, Alert } from '@mui/material'

const api = axios.create({ baseURL: import.meta.env.VITE_API_URL })

export default function CoinList() {
  const { data, error, isLoading } = useQuery({
    queryKey: ["coins"],
    queryFn: async () => (await api.get("/coins")).data,
    refetchInterval: 15000,
  })
  if (isLoading) return <Typography>Yükleniyor...</Typography>
  if (error) return <Alert severity="error">{error.message}</Alert>
  return (
    <>
      <Typography variant="h5">Coin Listesi</Typography>
      <Typography variant="body2" color="gray">{data.notification}</Typography>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Ad</TableCell><TableCell>Sembol</TableCell><TableCell>Fiyat</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.data.slice(0, 20).map((c: any) =>
            <TableRow key={c.id || c.symbol}>
              <TableCell>{c.name}</TableCell>
              <TableCell>{c.symbol}</TableCell>
              <TableCell>{c.price || c.current_price || "-"}</TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </>
  )
}