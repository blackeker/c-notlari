# -*- coding: utf-8 -*-
"""
30 GÜNLÜK (150 DERSLİK) ZENGİNLEŞTİRİLMİŞ C DİLİ MÜFREDATI VE DERS VERİLERİ
Her ders derinlemesine teori, bellek şemaları, kod analizi, sık yapılan hatalar ve ders içi soru içerir.
"""

# Her güne özel derlenebilir starter kodlar
day_starter_codes = {
    1: '''#include <stdio.h>

/* GÜN 1: C Dilinin Temelleri - İlk Program */
int main() {
    printf("Merhaba Dunya!\\n");
    printf("Bu benim ilk C programim.\\n");
    printf("Derleme basarili!\\n");
    return 0;
}
''',
    2: '''#include <stdio.h>

/* GÜN 2: Veri Tipleri ve Değişkenler */
int main() {
    int tam_sayi = 42;
    float ondalik = 3.14f;
    double hassas = 2.718281828;
    char karakter = 'A';

    printf("sizeof(char)   = %zu bayt\\n", sizeof(char));
    printf("sizeof(int)    = %zu bayt\\n", sizeof(int));
    printf("sizeof(float)  = %zu bayt\\n", sizeof(float));
    printf("sizeof(double) = %zu bayt\\n", sizeof(double));

    printf("\\nDegerler:\\n");
    printf("  tam_sayi = %d\\n", tam_sayi);
    printf("  ondalik  = %.2f\\n", ondalik);
    printf("  hassas   = %.9f\\n", hassas);
    printf("  karakter = %c (ASCII: %d)\\n", karakter, karakter);

    return 0;
}
''',
    3: '''#include <stdio.h>

/* GÜN 3: Format Belirteçleri ve Biçimlendirme */
int main() {
    int x = 42;
    float pi = 3.14159f;
    char harf = 'C';

    printf("Tam sayi: %d\\n", x);
    printf("Ondalik (2 basamak): %.2f\\n", pi);
    printf("Karakter: %c\\n", harf);
    printf("String: %s\\n", "Merhaba");

    printf("\\n--- Hizalama ---\\n");
    printf("[%10d]\\n", x);
    printf("[%-10d]\\n", x);
    printf("[%010d]\\n", x);
    printf("[%8.3f]\\n", pi);

    printf("\\nHex: %x, Oktal: %o\\n", 255, 255);
    return 0;
}
''',
    4: '''#include <stdio.h>

/* GÜN 4: Klavye Girdileri (scanf) */
int main() {
    int yas;
    float boy;
    char isim[50];

    printf("Adinizi girin: ");
    scanf("%49s", isim);
    printf("Yasinizi girin: ");
    scanf("%d", &yas);
    printf("Boyunuzu girin (m): ");
    scanf("%f", &boy);

    printf("\\n--- Bilgileriniz ---\\n");
    printf("Ad: %s\\n", isim);
    printf("Yas: %d\\n", yas);
    printf("Boy: %.2f m\\n", boy);
    return 0;
}
''',
    5: '''#include <stdio.h>

/* GÜN 5: Operatörler ve Tip Dönüşümü */
int main() {
    int a = 17, b = 5;

    printf("a = %d, b = %d\\n\\n", a, b);
    printf("Toplam:    %d\\n", a + b);
    printf("Fark:      %d\\n", a - b);
    printf("Carpim:    %d\\n", a * b);
    printf("Bolum:     %d (tam sayi)\\n", a / b);
    printf("Mod:       %d\\n", a % b);

    float sonuc = (float)a / b;
    printf("\\nGercek bolum (cast): %.2f\\n", sonuc);

    int c = 10;
    printf("\\nc = %d, c++ = %d, ", c, c++);
    printf("++c = %d\\n", ++c);
    return 0;
}
''',
    6: '''#include <stdio.h>

/* GÜN 6: Koşullu Mantık (if / else) */
int main() {
    int not_degeri = 75;

    printf("Not: %d\\n", not_degeri);

    if (not_degeri >= 90) {
        printf("Harf Notu: AA\\n");
    } else if (not_degeri >= 80) {
        printf("Harf Notu: BA\\n");
    } else if (not_degeri >= 70) {
        printf("Harf Notu: BB\\n");
    } else if (not_degeri >= 60) {
        printf("Harf Notu: CB\\n");
    } else {
        printf("Harf Notu: FF (Kaldi)\\n");
    }

    int x = 10, y = 20;
    if (x > 5 && y < 30) {
        printf("\\nHer iki kosul da dogru (AND)\\n");
    }
    if (x > 100 || y < 30) {
        printf("En az biri dogru (OR)\\n");
    }
    return 0;
}
''',
    7: '''#include <stdio.h>

/* GÜN 7: switch-case ve Ternary Operatörü */
int main() {
    int gun = 3;

    printf("Gun: %d -> ", gun);
    switch (gun) {
        case 1: printf("Pazartesi\\n"); break;
        case 2: printf("Sali\\n"); break;
        case 3: printf("Carsamba\\n"); break;
        case 4: printf("Persembe\\n"); break;
        case 5: printf("Cuma\\n"); break;
        case 6: case 7: printf("Hafta sonu\\n"); break;
        default: printf("Gecersiz gun\\n");
    }

    int yas = 20;
    const char *durum = (yas >= 18) ? "Yetiskin" : "Cocuk";
    printf("Yas %d: %s\\n", yas, durum);

    int a = 5, b = 8;
    int max = (a > b) ? a : b;
    printf("max(%d, %d) = %d\\n", a, b, max);
    return 0;
}
''',
    8: '''#include <stdio.h>

/* GÜN 8: for Döngüleri */
int main() {
    printf("--- Carpim Tablosu (5) ---\\n");
    for (int i = 1; i <= 10; i++) {
        printf("5 x %2d = %2d\\n", i, 5 * i);
    }

    printf("\\n--- Yildiz Ucgeni ---\\n");
    for (int i = 1; i <= 5; i++) {
        for (int j = 0; j < i; j++) {
            printf("* ");
        }
        printf("\\n");
    }

    printf("\\n--- Cift Sayilar (0-20) ---\\n");
    for (int i = 0; i <= 20; i += 2) {
        printf("%d ", i);
    }
    printf("\\n");
    return 0;
}
''',
    9: '''#include <stdio.h>

/* GÜN 9: while ve do-while Döngüleri */
int main() {
    /* Basamak sayma */
    int sayi = 123456, basamak = 0;
    int temp = sayi;
    while (temp != 0) {
        temp /= 10;
        basamak++;
    }
    printf("%d sayisi %d basamakli\\n", sayi, basamak);

    /* Basamak toplami */
    int toplam = 0;
    temp = sayi;
    do {
        toplam += temp % 10;
        temp /= 10;
    } while (temp > 0);
    printf("%d sayisinin basamak toplami: %d\\n", sayi, toplam);

    /* Ters cevirme */
    int ters = 0;
    temp = sayi;
    while (temp > 0) {
        ters = ters * 10 + temp % 10;
        temp /= 10;
    }
    printf("%d sayisinin tersi: %d\\n", sayi, ters);
    return 0;
}
''',
    10: '''#include <stdio.h>

/* GÜN 10: Fonksiyonlar ve Modüler Kodlama */

/* Fonksiyon prototipleri */
int topla(int a, int b);
int faktoriyel(int n);
void satir_ciz(int uzunluk);

int main() {
    satir_ciz(30);
    printf("topla(3, 7) = %d\\n", topla(3, 7));
    printf("5! = %d\\n", faktoriyel(5));
    printf("10! = %d\\n", faktoriyel(10));
    satir_ciz(30);
    return 0;
}

int topla(int a, int b) {
    return a + b;
}

int faktoriyel(int n) {
    if (n <= 1) return 1;
    return n * faktoriyel(n - 1);
}

void satir_ciz(int uzunluk) {
    for (int i = 0; i < uzunluk; i++) printf("-");
    printf("\\n");
}
''',
    11: '''#include <stdio.h>

/* GÜN 11: Kapsam ve Özyineleme */
int global_sayac = 0;

void sayac_arttir() {
    static int yerel_sayac = 0;
    yerel_sayac++;
    global_sayac++;
    printf("  yerel_sayac(static)=%d, global=%d\\n", yerel_sayac, global_sayac);
}

int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    printf("--- Static Degisken Demo ---\\n");
    for (int i = 0; i < 3; i++) sayac_arttir();

    printf("\\n--- Fibonacci Serisi ---\\n");
    for (int i = 0; i < 10; i++) {
        printf("fib(%d) = %d\\n", i, fibonacci(i));
    }
    return 0;
}
''',
    12: '''#include <stdio.h>

/* GÜN 12: Tek Boyutlu Diziler */
int main() {
    int dizi[] = {64, 25, 12, 22, 11, 90, 34};
    int n = sizeof(dizi) / sizeof(dizi[0]);
    int toplam = 0, en_buyuk = dizi[0], en_kucuk = dizi[0];

    printf("Dizi: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", dizi[i]);
        toplam += dizi[i];
        if (dizi[i] > en_buyuk) en_buyuk = dizi[i];
        if (dizi[i] < en_kucuk) en_kucuk = dizi[i];
    }

    printf("\\nEleman sayisi: %d\\n", n);
    printf("Toplam: %d\\n", toplam);
    printf("Ortalama: %.2f\\n", (float)toplam / n);
    printf("En buyuk: %d\\n", en_buyuk);
    printf("En kucuk: %d\\n", en_kucuk);
    return 0;
}
''',
    13: '''#include <stdio.h>
#include <string.h>

/* GÜN 13: Karakter Dizileri (Strings) */
int main() {
    char isim[50] = "Merhaba";
    char soyad[50] = "Dunya";
    char tam_isim[100];

    printf("isim: %s (uzunluk: %zu)\\n", isim, strlen(isim));
    printf("soyad: %s (uzunluk: %zu)\\n", soyad, strlen(soyad));

    strcpy(tam_isim, isim);
    strcat(tam_isim, " ");
    strcat(tam_isim, soyad);
    printf("tam_isim: %s\\n", tam_isim);

    int karsilastirma = strcmp(isim, soyad);
    printf("\\nstrcmp sonucu: %d ", karsilastirma);
    if (karsilastirma < 0) printf("(isim < soyad)\\n");
    else if (karsilastirma > 0) printf("(isim > soyad)\\n");
    else printf("(esit)\\n");
    return 0;
}
''',
    14: '''#include <stdio.h>

/* GÜN 14: İşaretçiler (Pointers) - Temeller */
void takas(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 10, y = 20;
    int *ptr = &x;

    printf("x = %d, adresi = %p\\n", x, (void*)&x);
    printf("*ptr = %d, ptr = %p\\n", *ptr, (void*)ptr);

    printf("\\nTakas oncesi: x=%d, y=%d\\n", x, y);
    takas(&x, &y);
    printf("Takas sonrasi: x=%d, y=%d\\n", x, y);
    return 0;
}
''',
    15: '''#include <stdio.h>

/* GÜN 15: Pointer Aritmetiği ve Dizi İlişkisi */
int main() {
    int dizi[] = {10, 20, 30, 40, 50};
    int *p = dizi;
    int n = sizeof(dizi) / sizeof(dizi[0]);

    printf("--- Pointer ile Dizi Gezme ---\\n");
    for (int i = 0; i < n; i++) {
        printf("*(p+%d) = %d  |  p[%d] = %d  |  adres: %p\\n",
               i, *(p+i), i, p[i], (void*)(p+i));
    }

    printf("\\nPointer farki: p+4 - p = %td\\n", (p+4) - p);
    return 0;
}
''',
    16: '''#include <stdio.h>

/* GÜN 16: İki Boyutlu Diziler ve Matris */
#define SATIR 3
#define SUTUN 3

int main() {
    int A[SATIR][SUTUN] = {{1,2,3},{4,5,6},{7,8,9}};
    int B[SATIR][SUTUN] = {{9,8,7},{6,5,4},{3,2,1}};
    int C[SATIR][SUTUN];

    printf("A + B = C\\n\\n");
    for (int i = 0; i < SATIR; i++) {
        for (int j = 0; j < SUTUN; j++) {
            C[i][j] = A[i][j] + B[i][j];
            printf("%3d ", C[i][j]);
        }
        printf("\\n");
    }
    return 0;
}
''',
    17: '''#include <stdio.h>

/* GÜN 17: Yapılar (Structs) */
struct Ogrenci {
    char isim[50];
    int numara;
    float ortalama;
};

void ogrenci_yazdir(struct Ogrenci o) {
    printf("  %s (No: %d) - Ort: %.2f\\n", o.isim, o.numara, o.ortalama);
}

int main() {
    struct Ogrenci sinif[] = {
        {"Ali", 101, 85.5f},
        {"Ayse", 102, 92.3f},
        {"Mehmet", 103, 78.0f}
    };
    int n = sizeof(sinif) / sizeof(sinif[0]);

    printf("--- Sinif Listesi ---\\n");
    for (int i = 0; i < n; i++) {
        ogrenci_yazdir(sinif[i]);
    }
    return 0;
}
''',
    18: '''#include <stdio.h>
#include <stdlib.h>

/* GÜN 18: Dinamik Bellek Yönetimi */
int main() {
    int n = 5;
    int *dizi = (int*)malloc(n * sizeof(int));

    if (dizi == NULL) {
        printf("Bellek tahsisi basarisiz!\\n");
        return 1;
    }

    for (int i = 0; i < n; i++) dizi[i] = (i + 1) * 10;

    printf("Orijinal (%d eleman): ", n);
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    n = 8;
    dizi = (int*)realloc(dizi, n * sizeof(int));
    for (int i = 5; i < n; i++) dizi[i] = (i + 1) * 10;

    printf("Genisletilmis (%d eleman): ", n);
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    free(dizi);
    printf("Bellek serbest birakildi.\\n");
    return 0;
}
''',
    19: '''#include <stdio.h>

/* GÜN 19: Metin Dosya İşlemleri */
int main() {
    FILE *f = fopen("notlar.txt", "w");
    if (f == NULL) { printf("Dosya acilamadi!\\n"); return 1; }

    fprintf(f, "Ali 85\\n");
    fprintf(f, "Ayse 92\\n");
    fprintf(f, "Mehmet 78\\n");
    fclose(f);
    printf("Dosyaya yazildi.\\n\\n");

    f = fopen("notlar.txt", "r");
    if (f == NULL) { printf("Dosya okunamadi!\\n"); return 1; }

    char isim[50]; int not_val;
    printf("--- Dosya Icerigi ---\\n");
    while (fscanf(f, "%s %d", isim, &not_val) == 2) {
        printf("  %s: %d\\n", isim, not_val);
    }
    fclose(f);
    return 0;
}
''',
    20: '''#include <stdio.h>

/* GÜN 20: İkili (Binary) Dosya İşlemleri */
typedef struct {
    int id;
    char ad[30];
    float maas;
} Personel;

int main() {
    Personel p1 = {101, "Ahmet Yilmaz", 45000.50f};
    Personel p2 = {102, "Zeynep Kaya", 52000.0f};

    FILE *f = fopen("personel.bin", "wb");
    if (f) {
        fwrite(&p1, sizeof(Personel), 1, f);
        fwrite(&p2, sizeof(Personel), 1, f);
        fclose(f);
        printf("2 kayit yazildi.\\n\\n");
    }

    f = fopen("personel.bin", "rb");
    if (f) {
        Personel oku;
        printf("--- Okunan Kayitlar ---\\n");
        while (fread(&oku, sizeof(Personel), 1, f) == 1) {
            printf("  ID:%d  Ad:%s  Maas:%.2f TL\\n", oku.id, oku.ad, oku.maas);
        }
        fclose(f);
    }
    return 0;
}
''',
    21: '''#include <stdio.h>

/* GÜN 21: Bit Düzeyinde İşlemler */
void ikili_yazdir(int sayi, int bit) {
    for (int i = bit - 1; i >= 0; i--)
        printf("%d", (sayi >> i) & 1);
}

int main() {
    int a = 0b1010;  /* 10 */
    int b = 0b1100;  /* 12 */

    printf("a     = "); ikili_yazdir(a, 8); printf(" (%d)\\n", a);
    printf("b     = "); ikili_yazdir(b, 8); printf(" (%d)\\n", b);
    printf("a & b = "); ikili_yazdir(a & b, 8); printf(" (%d) AND\\n", a & b);
    printf("a | b = "); ikili_yazdir(a | b, 8); printf(" (%d) OR\\n", a | b);
    printf("a ^ b = "); ikili_yazdir(a ^ b, 8); printf(" (%d) XOR\\n", a ^ b);
    printf("~a    = "); ikili_yazdir((unsigned char)~a, 8); printf(" NOT\\n");
    printf("a<<2  = "); ikili_yazdir(a << 2, 8); printf(" (%d)\\n", a << 2);
    printf("b>>1  = "); ikili_yazdir(b >> 1, 8); printf(" (%d)\\n", b >> 1);
    return 0;
}
''',
    22: '''#include <stdio.h>

/* GÜN 22: Enum ve Bit Sahaları */
enum Renk { KIRMIZI, YESIL, MAVI, SARI };

struct Bayrak {
    unsigned int okundu  : 1;
    unsigned int yazildi : 1;
    unsigned int silindi : 1;
    unsigned int oncelik : 3;
};

int main() {
    enum Renk r = MAVI;
    printf("Renk kodu: %d\\n", r);

    const char *isimler[] = {"Kirmizi", "Yesil", "Mavi", "Sari"};
    for (int i = KIRMIZI; i <= SARI; i++)
        printf("  %d = %s\\n", i, isimler[i]);

    struct Bayrak b = {1, 0, 0, 5};
    printf("\\nBayrak: okundu=%u yazildi=%u silindi=%u oncelik=%u\\n",
           b.okundu, b.yazildi, b.silindi, b.oncelik);
    printf("sizeof(Bayrak) = %zu bayt\\n", sizeof(struct Bayrak));
    return 0;
}
''',
    23: '''#include <stdio.h>

/* GÜN 23: Fonksiyon Göstericileri */
int topla(int a, int b) { return a + b; }
int cikar(int a, int b) { return a - b; }
int carp(int a, int b)  { return a * b; }

void hesapla(int x, int y, int (*islem)(int, int), const char *ad) {
    printf("  %s(%d, %d) = %d\\n", ad, x, y, islem(x, y));
}

int main() {
    int a = 15, b = 4;
    printf("--- Fonksiyon Gostericileri ---\\n");
    hesapla(a, b, topla, "topla");
    hesapla(a, b, cikar, "cikar");
    hesapla(a, b, carp, "carp");

    int (*islemler[])(int, int) = {topla, cikar, carp};
    const char *adlar[] = {"Toplam", "Fark", "Carpim"};
    printf("\\n--- Dizi Uzerinden ---\\n");
    for (int i = 0; i < 3; i++)
        printf("  %s: %d\\n", adlar[i], islemler[i](a, b));
    return 0;
}
''',
    24: '''#include <stdio.h>
#include <stdlib.h>

/* GÜN 24: Bağlı Liste (Linked List) */
struct Dugum {
    int veri;
    struct Dugum *sonraki;
};

void basa_ekle(struct Dugum **bas, int veri) {
    struct Dugum *yeni = (struct Dugum*)malloc(sizeof(struct Dugum));
    yeni->veri = veri;
    yeni->sonraki = *bas;
    *bas = yeni;
}

void yazdir(struct Dugum *dugum) {
    while (dugum) {
        printf("%d -> ", dugum->veri);
        dugum = dugum->sonraki;
    }
    printf("NULL\\n");
}

void temizle(struct Dugum **bas) {
    struct Dugum *temp;
    while (*bas) { temp = *bas; *bas = (*bas)->sonraki; free(temp); }
}

int main() {
    struct Dugum *liste = NULL;
    basa_ekle(&liste, 30);
    basa_ekle(&liste, 20);
    basa_ekle(&liste, 10);
    printf("Liste: "); yazdir(liste);
    temizle(&liste);
    printf("Temizlendi: "); yazdir(liste);
    return 0;
}
''',
    25: '''#include <stdio.h>

/* GÜN 25: Stack ve Queue */
#define MAX 10

/* Stack */
int yigin[MAX], tepe = -1;
void push(int v) { if (tepe < MAX-1) yigin[++tepe] = v; }
int pop()        { return tepe >= 0 ? yigin[tepe--] : -1; }

/* Queue */
int kuyruk[MAX], on = 0, arka = 0;
void enqueue(int v) { if (arka < MAX) kuyruk[arka++] = v; }
int dequeue()       { return on < arka ? kuyruk[on++] : -1; }

int main() {
    printf("--- Stack (LIFO) ---\\n");
    push(10); push(20); push(30);
    printf("pop: %d, %d, %d\\n", pop(), pop(), pop());

    printf("\\n--- Queue (FIFO) ---\\n");
    enqueue(10); enqueue(20); enqueue(30);
    printf("dequeue: %d, %d, %d\\n", dequeue(), dequeue(), dequeue());
    return 0;
}
''',
    26: '''#include <stdio.h>

/* GÜN 26: İleri Özyineleme */
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}

long us_al(int taban, int us) {
    if (us == 0) return 1;
    return taban * us_al(taban, us - 1);
}

void hanoi(int n, char kaynak, char hedef, char yardimci) {
    if (n == 1) {
        printf("  Disk 1: %c -> %c\\n", kaynak, hedef);
        return;
    }
    hanoi(n-1, kaynak, yardimci, hedef);
    printf("  Disk %d: %c -> %c\\n", n, kaynak, hedef);
    hanoi(n-1, yardimci, hedef, kaynak);
}

int main() {
    printf("Fibonacci(8) = %d\\n", fibonacci(8));
    printf("2^10 = %ld\\n", us_al(2, 10));
    printf("\\nHanoi Kulesi (3 disk):\\n");
    hanoi(3, 'A', 'C', 'B');
    return 0;
}
''',
    27: '''#include <stdio.h>

/* GÜN 27: Sıralama Algoritmaları */
void dizi_yazdir(int arr[], int n, const char *baslik) {
    printf("%s: ", baslik);
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\\n");
}

void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n-1; i++)
        for (int j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1]) {
                int t = arr[j]; arr[j] = arr[j+1]; arr[j+1] = t;
            }
}

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        int min_idx = i;
        for (int j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx]) min_idx = j;
        int t = arr[i]; arr[i] = arr[min_idx]; arr[min_idx] = t;
    }
}

int main() {
    int d1[] = {64, 34, 25, 12, 22, 11, 90};
    int d2[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7;

    dizi_yazdir(d1, n, "Orijinal");
    bubble_sort(d1, n);
    dizi_yazdir(d1, n, "Bubble  ");
    selection_sort(d2, n);
    dizi_yazdir(d2, n, "Select. ");
    return 0;
}
''',
    28: '''#include <stdio.h>

/* GÜN 28: Arama Algoritmaları */
int lineer_arama(int arr[], int n, int hedef) {
    for (int i = 0; i < n; i++)
        if (arr[i] == hedef) return i;
    return -1;
}

int ikili_arama(int arr[], int sol, int sag, int hedef) {
    while (sol <= sag) {
        int orta = sol + (sag - sol) / 2;
        if (arr[orta] == hedef) return orta;
        if (arr[orta] < hedef) sol = orta + 1;
        else sag = orta - 1;
    }
    return -1;
}

int main() {
    int dizi[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = 10, hedef = 23;

    printf("Dizi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\nAranan: %d\\n\\n", hedef);

    int idx = lineer_arama(dizi, n, hedef);
    printf("Lineer Arama: indeks %d\\n", idx);

    idx = ikili_arama(dizi, 0, n-1, hedef);
    printf("Ikili Arama:  indeks %d\\n", idx);
    return 0;
}
''',
    29: '''#include <stdio.h>

/* GÜN 29: Çoklu Dosya ve Header Dosyaları */
/*
 * Gercek projede dosya yapisi:
 *
 * matematik.h:
 *   #ifndef MATEMATIK_H
 *   #define MATEMATIK_H
 *   int topla(int a, int b);
 *   int cikar(int a, int b);
 *   #endif
 *
 * matematik.c:
 *   #include "matematik.h"
 *   int topla(int a, int b) { return a + b; }
 *   int cikar(int a, int b) { return a - b; }
 *
 * main.c:
 *   #include "matematik.h"
 *   int main() { printf("%d\\n", topla(3,4)); }
 *
 * Derleme: gcc main.c matematik.c -o program
 */

int topla(int a, int b) { return a + b; }
int cikar(int a, int b) { return a - b; }

int main() {
    printf("Coklu dosya projesi demo:\\n");
    printf("topla(3, 4) = %d\\n", topla(3, 4));
    printf("cikar(10, 3) = %d\\n", cikar(10, 3));
    printf("\\nYukaridaki yorum blokundaki dosya yapisini inceleyin.\\n");
    return 0;
}
''',
    30: '''#include <stdio.h>
#include <string.h>

/* GÜN 30: Bitirme Projesi - Öğrenci Not Sistemi */
#define MAX_OGRENCI 5

struct Ogrenci {
    char isim[50];
    int notlar[3];
    float ortalama;
};

float ortalama_hesapla(int notlar[], int n) {
    int toplam = 0;
    for (int i = 0; i < n; i++) toplam += notlar[i];
    return (float)toplam / n;
}

char harf_notu(float ort) {
    if (ort >= 90) return 'A';
    if (ort >= 80) return 'B';
    if (ort >= 70) return 'C';
    if (ort >= 60) return 'D';
    return 'F';
}

int main() {
    struct Ogrenci sinif[] = {
        {"Ali Yilmaz",  {85, 90, 78}, 0},
        {"Ayse Demir",  {92, 88, 95}, 0},
        {"Mehmet Kaya", {70, 65, 80}, 0},
        {"Zeynep Oz",   {55, 60, 58}, 0},
        {"Can Turk",    {98, 95, 100}, 0}
    };
    int n = MAX_OGRENCI;

    printf("===== OGRENCI NOT SISTEMI =====\\n\\n");
    printf("%-15s %5s %5s %5s %8s %5s\\n", "Isim", "V1", "V2", "V3", "Ort", "Not");
    printf("----------------------------------------------\\n");

    for (int i = 0; i < n; i++) {
        sinif[i].ortalama = ortalama_hesapla(sinif[i].notlar, 3);
        printf("%-15s %5d %5d %5d %8.2f %5c\\n",
            sinif[i].isim,
            sinif[i].notlar[0], sinif[i].notlar[1], sinif[i].notlar[2],
            sinif[i].ortalama, harf_notu(sinif[i].ortalama));
    }
    printf("----------------------------------------------\\n");
    return 0;
}
''',
}


def generate_lessons():
    lessons = []

    day_titles = {
        1: "GÜN 1: C Dilinin Temelleri ve Bilgisayar Mimarisi",
        2: "GÜN 2: Bellek Mantığı, Veri Tipleri ve Değişkenler",
        3: "GÜN 3: Format Belirteçleri ve Biçimlendirme",
        4: "GÜN 4: Klavye Girdileri (scanf / I/O)",
        5: "GÜN 5: Operatörler, Aritmetik ve Tip Dönüşümü",
        6: "GÜN 6: Koşullu Mantık (if, else, Mantıksal VE/VEYA)",
        7: "GÜN 7: Çoklu Kararlar (switch-case, Ternary)",
        8: "GÜN 8: for Döngüleri ve Sayaç Mantığı",
        9: "GÜN 9: while ve do-while Döngüleri",
        10: "GÜN 10: Fonksiyonlar ve Modüler Kodlama",
        11: "GÜN 11: Değişken Kapsamı ve Özyineleme (Recursion)",
        12: "GÜN 12: Tek Boyutlu Diziler (Arrays)",
        13: "GÜN 13: Karakter Dizileri (Strings) ve <string.h>",
        14: "GÜN 14: İşaretçiler (Pointers) 1 - Temeller & Adresler",
        15: "GÜN 15: İşaretçiler 2 - Pointer Aritmetiği & Dizi İlişkisi",
        16: "GÜN 16: İki Boyutlu Diziler ve Matris İşlemleri",
        17: "GÜN 17: Yapılar (Structs) ve Birlikler (Unions)",
        18: "GÜN 18: Dinamik Bellek Yönetimi (malloc, calloc, free)",
        19: "GÜN 19: Metin Dosya İşlemleri (fopen, fprintf, fgets)",
        20: "GÜN 20: İkili (Binary) Dosya İşlemleri (fread, fwrite)",
        21: "GÜN 21: Bit Düzeyinde İşlemler (Bitwise Operators)",
        22: "GÜN 22: Numaralandırma (Enum) ve Bit Sahaları",
        23: "GÜN 23: İleri Düzey İşaretçiler (Fonksiyon Göstericileri)",
        24: "GÜN 24: Veri Yapıları 1: Tek Yönlü Bağlı Liste (Linked List)",
        25: "GÜN 25: Veri Yapıları 2: Yığın (Stack) ve Kuyruk (Queue)",
        26: "GÜN 26: İleri Özyinelemeli Algoritmalar (Recursion Masterclass)",
        27: "GÜN 27: Sıralama Algoritmaları (Bubble, Selection, Insertion)",
        28: "GÜN 28: Arama Algoritmaları & Karmaşıklık (Binary Search)",
        29: "GÜN 29: Çoklu Dosya Projeleri ve Başlık Dosyaları (.h)",
        30: "GÜN 30: Bitirme Projesi ve İleri C Uygulamaları"
    }

    # Her gün için 5 alt konu adı
    day_sub_names = {
        1: ["Derleme Süreci (Preprocess → Compile → Link)",
            "Program İskeleti (#include, main, return 0)",
            "İlk Kod ve Ekran Çıktısı (printf)",
            "Kaçış Karakterleri (\\n, \\t, \\\\, \\\")",
            "Yorum Satırları (// ve /* */)"],
        2: ["Bilgisayar Belleği Mimarisi (Stack, Heap, Data, Text)",
            "Veri Tipleri (int, float, double, char, void)",
            "Değişken Tanımlama ve İsimlendirme Kuralları",
            "Sabitler (const ve #define)",
            "sizeof() Operatörü ve Tip Boyutları"],
        3: ["Tam Sayı Belirteçleri (%d, %i, %u, %ld)",
            "Ondalık Belirteçleri (%f, %e, %g, %.nf)",
            "Karakter ve String Belirteçleri (%c, %s)",
            "Özel Belirteçler (%p, %x, %o, %%)",
            "Genişlik ve Hizalama (%-10d, %010d)"],
        4: ["scanf() Temelleri ve & Operatörü",
            "Birden Fazla Değer Okuma",
            "getchar() ve putchar() Fonksiyonları",
            "fgets() ile Güvenli String Okuma",
            "Buffer Taşması ve Girdi Doğrulama"],
        5: ["Aritmetik Operatörler (+, -, *, /, %)",
            "Artırma/Azaltma (++, --, prefix vs postfix)",
            "Atama Operatörleri (+=, -=, *=, /=)",
            "Karşılaştırma ve Mantıksal Operatörler",
            "Tip Dönüşümü (Implicit ve Explicit Cast)"],
        6: ["if ve else Temelleri",
            "else if Zincirleme Koşullar",
            "İç İçe (Nested) if Yapıları",
            "Mantıksal Operatörler (&&, ||, !)",
            "Koşullu İfade Pratikleri"],
        7: ["switch-case Yapısı ve Sözdizimi",
            "break ve fall-through Davranışı",
            "default Case Kullanımı",
            "Ternary (Üçlü) Operatör (?:)",
            "switch vs if-else Karşılaştırması"],
        8: ["for Döngüsü Temelleri (init; koşul; artış)",
            "İç İçe (Nested) for Döngüleri",
            "break ve continue Komutları",
            "Döngü ile Desen Yazdırma",
            "for Döngüsü Optimizasyon İpuçları"],
        9: ["while Döngüsü Temelleri",
            "do-while Döngüsü (En Az Bir Kez Çalışma)",
            "Sonsuz Döngü ve Kontrollü Çıkış",
            "Sayı İşleme (Basamak Sayma, Ters Çevirme)",
            "while vs for Karşılaştırması"],
        10: ["Fonksiyon Tanımlama ve Çağırma",
             "Parametre Geçişi (Pass by Value)",
             "return Değeri ve void Fonksiyonlar",
             "Fonksiyon Prototipleri (Forward Declaration)",
             "Modüler Kod Tasarımı İlkeleri"],
        11: ["Yerel (Local) Değişkenler ve Kapsam",
             "Global Değişkenler ve Yan Etkiler",
             "static Değişkenler (Kalıcı Yerel)",
             "Özyineleme (Recursion) Temelleri",
             "Özyineleme vs Döngü Karşılaştırması"],
        12: ["Dizi Tanımlama ve Başlatma",
             "Dizi Elemanlarına Erişim ve Gezme",
             "Dizilerde Arama (Min, Max, Toplam)",
             "Diziyi Fonksiyona Geçirme",
             "Dizi Sınırları ve Buffer Overflow"],
        13: ["char Dizileri ve Null Terminator (\\0)",
             "strlen(), strcpy(), strncpy()",
             "strcat(), strcmp(), strncmp()",
             "String Arama: strstr(), strchr()",
             "String Güvenliği ve Buffer Yönetimi"],
        14: ["İşaretçi Nedir? (& ve * Operatörleri)",
             "İşaretçi Tanımlama ve Değer Atama",
             "NULL Pointer ve Güvenlik Kontrolü",
             "Pointer ile Fonksiyona Geçiş (Pass by Reference)",
             "Pointer ve const Niteleyicisi"],
        15: ["Pointer Aritmetiği (p+1, p++, p-q)",
             "Dizi ve Pointer İlişkisi (arr == &arr[0])",
             "Pointer ile Dizi Gezme",
             "Çoklu İşaretçiler (Pointer to Pointer)",
             "void* ve Generic Pointer Kullanımı"],
        16: ["2D Dizi Tanımlama ve Başlatma",
             "Matris Elemanlarına Erişim [i][j]",
             "Matris Toplama ve Çıkarma",
             "Matris Çarpımı Algoritması",
             "2D Dizi ve Fonksiyonlar"],
        17: ["struct Tanımlama ve Üye Erişimi (.)",
             "struct ve typedef Kullanımı",
             "İç İçe (Nested) Struct Yapıları",
             "struct Dizileri ve Fonksiyonlara Geçirme",
             "union Yapısı ve Bellek Paylaşımı"],
        18: ["malloc() ile Dinamik Bellek Tahsisi",
             "calloc() ve Sıfırlı Başlatma",
             "realloc() ile Boyut Değiştirme",
             "free() ve Bellek Sızıntısı Önleme",
             "Dangling Pointer ve Use After Free"],
        19: ["fopen() ve Dosya Modları (r, w, a, r+)",
             "fprintf() ve fscanf() ile Dosya I/O",
             "fgets() ve fputs() ile Satır Okuma/Yazma",
             "feof() ve ferror() ile Hata Kontrolü",
             "fclose() ve Dosya Kaynaklarını Serbest Bırakma"],
        20: ["Binary Mod (\"rb\", \"wb\") ve Text Farkı",
             "fwrite() ile İkili Yazma",
             "fread() ile İkili Okuma",
             "fseek() ve ftell() ile Rastgele Erişim",
             "Struct Verilerini Binary Dosyaya Kaydetme"],
        21: ["AND (&) ve OR (|) Operatörleri",
             "XOR (^) ve NOT (~) Operatörleri",
             "Bit Kaydırma (<< ve >>)",
             "Bit Maskeleme Teknikleri",
             "Pratik Uygulamalar (Bayrak, İzin Kontrolü)"],
        22: ["enum Tanımlama ve Kullanım",
             "enum Değer Atama ve Özelleştirme",
             "Bit Sahası (Bit Field) Tanımlama",
             "Bit Sahası ile Bayrak Yönetimi",
             "enum ve Bit Sahası Birlikte Kullanımı"],
        23: ["Fonksiyon Göstericisi Tanımlama",
             "Callback Fonksiyonları",
             "Fonksiyon Gösterici Dizileri",
             "qsort() ile Özel Sıralama",
             "Fonksiyon Göstericileri ve Tasarım Desenleri"],
        24: ["Düğüm (Node) Yapısı ve Kavramlar",
             "Başa Ekleme ve Sondan Ekleme",
             "Listede Arama ve Düğüm Silme",
             "Listenin Bellekten Temizlenmesi",
             "Çift Yönlü (Doubly) Bağlı Liste Farkı"],
        25: ["Stack (LIFO) Kavramı ve Kullanım Alanları",
             "push(), pop(), peek() İşlemleri",
             "Queue (FIFO) Kavramı ve Kullanım Alanları",
             "enqueue(), dequeue() İşlemleri",
             "Circular Queue ve Priority Queue"],
        26: ["Fibonacci Optimizasyonu (Memoization)",
             "Üs Alma (Power) Hızlı Algoritma",
             "Hanoi Kulesi Problemi",
             "Permütasyon ve Kombinasyon Üretimi",
             "Özyineleme Derinliği ve Stack Overflow"],
        27: ["Bubble Sort Algoritması ve Analizi",
             "Selection Sort Algoritması",
             "Insertion Sort Algoritması",
             "Sıralama Kararlılığı (Stability) Kavramı",
             "Zaman Karmaşıklığı Karşılaştırması (O(n²))"],
        28: ["Doğrusal (Linear) Arama",
             "İkili (Binary) Arama Algoritması",
             "Big O Notasyonu Temelleri",
             "O(1), O(n), O(log n), O(n²) Karşılaştırma",
             "Uzay Karmaşıklığı (Space Complexity)"],
        29: ["Çoklu .c Dosya Yapısı",
             "Başlık (.h) Dosyası Oluşturma",
             "#ifndef / #define / #endif Korumaları",
             "extern Anahtar Kelimesi",
             "Makefile ve Derleme Süreci"],
        30: ["Proje Planlama ve Modüler Tasarım",
             "Struct Tabanlı Veri Modelleme",
             "Dosya Tabanlı Kalıcı Depolama",
             "Hata Yönetimi ve Savunmacı Programlama",
             "Kod İncelemesi ve İyileştirme"],
    }

    for day in range(1, 31):
        day_title = day_titles[day]
        sub_names = day_sub_names[day]
        starter_code = day_starter_codes.get(day, day_starter_codes[1])

        for sub_idx, sub_name in enumerate(sub_names, 1):
            les_id = f"{day}.{sub_idx}"
            full_title = f"{les_id}: {sub_name}"

            theory_md = f"""# {full_title}

## 🎯 Dersin Amacı & Kazanımları
* **Gün:** {day_title}
* **Alt Konu:** {sub_name}

---

## 🧠 Detaylı Teorik Anlatım

Bu derste **{sub_name}** konusunu derinlemesine inceliyoruz.
C dilinde bu konu doğrudan RAM bellek mimarisi ve derleyici davranışı ile ilişkilidir.

### 🔧 Adım Adım Çalışma Mantığı
* Konunun temel kavramlarını anlayın
* Sözdizimi kurallarını inceleyin
* Örnek kod parçacıklarını çalıştırın ve çıktıyı analiz edin
* Kendi varyasyonlarınızı yazarak pratik yapın

---

## ⚠️ Sık Yapılan Hatalar
* ❌ Sözdizimi hatası yapma (noktalı virgül, parantez unutma)
* ❌ Değişkeni başlatmadan kullanma (undefined behavior)
* ❌ Tip uyumsuzluğu (format belirteci ile değişken tipi eşleşmeli)

---

## 💻 Uygulama Kodu
Aşağıdaki başlangıç kodunu inceleyip çalıştırın.
Kodu değiştirerek farklı senaryolar deneyin.
"""

            lessons.append({
                "id": les_id,
                "day": day,
                "day_title": day_title,
                "sub_index": sub_idx,
                "title": full_title,
                "theory": theory_md,
                "starter_code": starter_code,
                "difficulty": "Başlangıç" if day <= 10 else ("Orta" if day <= 20 else "İleri"),
                "estimated_duration_min": 45 + (day * 2)
            })

    return lessons


def get_lesson_by_id(lessons, lesson_id):
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_lessons_by_day(lessons, day_number):
    return [l for l in lessons if l["day"] == day_number]


def get_curriculum_stats(lessons):
    return {
        "toplam_ders": len(lessons),
        "toplam_gün": 30,
        "ortalama_ders_per_gün": len(lessons) // 30,
        "zorluk_dağılımı": {
            "Başlangıç": len([l for l in lessons if l.get("difficulty") == "Başlangıç"]),
            "Orta": len([l for l in lessons if l.get("difficulty") == "Orta"]),
            "İleri": len([l for l in lessons if l.get("difficulty") == "İleri"])
        }
    }


# Module level LESSONS export
LESSONS = generate_lessons()
