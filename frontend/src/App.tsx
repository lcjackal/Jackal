// ... diğer importlar
import SettingsPanel from './components/SettingsPanel'
import TrackedCoinsPanel from './components/TrackedCoinsPanel'
// ... uygun yere ekle:
<Tab label="Ayarlar" />
<Tab label="İzlenen Coinler" />
// ...
{tab === 11 && <TrackedCoinsPanel />}
{tab === 12 && <SettingsPanel />}