import React, { useState } from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import DownloadIcon from '@mui/icons-material/Download';
import UploadIcon from '@mui/icons-material/Upload';

// Eğer api ve queryClient yoksa, aşağıdaki satırları ekleyin veya kendi projenize göre uyarlayın
// import api from "../api"; // api.js veya api.ts dosyanız varsa
// import { useQueryClient } from "react-query";
// const queryClient = useQueryClient();

const SettingsPanel: React.FC = () => {
  // Eğer mesaj göstermek istiyorsan:
  const [msg, setMsg] = useState<string | null>(null);

  const handleExport = async () => {
    // api nesnesi projenizde tanımlı olmalı!
    const res = await api.get("/settings/export", { responseType: "blob" });
    const url = window.URL.createObjectURL(new Blob([res.data]));
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "settings.json");
    document.body.appendChild(link);
    link.click();
  };

  const handleImport = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    await api.post("/settings/import", formData);
    setMsg("Ayarlar yüklendi.");
    // queryClient.invalidateQueries(["settings"]); // react-query kullanıyorsan aç
  };

  return (
    <Box sx={{ mt: 2 }}>
      <h2>Ayarlar</h2>
      {msg && <div>{msg}</div>}
      <Button variant="outlined" startIcon={<DownloadIcon />} onClick={handleExport}>
        Yedekle
      </Button>
      <Button variant="outlined" startIcon={<UploadIcon />} component="label">
        Geri Yükle
        <input hidden type="file" accept=".json" onChange={handleImport} />
      </Button>
    </Box>
  );
};

export default SettingsPanel;