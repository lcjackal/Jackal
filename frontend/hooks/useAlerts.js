// Uyarı spam'ini engelle (ör: son 5dk da aynı tipten sadece bir kez göster)
import { useRef } from "react"
export function useAlerts() {
  const [alerts, setAlerts] = useState([])
  const lastAlertTimes = useRef({})
  function addAlert(type, msg, timeout = 4000) {
    const now = Date.now()
    if (lastAlertTimes.current[msg] && (now - lastAlertTimes.current[msg]) < 5 * 60 * 1000) return
    lastAlertTimes.current[msg] = now
    const id = Math.random().toString(36).substr(2, 9)
    setAlerts(alerts => [...alerts, { id, type, msg }])
    if (timeout)
      setTimeout(() => setAlerts(alerts => alerts.filter(a => a.id !== id)), timeout)
  }
  function removeAlert(id) {
    setAlerts(alerts => alerts.filter(a => a.id !== id))
  }
  return { alerts, addAlert, removeAlert }
}