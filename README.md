# Küçük İşletmeler İçin Python/Flask ile Oluşturulmuş Modern Web Sitesi

Bu proje, küçük işletmeler için modern, responsive ve şık bir web sitesi oluşturmak amacıyla Flask, Bootstrap, HTML, CSS ve JavaScript kullanılarak geliştirilmiştir. Uygulama; hero, hakkımızda, hizmetlerimiz ve iletişim bölümlerini içerir.

- **Responsive Tasarım:** Bootstrap kullanılarak her cihazda uyumlu görünüm.
- **Yapışkan (Sticky) Navbar:** Sayfa her kaydırıldığında menü görünür kalır.
- **Hero Bölümü:** Arka plan görseli ve overlay ile dikkat çekici giriş ekranı.
- **Hakkımızda Bölümü:** Sol tarafta görsel (üzerine gelindiğinde fade out efekti) ve sağ tarafta metin.
- **Hizmetlerimiz Bölümü:** İki satırda toplam 6 hizmet kutucuğu; her kutucukta bir görsel ve hizmet adı, hover durumunda kutucuğun hafifçe büyümesi.
- **İletişim Bölümü:** Form aracılığıyla kullanıcı mesajlarının alınması.

## Kurulum

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/bektas-sari/flask-kucuk-isletme-sitesi.git
   cd flask_modern_site

Sanal Ortam Oluşturun (Opsiyonel ama önerilir):
python3 -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

Gerekli Paketleri Yükleyin:
pip install -r requirements.txt
Not: Eğer bir requirements.txt dosyanız yoksa, en azından Flask kurulmalıdır. Örneğin:
pip install Flask

Uygulamayı Çalıştırın:
python app.py

Tarayıcıda Açın:
http://127.0.0.1:5000

Kullanım
Navigasyon: Yapışkan navbar sayesinde, sayfanın üstündeki "Anasayfa", "Hakkımızda", "Hizmetlerimiz" ve "İletişim" linklerine tıklayarak sayfa içerisinde ilgili bölümlere hızlıca geçiş yapabilirsiniz.
Animasyonlar: Buton fade in animasyonu, görsel hover efektleri (fade out ve büyüme) ile zenginleştirilmiş kullanıcı deneyimi.

Özelleştirme
İçerik Güncelleme: Metinler ve görseller app.py ve templates/ içerisindeki HTML dosyalarından kolayca düzenlenebilir.
Stil Düzenlemeleri: CSS kodları static/css/style.css dosyasında bulunmakta; burada stil ve animasyon ayarlarını değiştirebilirsiniz.
Görseller: static/images/ klasöründeki dosyaları değiştirerek kendi görsellerinizi kullanabilirsiniz.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

Katkıda Bulunma
Katkılarınızı memnuniyetle karşılıyoruz! Hata bildirimi, özellik önerileri veya doğrudan katkı için lütfen bir issue oluşturun veya pull request gönderin.

İletişim
Herhangi bir soru veya geri bildirim için lütfen bektas.sari@gmail.com adresinden iletişime geçin.
