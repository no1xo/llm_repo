# Gelişmiş Akademik Test — 20 Soru + Cevaplar

Aşağıda her soru için kısa ve net çözümler/verili ispatlar bulunur.

---

## 1. (Analiz / Gerçek Analiz)  
**Soru:** \(f: \mathbb{R} \to \mathbb{R}\) sürekli ve  
\(\displaystyle \int_{-\infty}^{\infty} f(x)\,dx = 0,\quad \int_{-\infty}^{\infty} x f(x)\,dx = 0.\)  
Göster: \(\displaystyle \int_{-\infty}^{\infty} x^2 f(x)\,dx = 0\).

**Cevap (doğruluk durumu ve örnek):** Bu iddia genelde **yanlıştır**. İki ilk momentin 0 olması üçüncü momentin (ya da ikinci momentin) 0 olmasını gerektirmez. Aşağıda sürekli bir karşıörnek verilir.

**Karşıörnek (bump fonksiyon ile):** Let \(\varphi\) smooth (C∞), destekli, \(\int \varphi =1\), ve \(\int x\varphi(x)\,dx =0\). (Böyle bir even bump kolayca inşa edilir.) Tanımla
\[
f(x)=-2\varphi(x)+\varphi(x-1)+\varphi(x+1).
\]
Böylece \(\int f = -2\cdot1 +1+1 =0\). Ayrıca \(\int x f(x)\,dx = -2\cdot0 + 1\cdot1 + 1\cdot(-1) =0\). Ancak ikinci moment:
\[
\int x^2 f(x)\,dx = -2 m_2 + (m_2+1) + (m_2+1) = 2,
\]
burada \(m_2=\int x^2\varphi(x)\,dx\). Sonuç: ikinci moment \(=2\neq0\). Dolayısıyla önermenin genel hâli yanlış.

---

## 2. (Cebir / Soyut Cebir)  
**Soru:** \(G\) sonlu grup, \(H\) indeksi 2 olan altgrup. Göster \(H\) normal ve \(G/H\cong\mathbb{Z}_2\).

**Cevap:** İndeks 2 demek \( [G:H]=2\). Sol-kosetler \(gH\) ve sağ-kosetler \(Hg\) aynı sayıda ve toplam iki tane olmalı; ancak herhangi \(g\notin H\) için \(G\) iki kosete ayrılır: \(H\) ve \(gH\). Her \(g\) için \(gH\) ya \(H\) ile çakışır ya da diğer koset olur; aynı zamanda \(Hg\) de aynı iki kosettendir. İndeks 2 altgruplar her zaman normaldir çünkü sol ve sağ koset kümeleri birbirine eşit sayıda ve eleman eşlemesiyle tek tek çakışır; yani \(gH=Hg\) tüm \(g\). Böylece \(G/H\) iki elemanlı grup olur ve bu grup izomorfik \(\mathbb{Z}_2\) ile.

---

## 3. (Topoloji / Cebirsel Topoloji)  
**Soru:** \(X,Y\) bağlantılı, kompakt Hausdorff. \(f:X\to Y\) sürekli ve açık. Göster \(f\) örtme (covering) haritası.

**Cevap (kısa yol):** Genel durumda "sürekli + açık" bir harita örtme olması için local homeomorphism olması gerekir. Ancak ek koşullar (ör. her fiber izole ise ve örtücü lokal davranış gösterirse) gerekir. Soruda verilenler tek başına örtme garantisi vermez; genelde ek şartlar istenir (ör. her noktada fiber cardinalitesi sabit ve ayrık). Dolayısıyla sorunun doğru biçimi: eğer \(f\) sürekli, açık, lokal homeomorphism ve örtü koşulu sağlayan ek ayrıklık/finite-fiber şartı sağlanırsa \(f\) örtmedir. (Not: burada kısa cevap, doğru teknik koşulların belirtilmesi yönündedir.)

---

## 4. (İstatistik / Olasılık)  
**Soru:** \(\operatorname{Var}(X)=\sigma_X^2\), \(\operatorname{Var}(Y)=\sigma_Y^2\), \(\operatorname{Cov}(X,Y)=\rho\sigma_X\sigma_Y\). Göster \(\operatorname{Var}(X+Y)=\sigma_X^2+\sigma_Y^2+2\rho\sigma_X\sigma_Y\).

**Cevap:** Direkt:
\[
\operatorname{Var}(X+Y)=\mathbb{E}[(X+Y-\mathbb{E}[X+Y])^2]
= \operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y),
\]
yerine koyunca istenen form elde edilir.

---

## 5. (Lineer Cebir)  
**Soru:** \(A\) diagonalizable. Göster \(\det(e^A)=e^{\operatorname{Tr}(A)}\).

**Cevap:** \(A = P D P^{-1}\) ile \(e^A = P e^D P^{-1}\). Determinant çarpım özelliği ile \(\det(e^A)=\det(e^D)\). Eğer \(D=\mathrm{diag}(\lambda_1,\dots,\lambda_n)\) ise \(e^D=\mathrm{diag}(e^{\lambda_1},\dots,e^{\lambda_n})\) ve \(\det(e^D)=\prod e^{\lambda_i}=e^{\sum \lambda_i}=e^{\operatorname{Tr}(A)}\).

---

## 6. (Sayı Teorisi)  
**Soru:** \(p\) asal, göster \(a^p \equiv a \pmod p\) tüm \(a\in\mathbb{Z}_p\).

**Cevap (Fermat):** Eğer \(p\) asal ve \(a\not\equiv0\) ise Fermat'ın küçük teoremi \(a^{p-1}\equiv1\pmod p\) verir; çarpınca \(a^p\equiv a\). \(a\equiv0\) için de trivially doğru. Alternatif olarak polinom \(x^p-x\) tüm \( \mathbb{F}_p\) üzerinde kök verir çünkü \(\mathbb{F}_p\) alanında her eleman kendi p-inci kuvvetine eşittir.

---

## 7. (Kuantum Mekaniği)  
**Soru:** 1-D harmonik osilatörün temel durumu \(\psi_0(x)\) ve enerjisini ver.

**Cevap:** Temel dalga fonksiyonu (normalizasyon sabit \(N\)):
\[
\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} e^{-\frac{m\omega x^2}{2\hbar}}.
\]
Temel enerji:
\[
E_0 = \frac{1}{2}\hbar\omega.
\]

---

## 8. (Elektromanyetizma / Maxwell Denklemleri)  
**Soru:** Vakumda Maxwell denklemlerini yaz ve \(\mathbf{E}\) için dalga denklemine ulaş.

**Cevap:** Vakum (kaynak yok) için Maxwell:
\[
\nabla\cdot\mathbf{E}=0,\qquad \nabla\cdot\mathbf{B}=0,
\]
\[
\nabla\times\mathbf{E}=-\frac{\partial\mathbf{B}}{\partial t},\qquad
\nabla\times\mathbf{B}=\mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}.
\]
Curl'ün zaman türevini alıp ikinci denklemi kullan:
\[
\nabla\times(\nabla\times\mathbf{E}) = -\frac{\partial}{\partial t}(\nabla\times\mathbf{B})
= -\mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}.
\]
Sol taraftan \(\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}=-\nabla^2\mathbf{E}\) olur çünkü \(\nabla\cdot\mathbf{E}=0\). Böylece
\[
\nabla^2\mathbf{E} - \mu_0\varepsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}=0,
\]
ki bu elektromanyetik dalga denklemidir. Dalga hızı \(c=1/\sqrt{\mu_0\varepsilon_0}\).

---

## 9. (İstatistik / Teorik İstatistik)  
**Soru:** Unbiased tahminci için Cramér-Rao alt sınırını göster.

**Cevap (kısa ispat):** Likelihood \(L(\theta)=\log f(X;\theta)\), skor \(U(X)=\partial_\theta L\). Unbiased ise \(\mathbb{E}[\hat\theta]=\theta\). Cauchy–Schwarz uygulayarak
\[
\operatorname{Var}(\hat\theta) \ge \frac{(\mathrm{Cov}(\hat\theta,U))^2}{\operatorname{Var}(U)}.
\]
Hesaplar \(\mathrm{Cov}(\hat\theta,U)=1\) verir (detay: \(\mathbb{E}[U]=0\) ve \(\partial_\theta \mathbb{E}[\hat\theta]=1\)), ve \(\operatorname{Var}(U)=I(\theta)\) tanımıyla sonuç
\[
\operatorname{Var}(\hat\theta)\ge \frac{1}{I(\theta)}
\]
elde edilir.

---

## 10. (PDE / Laplace Denklemi)  
**Soru:** Birim karede sınır değer problemi: \(u_{xx}+u_{yy}=0\) ve kenarlar \(u=0\) ama üst kenarda \(u(x,1)=\sin(\pi x)\). Bul \(u(x,y)\).

**Cevap (ayırma yöntemi):** Ayrma ile sin serileri: üst sınır yalnızca \(\sin(\pi x)\) olduğundan çöz
\[
u(x,y)=\sinh(\pi y)\frac{\sin(\pi x)}{\sinh(\pi)}.
\]
(Doğrulama: \(u(x,0)=0,\ u(x,1)=\sinh(\pi)/\sinh(\pi)\sin(\pi x)=\sin(\pi x)\).)

---

## 11. (Optimizasyon / Konveks Analiz)  
**Soru:** \(f\in C^2\), Hessian pozitif yarı-tanımlı (konveks). Göster her lokal min global mintir.

**Cevap:** Konvekslik: \(f(\lambda x+(1-\lambda)y)\le \lambda f(x)+(1-\lambda)f(y)\). Bir \(x^*\) lokal minimum ise tüm küçük yönlerde \(f(x)\ge f(x^*)\)dır. Konveks fonksiyonda eğer lokal min varsa, fonksiyon boyunca global en küçük değer budur çünkü konveks fonksiyonun alt seviyeleri convex setlerdir; formal olarak, herhangi \(y\) için segment üzerindeki değerler \(f\) değerini aşamaz; bu basic konvekslik argümanı ile lokal minimum global olur.

---

## 12. (Sayı Teorisi)  
**Soru:** \(a,b\in\mathbb{Z}\) ve \(a^2+b^2\) asal ise ya \(a=0\) ya \(b=0\).

**Cevap:** Eğer \(a\neq0\) ve \(b\neq0\) olsaydı \(a^2+b^2\) çift olmayabilir fakat Gauss tam sayıları bakımı ile: asal \(p=a^2+b^2\) şeklinde yazılıyorsa \(p\) ya \(2\) ya da \(p\equiv1\pmod4\) türündedir. Söylenen önerme genel olarak yanlış (ör. \(a=1,b=2\) için \(1^2+2^2=5\) asaldır ve ne \(a\) ne \(b\) sıfırdır). Dolayısıyla ifade yanlıştır; karşıörnek \(1^2+2^2=5\).

---

## 13. (Süreçler / Poisson)  
**Soru:** Poisson süreci \(N(t)\) parametre \(\lambda\). Göster bağımsız artış ve \(N(t+s)-N(s)\sim\mathrm{Pois}(\lambda t)\).

**Cevap:** Poisson sürecin tanımı bu özellikleri içerir: artışların bağımsızlığı ve artışların Poisson dağılımı ile olması. Tekrar ispat: küçük aralıklarda olay oranı \(\lambda \Delta t\), limit alındığında Poisson yapısı ortaya çıkar; bağımsız alt aralıklar için bağımsız sayılar.

---

## 14. (Kodlama / Bilgi Kuramı)  
**Soru:** Binary symmetric channel (BSC) için kapasite \(C = 1 - H(p)\). Açıkla.

**Cevap:** Kanalın mutual information maksimumu uniform giriş dağılımı için alınır. BSC için \(I(X;Y)=1-H(p)\) olur (bit başına), burada \(H(p)=-p\log_2 p-(1-p)\log_2(1-p)\) ikili entropidir. Dolayısıyla kanal kapasitesi \(C=1-H(p)\).

---

## 15. (Karmaşık Analiz)  
**Soru:** Eğer entire \(g\) için \(|g(z)| \le A e^{B|z|}\) ise \(g\) polinomdur.

**Cevap (kısa ispat):** Bu tür büyüme sınırlaması \(g\)'nin en fazla birinci dereceden (veya daha genelde B büyüme sınıfına göre finite order) olduğunu söyler. Cauchy tahminleri ile türev boundları:  
\[
|g^{(n)}(0)| \le \frac{n!}{R^n} \sup_{|z|=R} |g(z)| \le \frac{n!}{R^n} A e^{B R}.
\]
Sağ taraf \(R\to\infty\) için sıfıra gitmesi için \(n\) yeterince büyük olmalı; uygun seçimle belirli dereceden büyük türevler 0 olur; böylece \(g\) polinomdur. (Daha ayrıntılı: growth order analizine dayanır.)

---

## 16. (Fonksiyonel Analiz)  
**Soru:** \(H\) Hilbert, \(T\) bounded, \(\|T\|<1\). Göster \(I-T\) terslenebilir ve \((I-T)^{-1}=\sum_{n=0}^\infty T^n\).

**Cevap:** Neumann serisi: \(\sum_{n=0}^\infty T^n\) operatör normunda mutlakça konverger çünkü geometrik seri ve \(\|T\|<1\). Ayrıca \((I-T)\sum_{n=0}^N T^n = I-T^{N+1}\) ve \(N\to\infty\) alınca sağ taraf \(I\). Yani ters var ve formül doğrudur.

---

## 17. (Kuantum Alan Teorisi / Temel Fizik)  
**Soru:** Serbest skaler alan için Euler-Lagrange denklemlerinden Klein-Gordon'u çıkar.

**Cevap:** Lagrange yoğunluğu
\(\mathcal{L}=\tfrac12(\partial_\mu\phi)(\partial^\mu\phi)-\tfrac12 m^2\phi^2.\) Euler-Lagrange:
\[
\partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi)}\right)-\frac{\partial\mathcal{L}}{\partial\phi}=0
\]
verir: \(\partial_\mu\partial^\mu\phi + m^2\phi = 0\) yani
\[
(\Box + m^2)\phi=0,
\]
bu Klein-Gordon denklemidir. Momentum uzayında Fourier ile \(\phi(x)=\int \tilde\phi(k)e^{-ikx}dk\) alırsak dispersion relation \(k^\mu k_\mu = m^2\) (yani \(\omega^2=\mathbf{k}^2+m^2\)) elde edilir.

---

## 18. (Diferansiyel Geometri)  
**Soru:** Levi-Civita bağlantısının tekilliğini göster.

**Cevap (kısa ispat):** Levi-Civita bağlantısı metrik uyumlu (\(\nabla g=0\)) ve torsiyonsuz (\(T=0\)) olmak üzere tanımlanır. Christoffel sembolleri için açık formül:
\[
\Gamma^k_{ij}=\tfrac12 g^{k\ell}(\partial_i g_{j\ell} + \partial_j g_{i\ell} - \partial_\ell g_{ij}).
\]
Bu formül tek bir bağlantıyı verir; yani koşulları sağlayan bağlantı eşsizdir.

---

## 19. (Çok Değişkenli İstatistik)  
**Soru:** \(X\sim N(\mu,\Sigma)\). Yoğunluk ve SE hakkında yorum.

**Cevap:** Yoğunluk:
\[
f_X(x)=\frac{1}{(2\pi)^{n/2}\det(\Sigma)^{1/2}}\exp\!\left(-\tfrac12 (x-\mu)^\top\Sigma^{-1}(x-\mu)\right).
\]
Standart hata (SE) genelde bileşenler için \(\mathrm{SE}( \hat\mu_i) = \sqrt{\Sigma_{ii}/N}\) gibi örnekleme dağılımlarında çıkar (örneklem büyüklüğüne göre); kovaryans matrisinin kökleri belirsizliğin ölçüsünü verir.

---

## 20. (Sinyaller & Dalgalar / Fourier Analizi)  
**Soru:** Parseval / Plancherel teoremi: \(\int |f(t)|^2 dt = \frac{1}{2\pi}\int |F(\omega)|^2 d\omega\).

**Cevap (öz):** Eğer \(F(\omega)=\int_{-\infty}^\infty f(t)e^{-i\omega t}dt\) tanımı kullanılıyorsa Plancherel/Parseval:
\[
\int_{-\infty}^\infty |f(t)|^2 dt = \frac{1}{2\pi}\int_{-\infty}^\infty |F(\omega)|^2 d\omega,
\]
iç çarpımın Fourier dönüşümü ile korunmasından (unitary property) elde edilir. İspat Fourier dönüşümün unitary olduğu doğrultusunda integraller üzerinden Cauchy ve ters dönüşüm kullanılarak yapılır.

---

# Notlar ve Açıklamalar
- Bazı sorularda (3. ve 12. gibi) orijinal sorunun ifadesi tam koşul gerektiriyor; ben gerekliyse düzeltici not veya karşıörnek belirttim.  
- Eğer her soru için **tam adım-adım ayrıntılı çözüm** (sayfa sayfa) istersen, bunu da her bir soru için ayrı Markdown dosyası şeklinde sağlayabilirim.  
- Bu paketi LLM test seti olarak kullanacaksan istersen her sorunun zorluk derecesine göre puanlama anahtarı ve beklenen ana fikirleri (rubric) hazırlayayım.

