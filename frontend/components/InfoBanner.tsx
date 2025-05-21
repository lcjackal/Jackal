import React from "react"
export function InfoBanner() {
  return (
    <div style={{ background: "#eef9fc", border: "1px solid #b4e3e6", padding: 8, marginBottom: 10, borderRadius: 6, fontSize: 14 }}>
      <b>Tespit Edilen Hareketler:</b> Emir defteri, hacim, teknik göstergeler, zincir üstü, balina hareketleri ve piyasa duyarlılığı gibi tüm kaynaklardan elde edilen hareketler burada listelenir.
      <br />
      <b>Potansiyel Fırsatlar Paneli:</b> Algoritmanın en güçlü bulduğu fırsatlar hızlıca özetlenir. Kaynaklar algoritmanın içinde ağırlıklandırılır, gereksiz detay gösterilmez.
      <br />
      <b>Not:</b> Vadeli işlemler ve balina verileri gibi gelişmiş piyasa kaynakları algoritmanın içinde dikkate alınır, fakat kullanıcıya ayrı panel/grafik olarak gösterilmez.
    </div>
  )
}