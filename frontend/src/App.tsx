import React, { useState } from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import SettingsPanel from './components/SettingsPanel';
import TrackedCoinsPanel from './components/TrackedCoinsPanel';

function App() {
  const [tab, setTab] = useState(0);

  const handleTabChange = (event: React.SyntheticEvent, newValue: number) => {
    setTab(newValue);
  };

  return (
    <div>
      <Tabs value={tab} onChange={handleTabChange}>
        <Tab label="Ayarlar" />
        <Tab label="İzlenen Coinler" />
      </Tabs>
      {tab === 0 && <SettingsPanel />}
      {tab === 1 && <TrackedCoinsPanel />}
    </div>
  );
}

export default App;