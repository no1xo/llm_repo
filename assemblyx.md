## ÖZETLE DERLEME

* Kaynak kod (karakter dizisi)
    * if (b == a) a = b;
* Token adı
    * if, (, b, ==, a, ), a, =, b, ;
* Sözcük ayrıştırma (Abstract Syntax Tree (AST)
    * if, ( b == a ), a = b
* Dönüştürme AST
    * if, ( b == a ), a = b

## ÖZETLE DERLEME

* Kaynak Program
* Ara Kod Üretimi
    * Optimizasyon
* Kod Üretimi
    * CMP CX, 0
    * JNZ BLCK

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
* Ara Kod
* Kod Optimizasyonu
* Hedef Dil Program
    * out_time = start_time + cycles * 60

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
* Ara Kod
* Kod Optimizasyonu
* Hedef Dil Program
    * out_time = start_time + cycles * 60
    * EAX = ADD(10, 20)
    * EBX = MUL(EAX, 100)

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
    * ADD(10, 20)
    * MUL(EAX, 100)
* Ara Kod
* Kod Optimizasyonu
* Hedef Dil Program
    * out_time = start_time + cycles * 60
    * EAX = ADD(10, 20)
    * EBX = MUL(EAX, 100)

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
    * ADD(10, 20)
    * MUL(EAX, 100)
* Ara Kod
* Kod Optimizasyonu
* Hedef Dil Program
    * out_time = start_time + cycles * 60
    * ADD(10, 20)
    * MUL(EAX, 100)

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
    * ADD(10, 20)
    * MUL(EAX, 100)
* Ara Kod
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100
* Kod Optimizasyonu
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100
* Hedef Dil Program
    * out_time = start_time + cycles * 60
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100

## Örnek Derleme

* Kaynak Program
* Lexical Analiz
* Semantic Analiz
    * ADD(10, 20)
    * MUL(EAX, 100)
* Ara Kod
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100
* Kod Optimizasyonu
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100
* Hedef Dil Program
    * out_time = start_time + cycles * 60
    * temp1 = (10 + 20)
    * temp2 = temp1 * 100


**Slide 1**

**ÖZETLE DERLEME**

Kaynak kod (character akışı)
if (b == 0) a = b;

Token akışı
if ( b == 0 ) a = b ;

Soyut sentaks ağacı (Abstract Syntax Tree (AST))
Dominating AST

**Slide 2**

**ÖZETLE DERLEME**

Ara Kod Üretimi
Optimizasyon
Kod Üretimi
CMP CX, 0
JNE bloğu

**Slide 3**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
CMP CX, 0
JNE L1
MOV AX, CX
L1:

Hedef (IL) Program
CMP CX, 0
JNE L1
MOV AX, CX
L1:

**Slide 4**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Critical Analiz
BB1:L ADD(ID:1) AND MUL(ID:1) ID(b) INT(0)
BB1:L ID(a) ID(b)

Ara Kod
CMP CX, 0
JNE L1
MOV AX, CX
L1:

Hedef (IL) Program
CMP CX, 0
JNE L1
MOV AX, CX
L1:

**Slide 5**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
CMP CX, 0
JNE L1
MOV AX, CX
L1:

Hedef (IL) Program
CMP CX, 0
JNE L1
MOV AX, CX
L1:

**Slide 6**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
CMP CX, 0
JNE L1
MOV AX, CX
L1:

Hedef (IL) Program
CMP CX, 0
JNE L1
MOV AX, CX
L1:

**Slide 7**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
temp3 = MUL(temp2 ID:1)
L1 = ID:2 temp3

Hedef (IL) Program
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
temp3 = MUL(temp2 ID:1)
L1 = ID:2 temp3

**Slide 8**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
temp3 = MUL(temp2 ID:1)
L1 = ID:2 temp3

Optimize Kod (temp3)
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
L1 = ID:2 temp2

Hedef (IL) Program
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
L1 = ID:2 temp2

**Slide 9**

**Örnek Derleme**

Kaynak Program
if (b == 0) a = b;

Lexical Analiz
if ( b == 0 ) a = b ;

Semantic Analiz
if b == 0 goto L1
a = b
L1:

Ara Kod
temp1 = (ID:1) INT(0)
temp2 = AND(temp1)
L1 = ID:2 temp2

Optimize Kod (temp2)
temp1 = (ID:1) INT(0)
L1 = ID:2 temp1

Hedef (IL) Program
temp1 = (ID:1) INT(0)
L1 = ID:2 temp1
---------
## Derleme ÖZET

**Kaynak Program**

```
cur_time = start_time + cycles * 60
```

**Lexical Analiz**

```
id1 := id2 + id3 * 60
```

**Syntax Analiz**

```
     :=
   /   \
  id1   +
     /   \
    id2   *
       /   \
      id3   60
```

**Semantic Analiz**

```
     :=
   /   \
  id1   +
     /   \
    id2   *
       /   \
      id3   inttoreal
             \
              60
```

**Ara Kod Üretici**

```
temp1 := inttoreal(60)
temp2 := id3 * temp1
temp3 := id2 + temp2
id1 := temp3
```

**Ara Kod**

**Kod Optimizasyonu**

```
temp1 := id3 * 60.0
id1 := id2 + temp1
```

**Kod Üretici**

``` assembly
MOVF id3, R2
MULF #60.0, R2
MOVF id2, R1
ADDF R2, R1
MOVF R1, id1
```

**Assembly Kod**

**Ayrıştırma Ağacı**

105

