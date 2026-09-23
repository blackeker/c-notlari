# -*- coding: utf-8 -*-
"""
C Dili Şablon & Algoritma Kütüphanesi Modülü (Snippets Data)
20 İleri Düzey Derlemeye Hazır Algoritma Şablonu İçerir.
"""

SNIPPETS = [
    {
        "id": "matrix_mult",
        "title": "İki Matrisin Çarpımı (Matrix Multiplication)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

#define N 3

void matris_carp(int A[N][N], int B[N][N], int C[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = 0;
            for (int k = 0; k < N; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    int A[N][N] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    int B[N][N] = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}; // Birim Matris
    int C[N][N];

    matris_carp(A, B, C);

    printf("Matris Carpim Sonucu:\\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%4d ", C[i][j]);
        }
        printf("\\n");
    }
    return 0;
}
"""
    },
    {
        "id": "quicksort",
        "title": "Hızlı Sıralama (QuickSort Algoritması)",
        "category": "Sıralama Algoritmaları",
        "code": """#include <stdio.h>

void takas(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int bolumle(int arr[], int dusuk, int yuksek) {
    int pivot = arr[yuksek];
    int i = (dusuk - 1);

    for (int j = dusuk; j <= yuksek - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            takas(&arr[i], &arr[j]);
        }
    }
    takas(&arr[i + 1], &arr[yuksek]);
    return (i + 1);
}

void quicksort(int arr[], int dusuk, int yuksek) {
    if (dusuk < yuksek) {
        int pi = bolumle(arr, dusuk, yuksek);
        quicksort(arr, dusuk, pi - 1);
        quicksort(arr, pi + 1, yuksek);
    }
}

int main() {
    int dizi[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(dizi) / sizeof(dizi[0]);

    printf("Orijinal Dizi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    quicksort(dizi, 0, n - 1);

    printf("QuickSort Sonrasi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    return 0;
}
"""
    },
    {
        "id": "linked_list",
        "title": "Tek Yönlü Bağlı Liste (Singly Linked List)",
        "category": "Veri Yapıları",
        "code": """#include <stdio.h>
#include <stdlib.h>

struct Dugum {
    int veri;
    struct Dugum* sonraki;
};

void ekle_basa(struct Dugum** bas_ref, int yeni_veri) {
    struct Dugum* yeni_dugum = (struct Dugum*)malloc(sizeof(struct Dugum));
    yeni_dugum->veri = yeni_veri;
    yeni_dugum->sonraki = (*bas_ref);
    (*bas_ref) = yeni_dugum;
}

void yazdir(struct Dugum* dugum) {
    printf("Bağlı Liste: ");
    while (dugum != NULL) {
        printf("%d -> ", dugum->veri);
        dugum = dugum->sonraki;
    }
    printf("NULL\\n");
}

int main() {
    struct Dugum* bas = NULL;

    ekle_basa(&bas, 30);
    ekle_basa(&bas, 20);
    ekle_basa(&bas, 10);

    yazdir(bas);

    // Bellek temizliği
    struct Dugum* gecici;
    while (bas != NULL) {
        gecici = bas;
        bas = bas->sonraki;
        free(gecici);
    }

    return 0;
}
"""
    },
    {
        "id": "binary_search",
        "title": "İkili Arama (Binary Search Algoritması)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

int ikili_arama(int arr[], int sol, int sag, int aranan) {
    while (sol <= sag) {
        int orta = sol + (sag - sol) / 2;

        if (arr[orta] == aranan) return orta;
        if (arr[orta] < aranan) sol = orta + 1;
        else sag = orta - 1;
    }
    return -1;
}

int main() {
    int dizi[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = sizeof(dizi) / sizeof(dizi[0]);
    int aranan = 23;

    int sonuc = ikili_arama(dizi, 0, n - 1, aranan);

    if (sonuc != -1) printf("Eleman %d. indekste bulundu!\\n", sonuc);
    else printf("Eleman dizide bulunamadi.\\n");

    return 0;
}
"""
    },
    {
        "id": "binary_file_io",
        "title": "İkili (Binary) Dosya Okuma & Yazma",
        "category": "Dosya İşlemleri",
        "code": """#include <stdio.h>

typedef struct {
    int id;
    char ad[30];
    float maas;
} Personel;

int main() {
    Personel p1 = {101, "Ahmet Yilmaz", 45000.50f};

    // Dosyaya Yazma
    FILE *f_out = fopen("personel.bin", "wb");
    if (f_out != NULL) {
        fwrite(&p1, sizeof(Personel), 1, f_out);
        fclose(f_out);
        printf("Personel kaydi bin dosyaya yazildi!\\n");
    }

    // Dosyadan Okuma
    Personel p_oku;
    FILE *f_in = fopen("personel.bin", "rb");
    if (f_in != NULL) {
        fread(&p_oku, sizeof(Personel), 1, f_in);
        fclose(f_in);
        printf("\\nOkunan Personel:\\nID: %d\\nAd: %s\\nMaas: %.2f TL\\n", p_oku.id, p_oku.ad, p_oku.maas);
    }

    return 0;
}
"""
    },
    {
        "id": "bubble_sort",
        "title": "Kabarcık Sıralaması (Bubble Sort)",
        "category": "Sıralama Algoritmaları",
        "code": """#include <stdio.h>

void takas(int *a, int *b) {
    int gecici = *a;
    *a = *b;
    *b = gecici;
}

void bubble_sort(int dizi[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int degisim_oldu = 0;
        for (int j = 0; j < n - 1 - i; j++) {
            if (dizi[j] > dizi[j + 1]) {
                takas(&dizi[j], &dizi[j + 1]);
                degisim_oldu = 1;
            }
        }
        if (degisim_oldu == 0) break; // Dizi sıralandıysa erken çıkış
    }
}

int main() {
    int dizi[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(dizi) / sizeof(dizi[0]);

    printf("Orijinal Dizi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    bubble_sort(dizi, n);

    printf("Bubble Sort Sonrasi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    return 0;
}
"""
    },
    {
        "id": "selection_sort",
        "title": "Seçmeli Sıralama (Selection Sort)",
        "category": "Sıralama Algoritmaları",
        "code": """#include <stdio.h>

void takas(int *a, int *b) {
    int gecici = *a;
    *a = *b;
    *b = gecici;
}

void selection_sort(int dizi[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_indeks = i;
        for (int j = i + 1; j < n; j++) {
            if (dizi[j] < dizi[min_indeks]) {
                min_indeks = j;
            }
        }
        if (min_indeks != i) {
            takas(&dizi[i], &dizi[min_indeks]);
        }
    }
}

int main() {
    int dizi[] = {29, 10, 14, 37, 13};
    int n = sizeof(dizi) / sizeof(dizi[0]);

    printf("Orijinal Dizi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    selection_sort(dizi, n);

    printf("Selection Sort Sonrasi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    return 0;
}
"""
    },
    {
        "id": "insertion_sort",
        "title": "Araya Ekleme Sıralaması (Insertion Sort)",
        "category": "Sıralama Algoritmaları",
        "code": """#include <stdio.h>

void insertion_sort(int dizi[], int n) {
    for (int i = 1; i < n; i++) {
        int anahtar = dizi[i];
        int j = i - 1;

        while (j >= 0 && dizi[j] > anahtar) {
            dizi[j + 1] = dizi[j];
            j--;
        }
        dizi[j + 1] = anahtar;
    }
}

int main() {
    int dizi[] = {12, 11, 13, 5, 6};
    int n = sizeof(dizi) / sizeof(dizi[0]);

    printf("Orijinal Dizi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    insertion_sort(dizi, n);

    printf("Insertion Sort Sonrasi: ");
    for (int i = 0; i < n; i++) printf("%d ", dizi[i]);
    printf("\\n");

    return 0;
}
"""
    },
    {
        "id": "stack_array",
        "title": "Dizi Tabanlı Yığın (Array-based Stack)",
        "category": "Veri Yapıları",
        "code": """#include <stdio.h>
#include <stdbool.h>

#define KAPASITE 5

typedef struct {
    int veriler[KAPASITE];
    int tepe;
} Yigin;

void yigin_olustur(Yigin *y) {
    y->tepe = -1;
}

bool dolu_mu(Yigin *y) {
    return y->tepe == KAPASITE - 1;
}

bool bos_mu(Yigin *y) {
    return y->tepe == -1;
}

bool push(Yigin *y, int veri) {
    if (dolu_mu(y)) {
        printf("Hata: Yigin dolu (Stack Overflow)!\\n");
        return false;
    }
    y->veriler[++(y->tepe)] = veri;
    printf("%d yigina eklendi.\\n", veri);
    return true;
}

int pop(Yigin *y) {
    if (bos_mu(y)) {
        printf("Hata: Yigin bos (Stack Underflow)!\\n");
        return -1;
    }
    return y->veriler[(y->tepe)--];
}

int peek(Yigin *y) {
    if (bos_mu(y)) {
        printf("Hata: Yigin bos!\\n");
        return -1;
    }
    return y->veriler[y->tepe];
}

int main() {
    Yigin y;
    yigin_olustur(&y);

    push(&y, 10);
    push(&y, 20);
    push(&y, 30);

    printf("Tepedeki eleman (peek): %d\\n", peek(&y));
    printf("Cikarilan eleman (pop): %d\\n", pop(&y));
    printf("Cikarilan eleman (pop): %d\\n", pop(&y));
    printf("Guncel tepe elemani: %d\\n", peek(&y));

    return 0;
}
"""
    },
    {
        "id": "queue_array",
        "title": "Dizi Tabanlı Dairesel Kuyruk (Array-based Queue)",
        "category": "Veri Yapıları",
        "code": """#include <stdio.h>
#include <stdbool.h>

#define KAPASITE 5

typedef struct {
    int veriler[KAPASITE];
    int bas;
    int son;
    int eleman_sayisi;
} Kuyruk;

void kuyruk_olustur(Kuyruk *k) {
    k->bas = 0;
    k->son = -1;
    k->eleman_sayisi = 0;
}

bool dolu_mu(Kuyruk *k) {
    return k->eleman_sayisi == KAPASITE;
}

bool bos_mu(Kuyruk *k) {
    return k->eleman_sayisi == 0;
}

bool enqueue(Kuyruk *k, int veri) {
    if (dolu_mu(k)) {
        printf("Hata: Kuyruk dolu!\\n");
        return false;
    }
    k->son = (k->son + 1) % KAPASITE;
    k->veriler[k->son] = veri;
    k->eleman_sayisi++;
    printf("%d kuyruga eklendi.\\n", veri);
    return true;
}

int dequeue(Kuyruk *k) {
    if (bos_mu(k)) {
        printf("Hata: Kuyruk bos!\\n");
        return -1;
    }
    int cikarilan = k->veriler[k->bas];
    k->bas = (k->bas + 1) % KAPASITE;
    k->eleman_sayisi--;
    return cikarilan;
}

int front(Kuyruk *k) {
    if (bos_mu(k)) {
        printf("Hata: Kuyruk bos!\\n");
        return -1;
    }
    return k->veriler[k->bas];
}

int main() {
    Kuyruk k;
    kuyruk_olustur(&k);

    enqueue(&k, 100);
    enqueue(&k, 200);
    enqueue(&k, 300);

    printf("Kuyruk basindaki eleman: %d\\n", front(&k));
    printf("Kuyruktan cikarildi: %d\\n", dequeue(&k));
    printf("Kuyruktan cikarildi: %d\\n", dequeue(&k));

    enqueue(&k, 400);
    enqueue(&k, 500);

    printf("Guncel kuyruk basi: %d\\n", front(&k));

    return 0;
}
"""
    },
    {
        "id": "fibonacci",
        "title": "Fibonacci Sayıları (İteratif ve Özyinelemeli)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

long long fibonacci_ozyinelemeli(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci_ozyinelemeli(n - 1) + fibonacci_ozyinelemeli(n - 2);
}

long long fibonacci_iteratif(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    long long onceki = 0, simdiki = 1, sonraki;
    for (int i = 2; i <= n; i++) {
        sonraki = onceki + simdiki;
        onceki = simdiki;
        simdiki = sonraki;
    }
    return simdiki;
}

int main() {
    int terim_sayisi = 10;

    printf("--- Ilk %d Fibonacci Sayisi (Iteratif) ---\\n", terim_sayisi);
    for (int i = 0; i < terim_sayisi; i++) {
        printf("%lld ", fibonacci_iteratif(i));
    }
    printf("\\n\\n");

    printf("--- Ozyinelemeli (Recursive) Dogrulama ---\\n");
    for (int i = 0; i < terim_sayisi; i++) {
        printf("F(%d) = %lld\\n", i, fibonacci_ozyinelemeli(i));
    }

    return 0;
}
"""
    },
    {
        "id": "string_reverse",
        "title": "Yerinde Metin Ters Çevirme (In-place String Reversal)",
        "category": "Metin İşleme",
        "code": """#include <stdio.h>
#include <string.h>

void metin_ters_cevir(char *str) {
    if (str == NULL) return;

    int sol = 0;
    int sag = strlen(str) - 1;

    while (sol < sag) {
        char gecici = str[sol];
        str[sol] = str[sag];
        str[sag] = gecici;

        sol++;
        sag--;
    }
}

int main() {
    char cumle[] = "C Programlama Dili 2026";

    printf("Orijinal Metin : %s\\n", cumle);

    metin_ters_cevir(cumle);

    printf("Ters Cevrilmis  : %s\\n", cumle);

    return 0;
}
"""
    },
    {
        "id": "caesar_cipher",
        "title": "Sezar Şifreleme ve Deşifreleme (Caesar Cipher)",
        "category": "Metin İşleme",
        "code": """#include <stdio.h>
#include <ctype.h>
#include <string.h>

void sezari_sifrele(char *metin, int anahtar) {
    anahtar = anahtar % 26;
    for (int i = 0; metin[i] != '\\0'; i++) {
        if (isupper((unsigned char)metin[i])) {
            metin[i] = (metin[i] - 'A' + anahtar) % 26 + 'A';
        } else if (islower((unsigned char)metin[i])) {
            metin[i] = (metin[i] - 'a' + anahtar) % 26 + 'a';
        }
    }
}

void sezari_coz(char *metin, int anahtar) {
    anahtar = anahtar % 26;
    sezari_sifrele(metin, 26 - anahtar);
}

int main() {
    char mesaj[100] = "Merhaba Dunya! C ile Kriptografi.";
    int anahtar = 3;

    printf("Orijinal Metin : %s\\n", mesaj);

    sezari_sifrele(mesaj, anahtar);
    printf("Sifreli Metin  : %s\\n", mesaj);

    sezari_coz(mesaj, anahtar);
    printf("Cozulmus Metin : %s\\n", mesaj);

    return 0;
}
"""
    },
    {
        "id": "file_copy",
        "title": "Metin Dosyası Kopyalama (Text File Copy)",
        "category": "Dosya İşlemleri",
        "code": """#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *kaynak_adi = "kaynak.txt";
    const char *hedef_adi = "hedef_kopya.txt";

    // Ornek kaynak dosya olusturalim
    FILE *f_kaynak = fopen(kaynak_adi, "w");
    if (f_kaynak == NULL) {
        perror("Kaynak dosya olusturulamadi");
        return 1;
    }
    fprintf(f_kaynak, "Bu metin C dosyasi kopyalama ornegidir.\\nSatir 2: Basariyla kopyalandi!\\n");
    fclose(f_kaynak);

    // Kopyalama islemi: kaynaktan oku, hedefe yaz
    FILE *kaynak = fopen(kaynak_adi, "r");
    if (kaynak == NULL) {
        perror("Kaynak dosya acilamadi");
        return 1;
    }

    FILE *hedef = fopen(hedef_adi, "w");
    if (hedef == NULL) {
        perror("Hedef dosya acilamadi");
        fclose(kaynak);
        return 1;
    }

    int ch;
    long bayt_sayisi = 0;
    while ((ch = fgetc(kaynak)) != EOF) {
        fputc(ch, hedef);
        bayt_sayisi++;
    }

    fclose(kaynak);
    fclose(hedef);

    printf("Dosya kopyalama tamamlandi!\\n");
    printf("Toplam %ld bayt basariyla '%s' dosyasina aktarildi.\\n", bayt_sayisi, hedef_adi);

    return 0;
}
"""
    },
    {
        "id": "dynamic_array",
        "title": "Dinamik Büyüyen Dizi (Auto-resizing Dynamic Array)",
        "category": "Dinamik Bellek",
        "code": """#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *veriler;
    int boyut;
    int kapasite;
} DinamikDizi;

DinamikDizi* dinamik_dizi_olustur(int baslangic_kapasite) {
    DinamikDizi *dizi = (DinamikDizi*)malloc(sizeof(DinamikDizi));
    if (dizi == NULL) return NULL;

    dizi->veriler = (int*)malloc(sizeof(int) * baslangic_kapasite);
    if (dizi->veriler == NULL) {
        free(dizi);
        return NULL;
    }
    dizi->boyut = 0;
    dizi->kapasite = baslangic_kapasite;
    return dizi;
}

void eleman_ekle(DinamikDizi *dizi, int deger) {
    if (dizi->boyut >= dizi->kapasite) {
        int yeni_kapasite = dizi->kapasite * 2;
        int *yeni_alan = (int*)realloc(dizi->veriler, sizeof(int) * yeni_kapasite);
        if (yeni_alan == NULL) {
            printf("Bellek genisletme hatasi!\\n");
            return;
        }
        dizi->veriler = yeni_alan;
        dizi->kapasite = yeni_kapasite;
        printf("[Kapasite Arttirildi]: Yeni Kapasite = %d\\n", dizi->kapasite);
    }
    dizi->veriler[dizi->boyut++] = deger;
}

void dinamik_dizi_yazdir(const DinamikDizi *dizi) {
    printf("Dizi (Boyut: %d / Kapasite: %d): [ ", dizi->boyut, dizi->kapasite);
    for (int i = 0; i < dizi->boyut; i++) {
        printf("%d ", dizi->veriler[i]);
    }
    printf("]\\n");
}

void dinamik_dizi_serbest_birak(DinamikDizi *dizi) {
    if (dizi != NULL) {
        free(dizi->veriler);
        free(dizi);
    }
}

int main() {
    DinamikDizi *liste = dinamik_dizi_olustur(2);

    eleman_ekle(liste, 10);
    dinamik_dizi_yazdir(liste);

    eleman_ekle(liste, 20);
    dinamik_dizi_yazdir(liste);

    eleman_ekle(liste, 30); // Kapasite 2 -> 4 katlanir
    dinamik_dizi_yazdir(liste);

    eleman_ekle(liste, 40);
    eleman_ekle(liste, 50); // Kapasite 4 -> 8 katlanir
    dinamik_dizi_yazdir(liste);

    dinamik_dizi_serbest_birak(liste);
    return 0;
}
"""
    },
    {
        "id": "hash_table",
        "title": "Açık Adreslemeli Hash Tablosu (Open Addressing Hash Table)",
        "category": "Veri Yapıları",
        "code": """#include <stdio.h>
#include <stdbool.h>

#define TABLO_BOYUTU 10

typedef struct {
    int anahtar;
    int deger;
    bool dolu;
} HashElemani;

typedef struct {
    HashElemani elemanlar[TABLO_BOYUTU];
} HashTablosu;

int hash_fonksiyonu(int anahtar) {
    return (anahtar >= 0 ? anahtar : -anahtar) % TABLO_BOYUTU;
}

void hash_baslat(HashTablosu *ht) {
    for (int i = 0; i < TABLO_BOYUTU; i++) {
        ht->elemanlar[i].dolu = false;
    }
}

bool hash_ekle(HashTablosu *ht, int anahtar, int deger) {
    int indeks = hash_fonksiyonu(anahtar);
    int baslangic = indeks;

    while (ht->elemanlar[indeks].dolu) {
        if (ht->elemanlar[indeks].anahtar == anahtar) {
            ht->elemanlar[indeks].deger = deger; // Guncelle
            return true;
        }
        indeks = (indeks + 1) % TABLO_BOYUTU; // Dogrusal yoklama
        if (indeks == baslangic) {
            printf("Hash tablosu tamamen dolu!\\n");
            return false;
        }
    }

    ht->elemanlar[indeks].anahtar = anahtar;
    ht->elemanlar[indeks].deger = deger;
    ht->elemanlar[indeks].dolu = true;
    return true;
}

int hash_ara(HashTablosu *ht, int anahtar, bool *bulundu) {
    int indeks = hash_fonksiyonu(anahtar);
    int baslangic = indeks;

    while (ht->elemanlar[indeks].dolu) {
        if (ht->elemanlar[indeks].anahtar == anahtar) {
            *bulundu = true;
            return ht->elemanlar[indeks].deger;
        }
        indeks = (indeks + 1) % TABLO_BOYUTU;
        if (indeks == baslangic) break;
    }

    *bulundu = false;
    return -1;
}

void hash_yazdir(HashTablosu *ht) {
    printf("--- Hash Tablosu (Dogrusal Yoklama) ---\\n");
    for (int i = 0; i < TABLO_BOYUTU; i++) {
        if (ht->elemanlar[i].dolu) {
            printf("[%d] -> Anahtar: %d, Deger: %d\\n", i, ht->elemanlar[i].anahtar, ht->elemanlar[i].deger);
        } else {
            printf("[%d] -> [BOS]\\n", i);
        }
    }
}

int main() {
    HashTablosu ht;
    hash_baslat(&ht);

    hash_ekle(&ht, 15, 1500);
    hash_ekle(&ht, 25, 2500); // 15 ile ayni hash degerine sahiptir (cakisma cozumu: indeks 6)
    hash_ekle(&ht, 35, 3500);
    hash_ekle(&ht, 7, 700);

    hash_yazdir(&ht);

    bool bulundu;
    int sonuc = hash_ara(&ht, 25, &bulundu);
    if (bulundu) {
        printf("\\nAnahtar 25 bulundu! Deger: %d\\n", sonuc);
    } else {
        printf("\\nAnahtar bulunamadi.\\n");
    }

    return 0;
}
"""
    },
    {
        "id": "matrix_transpose",
        "title": "Matris Transpozesi (Matrix Transpose)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

#define SATIR 3
#define SUTUN 4

void transpoze_al(int A[SATIR][SUTUN], int T[SUTUN][SATIR]) {
    for (int i = 0; i < SATIR; i++) {
        for (int j = 0; j < SUTUN; j++) {
            T[j][i] = A[i][j];
        }
    }
}

int main() {
    int A[SATIR][SUTUN] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int T[SUTUN][SATIR];

    printf("Orijinal Matris (%dx%d):\\n", SATIR, SUTUN);
    for (int i = 0; i < SATIR; i++) {
        for (int j = 0; j < SUTUN; j++) {
            printf("%4d ", A[i][j]);
        }
        printf("\\n");
    }

    transpoze_al(A, T);

    printf("\\nTranspoze Matris (%dx%d):\\n", SUTUN, SATIR);
    for (int i = 0; i < SUTUN; i++) {
        for (int j = 0; j < SATIR; j++) {
            printf("%4d ", T[i][j]);
        }
        printf("\\n");
    }

    return 0;
}
"""
    },
    {
        "id": "gcd_lcm",
        "title": "EBOB ve EKOK Hesaplama (Öklid Algoritması)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

long long ebob(long long a, long long b) {
    while (b != 0) {
        long long kalan = a % b;
        a = b;
        b = kalan;
    }
    return (a >= 0) ? a : -a;
}

long long ekok(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / ebob(a, b)) * b;
}

int main() {
    long long sayi1 = 48;
    long long sayi2 = 18;

    long long ortak_bolen = ebob(sayi1, sayi2);
    long long ortak_kat = ekok(sayi1, sayi2);

    printf("Sayi 1: %lld, Sayi 2: %lld\\n", sayi1, sayi2);
    printf("EBOB (GCD): %lld\\n", ortak_bolen);
    printf("EKOK (LCM): %lld\\n", ortak_kat);

    return 0;
}
"""
    },
    {
        "id": "tower_of_hanoi",
        "title": "Hanoi Kuleleri (Tower of Hanoi)",
        "category": "Matematik & Diziler",
        "code": """#include <stdio.h>

void hanoi(int disk_sayisi, char kaynak, char hedef, char yardimci, int *hamle_sayisi) {
    if (disk_sayisi == 1) {
        (*hamle_sayisi)++;
        printf("Hamle %2d: Disk 1, %c direginden %c diregine tasindi.\\n", *hamle_sayisi, kaynak, hedef);
        return;
    }

    hanoi(disk_sayisi - 1, kaynak, yardimci, hedef, hamle_sayisi);

    (*hamle_sayisi)++;
    printf("Hamle %2d: Disk %d, %c direginden %c diregine tasindi.\\n", *hamle_sayisi, disk_sayisi, kaynak, hedef);

    hanoi(disk_sayisi - 1, yardimci, hedef, kaynak, hamle_sayisi);
}

int main() {
    int disk_sayisi = 3;
    int toplam_hamle = 0;

    printf("--- %d Diskli Hanoi Kuleleri Cozumu ---\\n", disk_sayisi);
    hanoi(disk_sayisi, 'A', 'C', 'B', &toplam_hamle);

    printf("\\nCozum tamamlandi! Toplam hamle sayisi: %d\\n", toplam_hamle);

    return 0;
}
"""
    },
    {
        "id": "palindrome_checker",
        "title": "Palindrom Kontrolü (Palindrome Checker)",
        "category": "Metin İşleme",
        "code": """#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool palindrom_mu(const char *metin) {
    int sol = 0;
    int sag = strlen(metin) - 1;

    while (sol < sag) {
        while (sol < sag && !isalnum((unsigned char)metin[sol])) sol++;
        while (sol < sag && !isalnum((unsigned char)metin[sag])) sag--;

        if (tolower((unsigned char)metin[sol]) != tolower((unsigned char)metin[sag])) {
            return false;
        }

        sol++;
        sag--;
    }

    return true;
}

int main() {
    const char *test1 = "Ey Edip Adanada Pide Ye";
    const char *test2 = "programlama";
    const char *test3 = "Kac kak";

    printf("\\"%s\\" -> %s\\n", test1, palindrom_mu(test1) ? "Palindromdur!" : "Palindrom degildir.");
    printf("\\"%s\\" -> %s\\n", test2, palindrom_mu(test2) ? "Palindromdur!" : "Palindrom degildir.");
    printf("\\"%s\\" -> %s\\n", test3, palindrom_mu(test3) ? "Palindromdur!" : "Palindrom degildir.");

    return 0;
}
"""
    }
]
