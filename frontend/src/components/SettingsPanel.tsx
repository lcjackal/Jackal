// ...önceki kodun üstüne ek olarak:

import DownloadIcon from '@mui/icons-material/Download'
import UploadIcon from '@mui/icons-material/Upload'

const handleExport = async () => {
  const res = await api.get("/settings/export", { responseType: "blob" })
  const url = window.URL.createObjectURL(new Blob([res.data]))
  const link = document.createElement("a")
  link.href = url
  link.setAttribute("download", "settings.json")
  document.body.appendChild(link)
  link.click()
}

const handleImport = async (e) => {
  const file = e.target.files[0]
  if (!file) return
  const formData = new FormData()
  formData.append("file", file)
  await api.post("/settings/import", formData)
  setMsg("Ayarlar yüklendi.")
  queryClient.invalidateQueries(["settings"])
}

// ...panel sonuna ekle:
<Box sx={{ mt: 2 }}>
  <Button variant="outlined" startIcon={<DownloadIcon />} onClick={handleExport}>Yedekle</Button>
  <Button variant="outlined" startIcon={<UploadIcon />} component="label">Geri Yükle
    <input hidden type="file" accept=".json" onChange={handleImport} />
  </Button>
</Box>