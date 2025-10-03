# Akıllı Şehir Tasarımı — Prompt Teknikleri Karşılaştırma

## 1. Skeleton-of-Thought (SoT)
**System:** Önce kısa iskelet ver, sonra detayları aç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Ulaşım  
- Enerji  
- Çevre  
- Sağlık  
- Güvenlik  
**Detaylar:** Her başlık altında 3-4 cümle detaylı açıklama.

---

## 2. Least-to-Most (LtM)
**System:** Önce en basit alt görevleri çöz, sonra daha karmaşık olanları.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
1. LED sokak lambaları  
2. Akıllı trafik ışıkları  
3. Entegre yönetim sistemi  

---

## 3. Step-Back Prompting
**System:** Önce geniş bakış açısı ile değerlendir, sonra çözüm ver.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
**Genel Bakış:** Yaşam kalitesini artırmak, sürdürülebilirlik sağlamak.  
**Çözümler:** Ulaşım entegrasyonu, yenilenebilir enerji, veri odaklı planlama.

---

## 4. Plan-and-Solve (PS)
**System:** Önce planı çıkar, sonra uygulamaya başla.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
**Plan:** Ulaşım, Enerji, Çevre, Vatandaş hizmetleri  
**Uygulama:**  
- Ulaşım: Akıllı duraklar, otonom otobüsler  
- Enerji: Güneş panelleri, akıllı sayaçlar  

---

## 5. Decomposed Prompting
**System:** Görevi alt parçalara ayır, her parçayı ayrı çöz.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Ulaşım: Bisiklet yolları, scooter ağı  
- Enerji: Güneş ve rüzgâr kaynakları  
- Çevre: Atık robotları, hava sensörleri  
- Sağlık: Tele-sağlık merkezleri  
- Güvenlik: Akıllı kamera sistemleri  

---

## 6. Recursive Thought Decomposition (RTD)
**System:** Görev genişse alt başlıklara böl, gerekirse onları da ayır.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Ulaşım → toplu taşıma (otobüs, metro), özel araç (elektrikli altyapı, trafik optimizasyonu)  
- Enerji → yenilenebilir (güneş, rüzgâr), akıllı şebeke  
- Çevre → atık yönetimi, su tasarrufu  
- Sağlık → dijital kayıt, uzaktan müdahale  

---

## 7. Tree-of-Thoughts (ToT)
**System:** Farklı çözüm yolları üret, sonra en uygununu seç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Yol 1: Ulaşım ağı  
- Yol 2: Enerji verimliliği  
- Yol 3: Vatandaş katılımı  
**Seçim:** Yol 2  

---

## 8. Auto-CoT
**System:** Önce kendi düşünce zincirini kur, sonra yanıtı ver.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Zincir: Sorunlar → trafik, enerji, çevre  
- Çözümler: Akıllı duraklar, güneş panelleri, çevresel sensörler  
**Sonuç:** Entegre ulaşım, yenilenebilir enerji, sensörler  

---

## 9. MODP
**System:** Hem kullanıcı isteğini hem uygulanabilirliği gözet.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Trafik sıkışıklığını %30 azaltacak sistem  
- Enerji tüketimini %20 düşürecek sayaçlar  
- Atıkların %40’ını geri dönüştürecek düzen  

---

## 10. APEER
**System:** Farklı prompt varyasyonları üret, en iyisini seç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- V1: Enerji-ulaşım-çevre odaklı  
- V2: Sağlık-güvenlik odaklı  
- V3: Bütüncül yaklaşım  
**Seçim:** V3  

---

## 11. PAL
**System:** Hesaplama içeren görevlerde kod kullan.  
**User:** 10.000 hanede %15 enerji tasarrufu sağlanırsa kaç hanede tasarruf olur?  
**Assistant:**  
`10.000 × %15 = 1.500`  
Sonuç: 1.500 hane  

---

## 12. RAG
**System:** Önce dış bilgiyi çek, sonra yanıt ver.  
**User:** Dünyada akıllı şehir örnekleri ver.  
**Assistant:**  
- Barcelona: Akıllı ışıklandırma  
- Singapur: Trafik sensörleri  
- Amsterdam: Su yönetimi  

---

## 13. Self-Consistency
**System:** Farklı çözüm yolları üret, en tutarlı sonucu seç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Çözüm 1: Enerji + ulaşım + çevre  
- Çözüm 2: Ulaşım + enerji + sağlık  
- Çözüm 3: Çevre + enerji + ulaşım  
**Sonuç:** Ortak kesişim = enerji + ulaşım + çevre  

---

## 14. Otomatik Prompt Optimizasyonu
**System:** Aynı soruya birkaç slogan üret, en iyisini seç.  
**User:** Akıllı şehir için slogan öner.  
**Assistant:**  
- “Geleceğin şehri bugün”  
- “Akıllı yaşam, sürdürülebilir gelecek”  
- “Teknolojiyle daha yeşil şehirler”  
**Seçim:** “Akıllı yaşam, sürdürülebilir gelecek”  

---

## 15. Self-Refine (Öz-iyileştirme)
**System:** Önce bir taslak üret, sonra kendini değerlendir ve geliştirilmiş versiyonu yaz.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **İlk taslak:** "Şehirde akıllı trafik ışıkları ve güneş panelleri kurulmalı."  
- **Geri bildirim:** "Öneriler sınırlı, çeşitlilik ve sosyal boyut eklenmeli."  
- **İyileştirilmiş taslak:** "Akıllı trafik ışıkları, güneş panelleri, akıllı atık yönetim sistemi, tele-sağlık hizmetleri ve vatandaş katılım platformlarıyla sürdürülebilir bir akıllı şehir kurulmalı."

---

## 16. Reflexion (Yansıtma / Deneyimden Öğrenme)
**System:** Her denemeden sonra hataları yazılı olarak analiz et, sonraki cevabı güncelle.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **Deneme 1:** "Trafiği azaltmak için bisiklet yolları."  
- **Yansıtma:** "Tek başına yeterli değil; enerji, çevre ve sağlık da önemli."  
- **Deneme 2:** "Bisiklet yolları, yenilenebilir enerji, akıllı sağlık sistemleri, çevre sensörleri."  

---

## 17. CRITIC
**System:** Çözüm üret, sonra kendi çözümünü eleştir ve düzelt.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **İlk öneri:** "Yalnızca akıllı ulaşım ağı kurmak."  
- **Eleştiri:** "Yalnız ulaşım odaklı, enerji ve sosyal hizmetler eksik."  
- **Düzeltilmiş öneri:** "Akıllı ulaşım ağı, yenilenebilir enerji kaynakları, akıllı güvenlik kameraları, dijital sağlık sistemleri."  

---

## 18. Self-Consistency (Çoklu Yol Tutarlılığı)
**System:** Farklı çözüm yolları üret, en çok tekrarlanan unsurları seç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Yol A: "Ulaşım + Enerji + Çevre"  
- Yol B: "Enerji + Ulaşım + Sağlık"  
- Yol C: "Çevre + Enerji + Ulaşım"  
- **Sonuç:** Ortak kesişim = **Enerji + Ulaşım + Çevre**

---

## 18. Chain-of-Verification (CoVe)
**System:** İlk cevabı yaz, doğrulama soruları oluştur ve sonuçları kontrol ederek son cevabı ver.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **İlk cevap:** "İstanbul örneğinde akıllı ışıklar ve güneş panelleri kullanılmalı."  
- **Doğrulama soruları:**  
  - "Gerçekten bu sistemler uygulanabilir mi?"  
  - "Benzer uygulamalar başka şehirlerde başarılı oldu mu?"  
- **Kontrol:** Barcelona → akıllı ışıklar, Amsterdam → su yönetimi.  
- **Sonuç:** "Akıllı ışıklar, güneş panelleri, su yönetim sistemleri ve çevre sensörleri önerilir."

---

## 19. Tree-of-Thoughts (Düşünce Ağacı)
**System:** Farklı dallar üret, her dalı değerlendir, en uygununu seç.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Dal 1: Ulaşım (otobüs, metro, bisiklet yolları)  
- Dal 2: Enerji (güneş, rüzgâr, akıllı şebeke)  
- Dal 3: Sosyal hizmetler (sağlık, güvenlik, katılım)  
- **Değerlendirme:** Dal 2 sürdürülebilirlikte güçlü, Dal 1 kısa vadede etkili.  
- **Seçim:** Dal 1 + Dal 2 kombinasyonu → "Entegre ulaşım ve enerji sistemi."

---

## 20. Auto-CoT (Otomatik Zincir-Düşünce)
**System:** Önce kendi örnek düşünce zincirlerini üret, sonra çözümü oluştur.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **Örnek Zincir 1:** Sorun = trafik → çözüm = akıllı ışık  
- **Örnek Zincir 2:** Sorun = enerji → çözüm = güneş panelleri  
- **Örnek Zincir 3:** Sorun = sağlık → çözüm = tele-sağlık  
- **Sonuç:** "Akıllı ulaşım, yenilenebilir enerji, dijital sağlık hizmetleri."

---

## 21. Critic-CoT
**System:** Her düşünce adımını yaz, ardından eleştirip gerekirse düzelt.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- Adım 1: "Akıllı trafik ışıkları."  
  - **Eleştiri:** "Tek başına yeterli değil."  
- Adım 2: "Yenilenebilir enerji altyapısı."  
  - **Eleştiri:** "Ekonomik uygulanabilirlik dikkate alınmalı."  
- Adım 3: "Sağlık ve güvenlik sistemleri."  
  - **Eleştiri:** "Kapsayıcı oldu."  
- **Sonuç:** Dengeli öneri listesi.

---

## 22. Generative Self-Refinement (Paralel Aday + Sentez)
**System:** Birden çok aday üret, sonra sentezle en iyi cevabı oluştur.  
**User:** Akıllı şehir tasarımı için öneriler geliştir.  
**Assistant:**  
- **Aday 1:** "Bisiklet yolları ve toplu taşıma."  
- **Aday 2:** "Yenilenebilir enerji ve akıllı sayaçlar."  
- **Aday 3:** "Akıllı atık toplama ve çevre sensörleri."  
- **Sentezlenmiş final:** "Akıllı ulaşım, yenilenebilir enerji, çevre dostu sistemler ve vatandaş odaklı altyapı."

---
