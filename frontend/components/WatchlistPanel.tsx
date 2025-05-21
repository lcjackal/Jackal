// ... önceki kodlar ...
function addCoin() {
  if (!input.trim()) return
  setLoading(true)
  fetch("/api/watchlist/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ coin: input.trim().toUpperCase() })
  })
    .then(r => r.json())
    .then(d => {
      setLoading(false)
      if (d.ok) {
        setCoins(d.coins)
        setInput("")
        setMsg("")
        onChange && onChange(d.coins)
      } else {
        setMsg(d.msg)
      }
    })
    .catch(e => {
      setLoading(false)
      setMsg("Sunucuya erişilemiyor.")
    })
}