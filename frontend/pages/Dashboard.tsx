// ... önceki kodlar ...
<header>
  <button onClick={() => setShowSettings(x => !x)}>⚙️ Ayarlar</button>
  <button onClick={() => setShowHelp(x => !x)}>❓ Yardım</button>
</header>
{showHelp && <HelpPanel onClose={() => setShowHelp(false)} />}