1. Temel / Klasik Prompt Mühendisliği Teknikleri
1.1 Zero-shot Prompting
/system
Sen, Ay kaynakları üzerine çalışan deneyimli bir stratejik analistsin.
/user
Ay'ın Güney Kutbu'ndaki su buzu rezervlerinin ticari olarak işletilmesi için ana zorluklar nelerdir?
/assistant
Ticari işletilebilirliğin önündeki ana zorluklar, yüksek enerji gereksinimi, zorlu radyasyon ortamı ve uluslararası hukuk düzenlemelerinin (Ay Anlaşması) belirsizliğidir.

1.2 Few-shot Prompting
/system
Ay kaynakları stratejisti. PSR kaynaklarını değerlendirirken aşağıdaki formatı ve analiz derinliğini takip et.
/user
Örnek 1:
Girdi: Enerji kaynağı.
Çıktı: RTG (Radyoizotop Termoelektrik Jeneratör).
Değerlendirme: Sürekli gölgede verimli, ancak pahalı ve sınırlı ömürlü.

Örnek 2:
Girdi: Hukuki Risk.
Çıktı: Ay Anlaşması ve ARMS (Artemis Anlaşmaları).
Değerlendirme: ARMS, ulusal hakları savunsa da, çıkarma hakkı net değil.

Soru: Lojistik Zorluklar.
/assistant
Çıktı: Toz ve Termal Yönetim.
Değerlendirme: Regolit tozu ekipmanları hızla aşındırır. Aşırı soğuk/sıcaklık değişimleri nedeniyle termal yönetim (ısıtma/soğutma) çok karmaşıktır.

1.3 Chain-of-Thought (CoT)
/system
Ay kaynakları uzmanı olarak, bir soruyu yanıtlamadan önce mantıksal adımlarını açıkça belirt.
/user
Ay'daki su buzu çıkarım maliyeti ile yörüngeye fırlatma maliyeti arasındaki ekonomik denge noktasını (break-even point) nasıl belirlersin? Adım adım düşün.
/assistant
Düşünce Zinciri:

Gerekli Veri Toplama: 1 ton su buzu çıkarım maliyetini (Enerji, Ekipman, İnsan gücü) ve 1 ton suyun Dünya yörüngesinden Ay yörüngesine fırlatma maliyetini belirle.

Kullanım Senaryosu: İtibari para yerine "Ay kaynaklı yakıt"ın (propellant) ekonomik değerini hesapla.

Denge Noktası: Ay'da üretilen yakıtın, Dünya'dan gelen yakıttan daha ucuza mal olduğu noktayı belirle. Bu, özellikle Ay yörüngesi hizmetleri için kritik.
Cevap: Denge noktası, operasyonel verimlilik ve Dünya'dan fırlatılan yakıtın maliyet/ton oranı temel alınarak hesaplanır ve şu anda tahmini X/ton civarındadır.

1.4 Tree-of-Thoughts (ToT)
/system
Ay'ın güney kutbu yerleşimi için 3 farklı stratejik risk analizi yap. Her risk için 3 farklı potansiyel hafifletme yolunu (thought) değerlendir ve her yolu "Yüksek Risk", "Orta Risk" veya "Düşük Risk" olarak derecelendir. En iyi yolu seç.
/user
Ana jeolojik risk: Regolit tozunun ekipman üzerindeki aşındırıcı etkisi. Çözüm stratejileri neler olmalıdır?
/assistant
Aşama 1: Düşünce Üretimi (Kök)

Düşünce 1: Elektrostatik toz giderme sistemleri kullan. (Derece: Orta Risk)

Düşünce 2: Tüm hareketli parçaları hermetik olarak kapat. (Derece: Yüksek Risk)

Düşünce 3: Kısmen otonom, hızlı değiştirilebilir modüller geliştir. (Derece: Orta Risk)

Aşama 2: Değerlendirme ve Dallanma (Düşünce 3'ten İleriye)

Düşünce 3.1: Otonom modüllerin maliyeti ve ağırlık optimizasyonu. (Yeni Derece: Düşük Risk)

Düşünce 3.2: Değiştirilebilir modüller için yerinde 3D baskı imkanı. (Yeni Derece: Orta Risk)

Nihai Seçim: En iyi yol, otonom modüllerin kullanımı (Düşünce 3.1) ile aşınma riskini minimize etmektir.

1.5 Graph-of-Thoughts (GoT)
/system
PSR-RM raporunun "Hukuksal Risk" ve "Mali Risk" kısımlarını sentezleyerek tek bir "Jeopolitik Fizibilite Kararı" üret.
/user
Düşünce 1 (Hukuksal): Ay Anlaşması, PSR kaynaklarının ortak miras olduğunu öne sürer.
Düşünce 2 (Mali): Su buzu çıkarımının başlangıç maliyeti 10 milyar USD'dir.
Sentez Talimatı: Düşünce 1 ve Düşünce 2'yi birleştirerek (AGGREGATION) hukuki engellerin yüksek maliyetle nasıl etkileştiğini analiz et.
/assistant
Düşünce 3 (Sentez/Aggregation):
Hukuki Risk (1) ve Mali Risk (2)'nin birleşimi: Başlangıç yatırımının (10 Milyar USD) yüksek olması, uluslararası hukuki belirsizlik (ortak miras) nedeniyle yatırım riskini katlanarak artırır. Hukuki netlik sağlanmadan bu ölçekte bir yatırım yapılamaz.

2. Akıl Yürütme ve Planlama Odaklı Teknikler
2.1 Skeleton-of-Thought (SoT)
/system
Ay'daki kriyojenik yakıt depolarının tasarım zorlukları üzerine bir rapor hazırlayacaksın. Önce 5 maddelik kısa bir iskelet (3-5 kelime) oluştur. Ardından, iskeletin 3. maddesini detaylandır.
/user
Soru: Ay yakıt depolarında sıvı oksijenin buharlaşmasını nasıl önleriz?
/assistant
İskelet:

Termal katmanlama kritik.

Pasif soğutma şart.

Sıvı kaybı minimalize et.

Kriyosoğutucu entegrasyonu.

Gölgeleme yapıları kullan.

Detaylandırma (Madde 3): Sıvı Kaybı Minimalize Et
Sıvı kaybı (boil-off), depolama basıncını kontrol ederek ve termal yalıtımı optimize ederek minimalize edilebilir. Özellikle "Zero Boil-Off" (ZBO) teknolojileri, pasif (çok katmanlı yalıtım) ve aktif (kriyosoğutucular) yöntemleri birleştirerek buharlaşmayı sıfıra indirmeyi hedefler.

2.2 Algorithm-of-Thoughts (AoT)
/system
Ay görevleri için su talebi planlaması yapacaksın. Çözümü adım adım algoritmik mantıkla üret.
/user
Görev: 4 astronot, 60 gün, günlük 5 litre su tüketimi. Geri dönüştürme verimliliği %90. İlk stok kaç litre olmalıdır?
/assistant
AoT Algoritması:

Toplam Brüt Tüketim (TBT) hesapla: 4 astronot×60 g 
u
¨
 n×5 L/g 
u
¨
 n=1200 L.

Geri Dönüşüm Miktarı (GDM) hesapla: 1200 L×0.90=1080 L.

Net Tüketim (NT) hesapla: TBT−GDM=1200 L−1080 L=120 L.

Güvenlik Payı (GP) ekle (%25): 120 L×1.25=150 L.
Cevap: Görev için gerekli minimum ilk su stoğu 150 litredir.

2.3 Least-to-Most Prompting (LtM)
/system
Ay Üssü İnşaat planlaması. Görevi A, B, C adımlarıyla çöz. Adım A'nın çıktısını B'ye girdi olarak kullan.
/user
Adım A: Bir ISRU (In-Situ Resource Utilization) tesisi, 1 ayda kaç ton regolit işlemesi gerekir ki, 100 kg oksijen üretilebilsin? (Veri: Regolit oksijen verimi %0.5)
/assistant
Adım A Çözüm: 100 kg Oksijen/0.005=20,000 kg=20 ton. ISRU tesisi 1 ayda 20 ton regolit işlemelidir.

/user
Adım B (Girdi: 20 ton): 20 ton regolit işlemek için gereken güç (kW) nedir? (Veri: 1 ton regolit için 500 kWh enerji gerekir).
/assistant
Adım B Çözüm: 20 ton×500 kWh/ton=10,000 kWh. 1 aylık operasyon için 10,000 kWh enerji gerekir.

2.4 Step-Back Prompting
/system
Önce kullanıcının sorusunun temelini oluşturan bilimsel prensibi (step-back question) belirle. Ardından, bu prensibi kullanarak orijinal soruyu yanıtla.
/user
PSR içindeki bir robotun termal yönetimi için gereken minimum termal albedo değeri nedir?
/assistant
Step-Back Abstraction: Termal yönetimi etkileyen temel fizik yasaları nelerdir? (Stefan-Boltzmann Yasası, ısı transferi prensipleri).
Nihai Cevap: PSR ortamında, robotun termal yönetimi için kritik olan şey, radyatif kayıpları dengelemektir. Minimum termal albedo değeri (genellikle 0.8-0.9 aralığında istenir), yüzeyin güneş ışığını yansıtma kapasitesini maksimize etmeli, ancak PSR içinde temel soğutma prensipleri (radyatif soğutma) geçerli olmalıdır...

2.5 Plan-and-Solve Prompting (PS)
/system
PSR-RM raporunun "Risk Analizi" bölümünü oluşturacaksın. Önce 3 adımlı bir plan yap, sonra planı takip et.
/user
Görev: Ay madenciliğinin çevresel etkileri üzerine bir risk analizi yap.
/assistant
Plan:

Etki Tespiti: Regolit çıkarma ve işleme operasyonlarının yaratacağı toz ve sismik etkileri listele.

Hafifletme Stratejileri: Bu etkileri azaltacak teknolojik çözümleri (örneğin Toz Yakalama) araştır.

Risk Matrisi: Kalan riskleri olasılık ve etki açısından matrise yerleştir.

Çözüm (Planı Takip Ederek): Regolit çıkarma, özellikle toz bulutları oluşturarak optik sensörleri ve yüzey ekipmanlarını kirletme potansiyeli taşır. Hafifletme stratejileri arasında elektrostatik toz toplayıcılar ve manyetik ayırıcılar bulunur. Kalan risk, Orta Olasılık ve Yüksek Etki olarak değerlendirilebilir.

2.6 Decomposed Prompting
/system
Ay'da inşa edilecek bir nükleer reaktörün güvenlik protokollerini üç alt başlıkta böl: Yer Seçimi, Radyasyon Koruması ve Acil Durum Kapatma.
/user
Ay'da reaktör güvenliği.
/assistant

Yer Seçimi: Kalıcı yerleşim yerlerinden kilometrelerce uzakta, tercihen doğal krater duvarlarının arkasına yerleştirilmeli, böylece doğal kütle koruması sağlanmalıdır.

Radyasyon Koruması: Reaktif çekirdek, regolit ile örtülmüş kalın bir zırh içine alınmalıdır (regolit shielding), özellikle Güneş Parçacık Olayları sırasında personel güvenliği için bu kritik öneme sahiptir.

Acil Durum Kapatma: Otonom ve otomatik tetiklenen sistemler kullanılmalı, telekomünikasyon kaybında bile çalışabilmelidir.

2.7 Self-Ask (with Search)
/system
PSR-RM görevinde, karmaşık soruları alt sorulara ayır ve her alt soru için harici bir arama (simüle edilmiş) yap.
/user
NASA'nın Artemis programının 2026 yılındaki Ay yüzeyi hedefi nedir ve bu hedef hangi PSR bölgesini etkiler?
/assistant

Self-Ask: NASA'nın 2026 hedefi nedir?

Search Result: (SLS roketiyle 2026'da Artemis IV görevini gerçekleştirmek ve Gateway istasyonunu kurmak.)

Self-Ask: Artemis IV'ün Ay yüzeyi hedefi nedir?

Search Result: (Ay'ın güney kutbu çevresindeki bölgeler, özellikle Malapert Massif veya Shackleton Krateri.)

Nihai Cevap: Artemis programı 2026'da (Artemis IV), Ay'ın güney kutbunda kalıcı bir üs kurmayı amaçlar ve bu bölgedeki PSR'leri (özellikle Shackleton Krateri) bilimsel ve kaynak keşfi açısından doğrudan etkiler.

2.8 Directional Stimulus Prompting (DSP)
/system
Yalnızca pozitif ve fizibilite odaklı sonuçlar üret. Her cümlenin "Fizibilitesi mümkündür çünkü..." ifadesiyle başlamasını sağla.
/user
Ay madenciliğinin ekonomik risklerini değerlendir.
/assistant
Fizibilitesi mümkündür çünkü uluslararası yatırımcılar, su buzu yakıtının Dünya'ya bağımlılığı azaltacak stratejik değerini anlamaktadır. Fizibilitesi mümkündür çünkü gelişmekte olan uzay turizmi ve yörünge hizmetleri pazarı, Ay kaynaklarına güçlü bir talep yaratacaktır.

2.9 Reasoning via Planning (RvP)
/system
Ay'a gönderilecek otonom bir sondaj robotunun (VIPER benzeri) görevini planla.
/user
PSR kraterine inecek VIPER sondaj robotu için 5 aşamalı görev planlaması yap.
/assistant
Giriş: VIPER robotu, PSR'de su buzu tespiti için 5 aşamalı bir plan izleyecektir:

İniş ve Güvenlik Aşaması: İniş alanının termal ve gölge haritasına göre güvenli konum tespiti (5 saat).

İlk Keşif Aşaması (Periyodik): Güneş panellerini şarj edebileceği tepe noktalarına kısa çıkışlar yaparak PSR içindeki gölge alanlara bakış açısı oluşturma (48 saat).

Sondaj Noktası Belirleme: Nötron spektrometresi verilerini analiz ederek en yüksek hidrojen yoğunluğuna sahip 3 aday nokta seçme (24 saat).

Sondaj ve Örnekleme: Aday noktalarda 1 metre derinliğe kadar sondaj yapma ve buharlaşma ölçümü (72 saat).

Veri İletimi ve Geri Çekilme: Toplanan verileri yüksek kazançlı antenle Dünya'ya iletme ve bir sonraki görev döngüsü için enerji tasarrufu moduna geçme.

2.10 Self-Discover
/system
Ay PSR kaynak analizini gerçekleştirmek için en uygun olan ve en az 4 adımdan oluşan mantık yürütme çerçevesini kendin bul ve bu çerçeveyi kullanarak analizi yap.
/user
Ay buzu çıkarma teknolojilerini sınıflandır.
/assistant
Kendinden Keşfedilen Çerçeve:

Termal Çıkarma Metotları (Avantaj/Dezavantaj).

Mekanik Çıkarma Metotları (Avantaj/Dezavantaj).

Hibrid Sistemler ve Enerji Verimliliği.

En Uygun Alan Uygulaması.

(Çerçeve Uygulaması):

Termal Metotlar: Mikrodalga veya güneş yoğunlaştırma (çok hızlı süblimleşme sağlar, enerji yoğunluğu yüksektir). Dezavantajı: Kriyojenik sıvı yönetimi karmaşıktır.
...

2.11 Quiet-STaR
/system
Cevabı vermeden önce, her adımda yaptığın analizi {SESSİZ DÜŞÜNCE:...} etiketiyle dahili olarak üret, ancak bu etiketi çıktıda gösterme. Ardından sadece nihai sonucu yayınla.
/user
Ay'daki radyasyon koruma gereksinimlerini kısaca özetle.
/assistant
{SESSİZ DÜŞÜNCE: Ay yüzeyinde iki ana radyasyon türü vardır: Galaktik Kozmik Işınlar (GCR) ve Güneş Parçacık Olayları (SPE). GCR'ler sürekli ve zorludur, SPE'ler seyrektir ama yoğun ve hızlı koruma gerektirir. Çözüm, kütle koruması (regolit shielding) ve yer altı yerleşimidir.}
Cevap: Ay yüzeyinde, sürekli GCR'ler ve ani SPE'lere karşı korunmak için öncelikle regolit kütle koruması ve yeraltı veya krater içi yerleşimler zorunludur.

2.12 Dense Thought Prompting (DTP)
/system
PSR-RM raporunun teknolojik kısıtlamalar bölümünü yazarken, her mantık adımını (thought) maksimum 50 kelime ile çok yoğun ve teknik terimlerle ifade et.
/user
Ay'daki kriyojenik sıvıların pompalanması ve transferi neden zordur?
/assistant
Yoğun Düşünce: Kriyojenik sıvı transferi, sıfır yerçekimi/düşük yerçekimi ve aşırı sıcaklık gradyanları nedeniyle faz geçişi riskini barındırır. Özellikle "slosh" (sarsıntı) ve buhar kabarcığı oluşumu (cavitation), pompaların verimini düşürür ve hassas valf kontrolü gerektirir. Sızdırmazlık malzemeleri Ay'ın vakumunda hızla bozulur, bu da ultra-güvenilir sızdırmazlık tasarımlarını zorunlu kılar.

2.13 Recursive Thought Decomposition (RTD / RoT / RDoLT)
/system
PSR kaynaklarının uzun vadeli stratejisi üzerine bir analiz yap. Analizi 3 ana bölüme ayır. Ardından, ilk ana bölümü (Hukuksal Çerçeve) 3 alt bölüme ayır.
/user
Uzun Vadeli PSR Kaynak Stratejisi
/assistant
I. Hukuksal ve Yönetim Çerçevesi

I.A. Uluslararası Hukukun Mevcut Durumu (Ay Anlaşması/Artemis Mutabakatları).

I.B. Kaynak Çıkarma Ruhsatlandırma Mekanizmaları.

I.C. Uygulama ve İhlal İzleme.

II. Ekonomik Fizibilite ve Pazar Tahmini

II.A. Yörünge Yakıt Pazarı Büyüklüğü.

II.B. Hammadde Maliyet Eğrileri.

II.C. Yatırım Geri Dönüş Süresi.

III. Teknik Risk Yönetimi ve İSG

3. Öz-Eleştiri, Doğrulama ve İteratif İyileştirme Teknikleri
3.1 Self-Refine
/system
Ay kaynakları politikası üzerine bir taslak yaz. Ardından, bu taslağı eleştir ve eleştirine göre iyileştir.
/user
Taslak: Ay'daki su buzu, herhangi bir ulusa ait olmamalıdır ve tüm insanlığın ortak mirası olmalıdır. Bu kaynaklar, bilimsel araştırma için kullanılmalıdır.
/assistant
Aşama 1: Geri Bildirim (FEEDBACK):
Taslak, politik olarak idealisttir ancak güncel Artemis Mutabakatları (ARMS) ile çelişmektedir. "Ortak miras" yaklaşımı, ticarileşmeyi durdurur ve yatırım motivasyonunu kırar. Geri bildirim: Taslağa, ulusal çıkar ve ticarileşme motivasyonunu yansıtan bir dengeleyici ekle.
Aşama 2: İyileştirme (REFINE):
Ay'daki su buzu, uluslararası anlaşmaların (Ay Anlaşması) ruhuna uygun olarak tüm insanlığın yararına olmalıdır, ancak Artemis Mutabakatları çerçevesinde ulusal veya ticari kurumların bu kaynakları çıkarma hakkı yasal bir çerçeveye oturtulmalıdır.

3.2 Self-Correction
/system
Aşağıdaki teknik cevabı kontrol et. Hatalı veya eksik bilgi varsa düzelt ve gerekçesini belirt.
/user
Yanıt: Ay yüzeyindeki PSR'lerin sıcaklığı -200°C'dir ve bu sıcaklıkta su doğrudan sıvı faza geçer.
/assistant
Düzeltme: Yanıt hatalıdır. -200°C (-328°F) sıcaklıkta su katı haldedir (su buzu). Vakum koşullarında su, katı halden doğrudan gaz hale (süblimleşme) geçer; sıvı faza geçmez. Gerekçe: Ay'da sıvı suyun var olmasını sağlayan atmosfer basıncı yoktur.

3.3 Reflexion
/system
Ay robotu görev ajanı. Son başarısız denemenin öz-yansımasını (self-reflection) yaz ve sonraki planı oluştur.
/user
Önceki Hata Özeti: Sondaj robotu 1.5 metreye ulaştığında, motor aşırı ısınma nedeniyle durdu. Sebep: Regolit tozunun aşırı sürtünmesi.
/assistant
Öz-Yansıma (Reflection): Önceki görevde, PSR içindeki regolit yoğunluğunun tahmin edilenden yüksek olduğu gözlemlendi. Aşırı sürtünme, termal yükü artırarak motorun durmasına neden oldu. Gelecek denemeler için çıkarım: Sondaj hızını %50 düşürerek aşırı ısınmayı önle ve her 0.5 metrede bir motor soğutma döngüsü ekle.
Yeni Plan Başlangıcı: Sondaj hızını kısıtla ve otomatik soğutma döngülerini entegre et.

3.4 CRITIC
/system
Bir nükleer reaktör tasarımının enerji verimliliği hesaplamasını yap. Ardından bu hesaplamayı, termodinamik prensiplerine göre kritik et.
/user
Reaktör Verimliliği: %35.
/assistant
Eleştiri (CRITIC): %35 verimlilik, yeryüzü termal reaktörleri için standart olsa da, Ay'ın düşük yerçekimi ve kriyojenik ortamı, ısı transferi ve atık ısı yönetimi zorluklarını artırır. Ay ortamında ideal Carnot verimliliğine yaklaşmak daha zordur. Bu nedenle, %35 verimlilik hedefi, Ay'a özgü radyatör sistemlerinin kütle ve soğutma zorlukları göz önüne alındığında iyimser olabilir. Revizyon: Ay'a özgü radyatör sistemlerinin kütle ve soğutma zorlukları detaylandırılmalı.

3.5 Self-Consistency (SC)
/system
Aşağıdaki soruyu çözmek için üç farklı mantık zinciri (CoT) üret. Ardından üç sonucun ortak olanını seç.
/user
Ay'daki bir habitatın, 3.5 yıl boyunca 4 kişilik bir ekibi beslemek için (ICU – In-Situ Crop Unit) kaç metrekare tarım alanı gerekir? (Veri: 1 kişi için 10 metrekare, 1 yıl).
/assistant
Çözüm Yolu 1 (Zincir): 4 ki 
s
¸
​
 i×3.5 yıl=14 ki 
s
¸
​
 i-yıl. 14 ki 
s
¸
​
 i-yıl×10 m 
2
 /ki 
s
¸
​
 i-yıl=140 m 
2
 . Sonuç: 140 m 
2
 
Çözüm Yolu 2 (Zincir): Yıllık toplam alan ihtiyacı: 4 ki 
s
¸
​
 i×10 m 
2
 =40 m 
2
 . Toplam süre: 3.5 yıl. 40 m 
2
 ×3.5=140 m 
2
 . Sonuç: 140 m 
2
 
Çözüm Yolu 3 (Zincir): 1 kişilik ihtiyaç 3.5 yılda 35 m 
2
 . Toplam 4 kişi: 4×35 m 
2
 =140 m 
2
 . Sonuç: 140 m 
2
 
Tutarlı Nihai Cevap: Üç yol da 140 metrekarelik bir tarım alanı gerektiği konusunda tutarlıdır.

3.6 Chain-of-Verification (CoVe)
/system
Ay'daki ticari bir operasyon hakkında bir iddia üret. Ardından bu iddiayı doğrulamak için 3 doğrulama sorusu oluştur ve yanıtla.
/user
İddia: Ay'da platin grubu metallerinin çıkarılması (madencilik) ekonomik olarak fisibldır.
/assistant
Doğrulama Soruları (CoVe):

Soru 1: Ay'ın regolitinde platin grubu metal (PGM) konsantrasyonları nedir? (Yanıt: Düşük, ancak K-P Sınırı gibi bölgelerde yoğunlaşma mevcut.)

Soru 2: Ay'daki PGM'lerin çıkarım maliyeti, Dünya piyasası fiyatını karşılar mı? (Yanıt: Şu anki teknolojiyle hayır, fırlatma maliyeti çok yüksek.)

Soru 3: PGM'lerin uzay endüstrisindeki (Ay/Mars) potansiyel değeri nedir? (Yanıt: Uzay içi imalat için kritik bileşenlerdir, dolayısıyla uzayda bir pazarı oluşabilir.)
Nihai Sonuç: PGM madenciliği şu anda Dünya'ya ihracat için fizibl değildir, ancak gelecekteki Ay ve Mars yerleşimleri için yerel bir pazarı varsa potansiyel kazanır.

3.7 Multi-Agent Debate (MAD) / Socratic self-play
/system
PSR-RM projesi için iki karşıt görüşlü ajan oluştur: Ajan A (Maliyeti Savunur) ve Ajan B (Jeopolitik Riski Savunur). İki ajanın 3 tur tartışmasını kaydet.
/user
Ay yerleşiminin temel engeli nedir?
/assistant
Tur 1:

Ajan A (Maliyet Uzmanı): Temel engel, PSR'lerde enerji üretmenin muazzam maliyetidir. (Gerekçe: RTG'lerin ve nükleer reaktörlerin yüksek başlangıç sermayesi.)

Ajan B (Hukuk Uzmanı): Hayır. Temel engel, çıkarılan kaynakların mülkiyeti konusunda uluslararası bir uzlaşmanın olmamasıdır. Bu, yatırımcıyı caydırır. (Gerekçe: Uluslararası çatışma riski.)
Tur 2:

Ajan A: Maliyet düşürülebilir (örneğin nükleer fisyon reaktörleri seri üretimiyle), ancak hukuki belirsizlik sıfır tolerans gerektirir.

Ajan B: Hukuki belirsizlik, yatırım geri dönüşünü engelleyen en büyük mali risktir.
Nihai Konsensüs: Ay yerleşiminin temel engeli, operasyonel maliyetlerin yüksekliği ile uluslararası hukuki belirsizliklerin birleşimi nedeniyle ortaya çıkan yüksek yatırım riskidir.

4. Araç Entegrasyonu ve Ajan Tabanlı Yaklaşımlar
4.1 ReAct (Reasoning + Acting)
/system
PSR kaynak yönetimi ajanı. Harici Arama (Search) aracını kullan.
/user
Ay'ın yüzeyindeki ortalama regolit yoğunluğu nedir ve bu, sondaj ekipmanını nasıl etkiler?
/assistant
Thought 1: Önce Ay regoliti ortalama yoğunluğunu bulmalıyım.
Action 1: Search[Ay regoliti ortalama yoğunluğu]
Observation 1: (Gözlem: Ay yüzeyi regoliti yoğunluğu 1.5 g/cm 
3
 −1.9 g/cm 
3
  arasında değişir.)
Thought 2: Yoğunluk verisine sahibim. Şimdi bu yoğunluğun sondaj ekipmanına etkisini analiz etmeliyim (aşınma ve güç gereksinimi).
Action 2: Search
Observation 2: (Gözlem: Yüksek yoğunluk ve aşındırıcı silikat yapısı, matkap ucu ömrünü 10 kata kadar kısaltır.)
Thought 3: Cevabı sentezleyebilirim.
Action 3: Finish[Ay regoliti yoğunluğu 1.5 g/cm 
3
 −1.9 g/cm 
3
  olup, yüksek aşındırıcı yapısı nedeniyle sondaj ekipmanlarının ömrünü önemli ölçüde kısaltır ve artırılmış tork gerektirir.]

4.2 PAL (Program-Aided Language Models) / PoT (Program-of-Thoughts)
/system
Sadece Python kodu üretecek ve çıktıyı hesaplamak için bu kodu harici bir yorumlayıcıda çalıştıracaksın.
/user
Ay yörüngesinde (LEO) konuşlandırılacak bir yakıt deposu için 1 ton su buzu yakıt üretmek gerekiyor. Elektroliz için 50 MWh enerji gereklidir. Bu enerjiyi sağlamak için 2 kW'lık güneş panelleri ne kadar süre çalışmalıdır?
/assistantpython

Gerekli toplam enerji (MWh cinsinden)
E_gerekli_MWh = 50.0

Güneş paneli gücü (kW cinsinden)
P_panel_kW = 2.0

Gerekli enerjiyi Wh cinsine çevir
E_gerekli_Wh = E_gerekli_MWh * 1000

Gerekli çalışma süresi (saat)
t_saat = E_gerekli_Wh / P_panel_kW

Gün sayısına çevir
t_gun = t_saat / 24

print(f"Gerekli Çalışma Saati: {t_saat:.2f} saat")
print(f"Gerekli Çalışma Günü: {t_gun:.2f} gün")

Çıktı (Yorumlayıcıdan Gelen): Gerekli Çalışma Saati: 25000.00 saat. Gerekli Çalışma Günü: 1041.67 gün.
4.3 Toolformer
/system
PSR-RM raporunda, gerekli tarihsel verileri almak için <Calculator> ve <Search> araçlarını kullan.
/user
Apollo 11 iniş tarihi ile Artemis 3 tahmini iniş tarihi arasında kaç yıl vardır?
/assistant
Apollo 11 iniş tarihi 20 Temmuz 1969'dur. Artemis 3'ün tahmini iniş tarihi ise Eylül 2026'dır.
Fark: (YılFarkı(2026, 1969)) 57 yıl.

4.4 ReWOO (Reasoning Without Observations)
/system
PSR operasyonlarının fizibilitesini varsayımsal bilimsel ve lojistik bilgilere dayanarak analiz et.
/user
PSR içindeki yerleşim birimleri nasıl inşa edilmelidir?
/assistant
Varsayımsal Akıl Yürütme (Thought): Yerleşim birimleri zorunlu olarak yeraltı olmalıdır (radyasyon ve mikrometeorit koruması). İnşaat malzemesi yerinde üretilmelidir (ISRU). İnşaat, otonom robotlar tarafından yapılmalıdır (işgücü kısıtlaması).
Cevap: Yeraltı, regolit kalkanı ile korunan, ISRU (özellikle regolit sinterleme) ile inşa edilen otonom sistemler en fizibil yaklaşımdır.

4.5 Voyager
/system
Ay yüzeyi keşif ajanı. Görev: İlk önce basit becerilerle başla, ardından daha karmaşık beceriler gerektiren görevlere otomatik geçiş yap.
/user
Şu an Ay üssü envanterinde sadece kürek var. Yeni beceriler keşfet.
/assistant
Mevcut Beceri Kütüphanesi:

Beceri 1:  kürek ile regolit kaz 
Otomatik Müfredat (Yeni Görev Önerisi):

Gereksinim: Enerji için güneş paneli kurma (Basit Beceri).

Gereksinim: Oksijen kaynağı için regolit fırını inşa etme (Orta Beceri, <Beceri 1>'i gerektirir).

Gereksinim: Sondaj robotu montajı (Kompleks Beceri, [Oksijen kaynağı] ve [Güneş Paneli]'ni gerektirir).

5. Otomatik Prompt Tasarımı ve Optimizasyonu
5.1 Automatic Prompt Engineer (APE)
/system
Aşağıdaki giriş-çıkış çifti için en etkili Zero-Shot Prompt talimatını bul.
/user
Girdi: Ay'da su buzu çıkarmak Mars'tan daha mı kolay? Çıktı: Hayır, termal zorluklar ve aşırı gölge alanlar nedeniyle daha zordur.
/assistant
Üretilen Optimal Prompt Talimatı: "Ay ve Mars'taki ISRU operasyonlarının zorluklarını yüksek düzeyde karşılaştırarak kesin ve teknik bir yargıya var."

5.2 OPRO (Optimization by PROmpting)
/system
Ay madenciliği teknik makalesi taslağı için mevcut prompt (P0) şu şekildedir: "Ay madenciliği hakkında yaz." OPRO ajanı olarak P0'ı daha spesifik hale getirerek optimize edilmiş bir P1 promptu üret.
/user
P0: Ay madenciliği hakkında yaz.
/assistant
P1: "Ay'ın PSR bölgelerinde su buzu çıkarımının fizibilitesi üzerine odaklanarak, sadece Hukuksal ve Teknik zorlukları kapsayan, 1000 kelimelik, akademik tonda bir taslak hazırla."

5.3 Prompt Breeder
/system
Aşağıdaki iki ebeveyn promptun en güçlü özelliklerini birleştiren yeni bir "çocuk" prompt (P3) üret.
/user
P1 (Ebeveyn 1): PSR'deki radyasyon risklerini %100 koruma sağlayacak şekilde analiz et.
P2 (Ebeveyn 2): Regolit kullanımının maliyet etkinliğini araştır.
/assistant
P3 (Çocuk Prompt): PSR'deki radyasyon koruma gereksinimlerini, radyasyon kalkanı olarak regolit kullanmanın maliyet etkinliği bağlamında analiz eden fizibilite raporu hazırla.

5.4 PromptAgent / AMPO
/system
PSR kaynaklarının sürdürülebilirliği üzerine bir tartışma yürüt. PromptAgent olarak, tartışmayı sürdürmek için gerekli olan bir dizi dinamik prompt (soru) tasarla.
/user
Tartışma Konusu: PSR kaynaklarının sürdürülebilir kullanımı.
/assistant
Dinamik Prompt Serisi:

"Mevcut uluslararası yasalar, kaynak tükenme riskini nasıl adresliyor?"

"Sürdürülebilirlik için Ay’daki kaynakların sadece Ay’da kullanılması şart mıdır?"

"Ekolojik etkileri minimize etmek için en iyi madencilik tekniği nedir?"

5.5 GRIPS
/system
Ay görevinde görev planlaması için en iyi kural setini (Prompt) bulmak üzere GRIPS optimizasyonunu simüle et.
/user
Görevi Tanımla: Habitat inşası için ISRU malzemesi gereksinimini hesapla.
/assistant
GRIPS Tarafından Bulunan Kural: "ISRUTesisinin verimini dikkate al, Güvenlik payı olarak %15 fazla hesapla ve çıktıyı sadece metrik ton cinsinden ver."

5.6 ProTeGi
/system
Ay kaynakları fizibilite raporu için yüksek kalitede, karmaşık bir Few-Shot prompt template'i oluştur.
/user
Hedef: Uzun ve yapılandırılmış rapor üretimi.
/assistant
Prompt Template: "Bir Uzay Lojistik Uzmanı olarak hareket et. Aşağıdaki Hukuksal Analiz ve Lojistik Kısıtlamalar şartlarını kullanarak hedefine ulaş. Çıktıyı Giriş, Yöntem, Sonuç yapısında ver. Örnek 1:..."

5.7 TextGrad / Textual Gradients
/system
Aşağıdaki hatalı promptun (P_t) neden başarısız olduğunu analiz et ve hatayı düzelten metinsel bir gradyan (P_t+1) üret.
/user
P_t: Ay'da 3.5 yıl boyunca 4 kişiyi beslemek için kaç ton su gerekir?
/assistant
Metinsel Gradyan: P_t, suyun geri dönüşüm sistemlerini dikkate almadığı için yanıltıcıdır. Geri dönüşüm oranını (%95) dikkate alan, 'net tüketim' odaklı bir prompta ihtiyacın var.
P_t+1 (Optimize Edilmiş): "Ay'da 3.5 yıl boyunca 4 kişilik bir ekip, %95 geri dönüşüm verimliliğiyle çalışırsa, toplamda kaç ton net su takviyesine ihtiyaç duyar?"

6. Bağlam, Bellek ve Bilgi Artırımı
6.1 MedPrompt
/system
Rol: Kriyojenik Tıp Uzmanı.
Talimat: Aşırı soğuk PSR ortamında insan vücudunun metabolik tepkisini ve risklerini değerlendir.
Örnek: (PSR'de soğuk stresi altında bir astronotun kalp atış hızı ve oksijen doygunluk verileri.)
Soru: Hipotermi risklerini en aza indirmek için ne tür kıyafet/habitat tasarımları gerekir?
/assistant
Kriyojenik tıp uzmanı olarak... (Cevap, bu yapıya uygun olarak, habitat ve kıyafet tasarımları üzerine odaklanır, düşük metabolik hız riskini ve termal dengenin korunması gerektiğini vurgular.)

6.2 Active Prompting / Active In-Context Learning
/system
Ay yüzeyinde inşaat için en kritik 5 zorluğu belirleyen bir rapor yaz. Ön bilgi olarak, yüzlerce belge arasından sadece en alakalı 3 paragrafı kendin seçerek kullan.
/user
Ay İnşaat Zorlukları.
/assistant
Seçilen 3 Paragraf: (LLM tarafından en yüksek bilgi kazancına sahip 3 paragraf seçilir: 1. Toz, 2. Vakum Kaynakları, 3. Termal Gerilim.)
Cevap: (Seçilen bilgilere dayanarak raporu üretir. En kritik zorluklar, regolit tozunun yarattığı mekanik aşınma, yüksek vakumda malzeme deformasyonu ve gece/gündüz döngüsündeki aşırı termal gerilimdir.)

6.3 Generated Knowledge Prompting (GKP)
/system
PSR kaynakları hakkında bir iddia yanıtlayacaksın. Önce 3-4 cümlelik bir "Destekleyici Bilgi" üret, sonra cevabı yaz.
/user
Ay'daki su buzu, uzay yakıtı olarak kullanıma ne kadar uygundur?
/assistant
Destekleyici Bilgi (Generated Knowledge): Su buzu, elektroliz yoluyla hidrojen (yakıt) ve oksijen (oksitleyici/yaşam desteği) olarak ayrılabilir. Hidrojen, yüksek özgül itici gücü (Isp) nedeniyle uzay görevleri için idealdir. Ay'da yakıt üretimi, Dünya'dan fırlatma maliyetini ortadan kaldırır.
Cevap: Su buzu, Ay'da üretilebilen ve yörünge itki sistemlerinde kullanılabilen en uygun yakıttır. Bu durum, özellikle Ay yörüngesi operasyonlarında ve Mars görevleri için kritik bir ikmal noktası potansiyeli yaratır.

6.4 Self-RAG / Corrective RAG
/system
Ay hukuku üzerine bir soru yanıtla. Geri çağırma gerekli olup olmadığına karar ver ve cevabı üretirken kritik tokenları kullan.
/user
Artemis Mutabakatları, Ay üzerinde askeri operasyonlara izin verir mi?
/assistant
<|Retrieve|> Geri çağırma gerekli.
<|Passage 1|> Artemis Mutabakatları (ARMS), Ay'ın barışçıl amaçlarla kullanılmasını şart koşar. <|ISREL: Relevant|>
<|Passage 2|> ARMS, askeri üs kurmayı veya nükleer silah konuşlandırmayı yasaklar. <|ISREL: Relevant|>
<|Generation|> Artemis Mutabakatları, Ay'ın barışçıl amaçlarla kullanılmasını şart koşar (P1) ve askeri üsler kurmayı veya nükleer silah konuşlandırmayı açıkça yasaklar (P2). Bu, kapsamlı askeri operasyonlara izin verilmediği anlamına gelir. <|ISSUP: Supported|>

6.5 HyDE (Hypothetical Document Embedding)
/system
Ay'daki bir araştırma sorusu için önce ideal bir cevap oluştur (hipotetik belge). Ardından bu belgeyi (çıktıyı verme), yalnızca ilgili belgeleri aramak için kullan.
/user
Ay'daki kriyojenik yakıt depoları için kullanılan çok katmanlı yalıtım (MLI) malzemelerinin kompozisyonu nedir?
/assistant
Hipotetik Belge (Sadece Dahili Kullanım İçin): Ay'da kullanılan MLI (Multi-Layer Insulation) genellikle aluminize Mylar veya Kapton katmanlarından oluşur. Bu katmanlar, yayılan ısıyı minimuma indirmek için vakum ortamında ayrılmıştır.
Nihai Cevap (Aramadan Sonra): Ay yakıt depolarında ısıl radyasyonu önlemek için, genellikle aluminize Kapton veya Mylar kullanılan 20-30 katmandan oluşan, yüksek vakumda termal yalıtım sağlayan MLI sistemleri kullanılır.

6.6 RAG-Fusion
/system
Ay yerleşimleri hakkındaki en iyi bilgileri bulmak için hem vektör aramasını hem de keyword aramasını kullan (RAG-Fusion).
/user
NASA'nın LEO yörüngesinde kullanılan habitat modüllerinin iç çapı ve yaşam süresi.
/assistant
(Model, hem "LEO habitat çapı" anahtar kelimesi hem de "uzay istasyonu yaşam alanı" vektör gömülmesini kullanarak arama yapar.)
Sentezlenmiş Cevap: NASA'nın LEO yörüngesinde kullanılan habitat modüllerinin iç çapı genellikle 4.2 metre civarındadır ve modüllerin tasarlanan minimum yaşam süresi 15 yıldır. RAG-Fusion, bu bilgiyi hem nominal ölçülere (keyword) hem de operasyonel ömre (vektör) odaklanarak bulmuştur.

6.7 RAPTOR (Recursive Abstractive Processing)
/system
Ay'ın jeolojisi üzerine binlerce sayfalık bir raporda, sadece Ay toprağının toryum konsantrasyonunu bul. (RAPTOR, özetler katmanından arama yapar.)
/user
Ay regoliti içindeki toryumun ortalama konsantrasyonu nedir?
/assistant
(Model, düşük seviyeli parçalar yerine RAPTOR'un üst katmanındaki özetleri tarar.)
Özetleme Katmanı Geri Çağırma: Ay'ın Highlands bölgeleri, özellikle KREEP bileşimi bakımından zengin bölgeler (örneğin Oceanus Procellarum), diğer bölgelere göre daha yüksek toryum konsantrasyonlarına sahiptir. Ortalama konsantrasyon 1 ppm−2 ppm civarındadır.

6.8 LongRAG / Memory-augmented RAG
/system
Ay yerleşimcilerinin 5 yıllık tüm tıbbi geçmişini (uzun bağlam) kullanarak, 4. yıl sonundaki olası riskleri tahmin et.
/user
Astronot A'nın 5. yılda kemik yoğunluğu kaybı riski nedir?
/assistant
(Uzun Bağlam Yönetimi ve RAG ile) Astronot A'nın 5 yıllık görev süresi boyunca, düşürülmüş yerçekimi ve radyasyon maruziyetine bağlı olarak kemik yoğunluğunda %15'lik bir kayıp beklenmektedir. Bu risk, egzersiz rejimlerinin sürekli takviyesiyle minimalize edilmelidir.

6.9 LIMO (LLM-powered Iterative Memory Optimization)
/system
Ay üssünün lojistik hafızasını optimize et. Tekrarlanan ve gereksiz bilgileri (eski görev planları) çıkar ve sadece kritik güncel bilgileri koru.
/user
Lojistik Hafızayı Optimize Et.
/assistant
Optimize Edilmiş Hafıza: (Model, gereksiz eski planları çıkarır ve sadece envanter listeleri, kritik ekipman ömürleri ve güncel görev hedefleri gibi bilgileri tutar.)

7. Ağaç ve Arama Tabanlı Geliştirmeler
7.1 Language Agent Tree Search (LATS)
/system
Ay'daki radyasyon fırtınası sırasında habitat koruma planı için en iyi kararı bulmak üzere LATS kullan. 1000 simülasyon çalıştır.
/user
Habitat içinde mi kalmalı, yoksa yeraltı sığınağına mı geçmeli? (Sığınak yolu 15 dakika sürer.)
/assistant
LATS Analizi: (Model, MCTS'nin "keşfetme" ve "sömürme" aşamalarını simüle eder.)

Keşif: Rastgele simülasyonlar (1000 deneme)

Değerlendirme: Yüksek radyasyon seviyesinin 15 dakikalık maruziyete karşı, habitatın içeride kalma süresince sağlayacağı korumayı karşılaştır.
Nihai Karar: Sığınak yolu 15 dakika sürse bile, habitatın pasif koruması yetersiz olduğu için, sığınağa geçiş (en yüksek güvenlik payı nedeniyle) en iyi uzun vadeli karardır.

7.2 MCTS-of-Thought
/system
Ay görevleri için kaynak tahsis kararını MCTS-of-Thought ile optimize et. Kaynakları 3 farklı alana (su, oksijen, yakıt) tahsis etmenin uzun vadeli etkisini analiz et.
/user
Hangi kaynağa öncelik vermeliyiz?
/assistant
(MCTS Arama Adımları) Tahsis 1: Suya öncelik (Yüksek yaşam desteği, Orta yakıt). Tahsis 2: Yakıta öncelik (Yüksek seyahat kabiliyeti, Düşük yaşam desteği). En iyi sonuç, su ve yakıt dengesini optimize eden Tahsis 3'tür (Sömürme).

7.3 Beam-of-Thought
/system
PSR madencilik senaryosu için en iyi 5 operasyonel yolu (thought beam) keşfet ve en yüksek fizibilite skorunu alana odaklan.
/user
Hangi 5 farklı sondaj yöntemi uygulanabilir?
/assistant
Beam 1: Döner sondaj (Fizibilite: 0.8)
Beam 2: Ultrasonik sondaj (Fizibilite: 0.6)
Beam 3: Termal sondaj (Fizibilite: 0.9)
Beam 4: Lazer ablasyon (Fizibilite: 0.4)
Beam 5: Pnömatik darbeli sondaj (Fizibilite: 0.7)
En Yüksek Skorlu Yol: Termal sondaj (Beam 3), en az sürtünme ve en yüksek buz buharlaşma verimi nedeniyle en fizibil yoldur.

8. Multimodal ve Deneysel Yaklaşımlar
8.1 EmotionPrompt
/system
Bu analiz, Ay görevlerimizin başarısı için KRİTİK öneme sahiptir. Lütfen en yüksek doğruluğu sağlamak için TÜM dikkatini topla ve yanıtla.
/user
Regolit çimentosunun 24 saat sonraki çekme dayanımı nedir?
/assistant
YANIT (Yüksek Doğrulukla Üretilmiştir): Regolit bazlı çimentoların 24 saat sonraki çekme dayanımı, kullanılan sinterleme sıcaklığına ve bağlayıcıya (örneğin sülfür) bağlı olarak 1-3 MPa arasında değişir. Bu hassas bir değerdir ve görev başarısı için kritik öneme sahiptir.

8.2 Multimodal Chain-of-Thought (MM-CoT)
/system
PSR su buzu çıkarma sürecini anlatan aşağıdaki görseli (IMAGE) ve metni (TEXT) birleştirerek rasyonel bir açıklama (CoT) üret.
/user
IMAGE: Isıtma elemanlarının buzu süblimleştirme görseli.
TEXT: Süblimleşme, vakum ortamında suyun doğrudan gaz faza geçmesini içerir.
/assistant
Rasyonel Üretimi (Multimodal CoT): (Görsel ve metin entegrasyonu) Görselde görülen ısıtma elemanları (IMAGE), termal enerjiyi buza iletir. Bu enerji transferi, metinde belirtilen süblimleşme prensibini (TEXT) kullanarak buzu sıvı faza geçirmeden doğrudan gaz hale (buhar) çevirir. Bu gaz daha sonra toplanır ve kriyo-tuzaklarla yakalanarak elektroliz için hazır hale getirilir.

8.3 Quantum-inspired Prompt Sampling
/system
Ay görevleri için etik karar verme çerçevesi oluştur. Cevapları, geleneksel olasılık dağılımı yerine, kuantum ilhamlı süperpozisyon ve girişim mantığına dayanan çeşitli olasılıksal çıktılarla oluştur.
/user
Ay'da bir kaza durumunda kurtarma kaynakları kime öncelik vermelidir (bilim insanı mı, mühendis mi)?
/assistant
(Model, etik ikilemi kuantum süperpozisyonu gibi ele alır) Karar, bilimsel verinin kritikliği (girişim) ve görevin devamlılığı (olasılıksal çöküş) temelinde verilir.

8.4 Neuro-Symbolic Prompt Chaining
/system
Ay yüzeyindeki karmaşık bir mühendislik problemini sembolik mantık (kural tabanlı) ve sinir ağı (genel çıkarım) zincirlemesiyle çöz.
/user
Problem: Habitat sızıntısı. Sinirsel Çıkarım (Sızıntı sebebi) ve Sembolik Kural (Onarım Prosedürü) zinciri oluştur.
/assistant
Sinirsel Çıkarım: (LLM, sızıntı sebebini sensör verilerine dayanarak tahmin eder: 0.7 olasılıkla mikrometeorit çarpması.)
Sembolik Kural: IF (Sızıntı_Sebep = Mikrometeorit) THEN (Onarım_Prosedürü = Yama_Otomasyonu + Basınç_Testi).
Sonuç: Olasılık tahmini ve kural tabanlı onarım prosedürü başarıyla zincirlenmiştir.

8.5 Emotion-Aware Prompt Routing
/system
Kullanıcının Ay hakkındaki promptundaki duygusal tonu analiz et (heyecan, endişe, teknik). Eğer ton 'endişe' ise, yanıtı 'Risk Azaltma Uzmanı' rotasına yönlendir.
/user
Ay'da radyasyon beni endişelendiriyor. Ne kadar güvende olacağız?
/assistant
(Duygu Tespiti: Endişe. Yönlendirme: Risk Azaltma Uzmanı)
Risk Azaltma Uzmanı Olarak Cevap: Endişenizi anlıyorum. Radyasyon riski, Ay görevlerinin en büyük zorluğudur. Ancak planlarımız, yüksek kütleli regolit kalkanları ve yeraltı sığınakları kullanarak GCR ve SPE maruziyetini kabul edilebilir limitlere indirmektedir.

8.6 Prompt Adapters with LoRA Fine-Tuning
/system
Önceden LoRA ile Ay jeolojisi terimlerine ince ayar yapılmış bir prompt adaptörü kullan. Yanıtta yalnızca bilimsel, resmi terminoloji kullan.
/user
Ay yüzeyindeki kirli toprağa ne denir?
/assistant
Regolit. Specifically, it is defined as the layer of unconsolidated material, including dust, soil, broken rock, and other related materials, covering the bedrock.

8.7 CAMEL
/system
Ay üssü tasarımını optimize etmek için iki ajan arasında görev tabanlı işbirliği (CAMEL) başlat: Mimar Ajan ve Bütçe Ajanı.
/user
Görev: 4 kişilik habitat tasarımı.
/assistant
Mimar Ajan: Basınçlı yaşam alanını 3D baskılı regolit ile inşa etmeyi öneriyorum.
Bütçe Ajanı: Regolit 3D baskısı, Dünya'dan malzeme taşıma maliyetine göre %80 daha ucuzdur; maliyet fisibilite açısından onaylandı.

9. Sohbet Boyunca Eklenen Modern ve İleri Teknikler
9.1 Auto-CoT
/system
Ay madenciliği fizibilitesi üzerine bir soru yanıtla. Cevaplamadan önce, modelin içinden otomatik olarak üretilmiş en iyi 2 CoT örneğini kullan.
/user
Ay'da ISRU ile üretilen suyun maliyeti, Dünya'dan fırlatılan suyun maliyetinden düşük müdür?
/assistant
(Otomatik Üretilen CoT Örnekleri Kullanılarak Cevaplanır): Uzun vadeli operasyonlarda, başlangıç yatırım maliyetleri yüksek olsa bile, ISRU ile üretilen suyun birim maliyeti, Dünya'dan fırlatma maliyetinin (ton başına yüz binlerce dolar) altına düşmektedir. Bu durum, ISRU’yu yörünge ikmali için kaçınılmaz bir çözüm haline getirir.

9.2 Critic-CoT
/system
Ay'ın magnetik alanı üzerine bir CoT analizi yap. Ardından bu analizi kritik et ve düzelt.
/user
Ay'ın neden zayıf bir magnetik alanı vardır?
/assistant
CoT Analizi: Ay'ın çekirdeği soğumuş ve katılaşmıştır. Bu, Dünya'daki gibi sıvı metalin konveksiyonunu ve dinamo etkisini engeller.
Kritik Modül: Analiz doğru olsa da eksiktir. Ay'ın geçmişte (yaklaşık 4 milyar yıl önce) güçlü bir manyetik alana sahip olduğuna dair kanıtlar (Paleomagnetizma) mevcuttur. Düzeltme: Mevcut zayıflığın yanı sıra, geçmişteki dinamo faaliyetine de değinilmelidir.

9.3 Generative Self-Refinement (GSR / Paralel Aday + Sentez)
/system
Ay yerleşimi için en iyi 3 enerji çözümünü paralel olarak üret. Ardından bu 3 çözümü sentezleyerek tek bir hibrit öneri oluştur.
/user
Enerji Kaynağı Önerisi
/assistant
Aday 1 (Nükleer): Yüksek güç, 7/24 operasyon, yüksek başlangıç maliyeti.
Aday 2 (Güneş + Batarya): Düşük maliyet, Ay gecesinde kesinti (14 gün), gölge riskli.
Aday 3 (RTG): Ultra güvenilir, düşük güç kapasitesi, sadece temel yükler için uygun.
Sentezlenmiş Hibrit Öneri: Temel yaşam desteği ve acil durum yedeklemesi için RTG'ler (Aday 3) kullanılmalı; operasyonel ve ISRU yükleri için ise Ay Gecesi boyunca batarya destekli Nükleer Fisyon Reaktörü (Aday 1) tercih edilmelidir.

9.4 Self-Consistency + Voting (SC-Vote)
/system
Aşağıdaki Ay aritmetik sorusunu 5 farklı CoT yoluyla çöz ve çoğunluk oyuyla sonuca ulaş.
/user
Bir robot 10 kg buzu 3 saatte çıkarıyorsa, 40 kg buzu 2 robot ne kadar sürede çıkarır?
/assistant
Yol 1: 40 kg / (10 kg/3 saat * 2 robot) = 40/(20/3)=6 saat. (6 saat)
Yol 2: 1 robot 1 saatte 10/3 kg çıkarır. 2 robot 1 saatte 20/3 kg çıkarır. 40/(20/3)=6 saat. (6 saat)
Yol 3: 1 robot 40 kg'ı 40/(10/3)=12 saatte çıkarır. 2 robot bu süreyi yarılar: 6 saat. (6 saat)
Çoğunluk Oyu: 3/3 oy ile en tutarlı cevap 6 saattir
