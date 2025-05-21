// ... mevcut kodun en üstüne ekle:
import DownloadIcon from '@mui/icons-material/Download';

// ... mevcut kodun <Box> içindeki üst kısmına ekle:
<Box sx={{ mb: 2 }}>
  {/* ... eski kod ... */}
  <Button
    variant="outlined"
    startIcon={<DownloadIcon />}
    href={api.defaults.baseURL + "/report/portfolio_csv"}
    target="_blank"
    sx={{ ml: 2 }}
  >
    Rapor (CSV) İndir
  </Button>
</Box>