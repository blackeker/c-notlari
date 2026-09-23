# -*- coding: utf-8 -*-
"""
C Dili Standart Kütüphaneler ve Hızlı Referans Rehberi (Cheat Sheet Data)
12 Temel Standart Kütüphane ve Sık Kullanılan Fonksiyon/Makro Referansı İçerir.
"""

CHEATSHEET = [
    {
        "library": "<stdio.h>",
        "desc": "Standart Giriş / Çıkış Kütüphanesi",
        "functions": [
            {"name": "printf(\"fmt\", ...)", "desc": "Ekrana biçimlendirilmiş metin yazdırır."},
            {"name": "scanf(\"fmt\", &var)", "desc": "Klavyeden biçimlendirilmiş veri okur."},
            {"name": "puts(\"str\")", "desc": "Ekrana string yazdırıp sonuna \\n ekler."},
            {"name": "getchar()", "desc": "Klavyeden tek bir karakter okur."},
            {"name": "fgets(str, n, stdin)", "desc": "Klavyeden güvenli bir şekilde satır okur."}
        ]
    },
    {
        "library": "<string.h>",
        "desc": "Karakter Dizisi (String) İşleme Kütüphanesi",
        "functions": [
            {"name": "strlen(str)", "desc": "String'in karakter uzunluğunu hesaplar ('\\0' hariç)."},
            {"name": "strcpy(dest, src)", "desc": "src metnini dest dizisine kopyalar."},
            {"name": "strcat(s1, s2)", "desc": "s2 metnini s1'in sonuna ekler."},
            {"name": "strcmp(s1, s2)", "desc": "İki metni alfabetik karşılaştırır (Eşitse 0 döner)."},
            {"name": "strstr(haystack, needle)", "desc": "Metin içinde alt metin arar."}
        ]
    },
    {
        "library": "<stdlib.h>",
        "desc": "Genel Amaçlı Utiliteler ve Dinamik Bellek",
        "functions": [
            {"name": "malloc(size)", "desc": "Heap alanından belirtilen bayt kadar bellek tahsis eder."},
            {"name": "free(ptr)", "desc": "Tahsis edilmiş dinamik belleği serbest bırakır."},
            {"name": "rand()", "desc": "Rastgele tamsayı üretir."},
            {"name": "atoi(str)", "desc": "String ifadeyi tam sayıya (int) dönüştürür."},
            {"name": "exit(code)", "desc": "Programı belirtilen kod ile derhal sonlandırır."}
        ]
    },
    {
        "library": "<math.h>",
        "desc": "Matematiksel Fonksiyonlar",
        "functions": [
            {"name": "pow(base, exp)", "desc": "Üs alma işlemi yapar (base^exp)."},
            {"name": "sqrt(x)", "desc": "Karekök hesaplar."},
            {"name": "abs(x) / fabsf(x)", "desc": "Mutlak değer alır."},
            {"name": "ceil(x) / floor(x)", "desc": "Yukarı / Aşağı tam sayıya yuvarlar."},
            {"name": "sin(x) / cos(x)", "desc": "Trigonometrik radyan hesapları yapar."}
        ]
    },
    {
        "library": "<stdbool.h>",
        "desc": "Mantıksal Türler (C99)",
        "functions": [
            {"name": "bool", "desc": "Mantıksal veri tipi (true veya false)."},
            {"name": "true", "desc": "1 (Doğru) sabitini temsil eder."},
            {"name": "false", "desc": "0 (Yanlış) sabitini temsil eder."}
        ]
    },
    {
        "library": "<ctype.h>",
        "desc": "Karakter Sınıflandırma ve Dönüştürme Fonksiyonları",
        "functions": [
            {"name": "isalpha(c)", "desc": "Karakterin alfabetik harf olup olmadığını denetler ('a'-'z', 'A'-'Z')."},
            {"name": "isdigit(c)", "desc": "Karakterin rakam olup olmadığını denetler ('0'-'9')."},
            {"name": "isalnum(c)", "desc": "Karakterin alfanümerik (harf veya rakam) olup olmadığını denetler."},
            {"name": "isspace(c)", "desc": "Karakterin boşluk, tab ya da yeni satır karakteri olup olmadığını denetler."},
            {"name": "isupper(c) / islower(c)", "desc": "Karakterin büyük harf / küçük harf olup olmadığını denetler."},
            {"name": "toupper(c)", "desc": "Küçük harf karakteri büyük harfe dönüştürür."},
            {"name": "tolower(c)", "desc": "Büyük harf karakteri küçük harfe dönüştürür."}
        ]
    },
    {
        "library": "<time.h>",
        "desc": "Tarih ve Zaman İşlemleri Kütüphanesi",
        "functions": [
            {"name": "time(NULL)", "desc": "1 Ocak 1970'ten (Epoch) bu yana geçen süreyi saniye (time_t) cinsinden verir."},
            {"name": "clock()", "desc": "Programın başlangıcından itibaren harcanan işlemci (CPU) süresini saat vuruşu cinsinden döndürür."},
            {"name": "difftime(t2, t1)", "desc": "İki time_t zaman değeri arasındaki farkı saniye (double) cinsinden hesaplar."},
            {"name": "localtime(&t)", "desc": "time_t değerini yerel saat dilimine göre yapılandırılmış struct tm işaretçisine çevirir."},
            {"name": "strftime(s, max, fmt, tm)", "desc": "struct tm zaman yapısını belirtilen formatta metne (string) dönüştürür."},
            {"name": "asctime(tm) / ctime(&t)", "desc": "Tarih ve saati okunabilir standart metin biçimine çevirir."}
        ]
    },
    {
        "library": "<limits.h>",
        "desc": "Tamsayı Türlerinin Donanımsal Sınır Değerleri ve Sabitleri",
        "functions": [
            {"name": "CHAR_MIN / CHAR_MAX", "desc": "İşaretli char türünün alabileceği minimum (-128) ve maksimum (127) değerler."},
            {"name": "INT_MIN / INT_MAX", "desc": "Standart int türünün minimum (-2147483648) ve maksimum (2147483647) sınırları."},
            {"name": "UINT_MAX", "desc": "İşaretsiz int (unsigned int) türünün alabileceği maksimum değer (4294967295)."},
            {"name": "LONG_MIN / LONG_MAX", "desc": "Long int türünün temsil edebileceği minimum ve maksimum değerler."},
            {"name": "SHRT_MIN / SHRT_MAX", "desc": "Short tamsayı türünün minimum (-32768) ve maksimum (32767) sınırları."},
            {"name": "LLONG_MIN / LLONG_MAX", "desc": "64-bit long long int türünün minimum ve maksimum sınır değerleri."}
        ]
    },
    {
        "library": "<float.h>",
        "desc": "Kayan Noktalı (Floating Point) Sayı Sınırları ve Hassasiyetleri",
        "functions": [
            {"name": "FLT_MIN / FLT_MAX", "desc": "Tek duyarlıklı float türünün alabileceği minimum pozitif ve maksimum değerler."},
            {"name": "DBL_MIN / DBL_MAX", "desc": "Çift duyarlıklı double türünün alabileceği minimum pozitif ve maksimum değerler."},
            {"name": "FLT_EPSILON / DBL_EPSILON", "desc": "1.0 sayısı ile 1.0'dan büyük en yakın temsil edilebilir sayı arasındaki fark (makine hassasiyeti)."},
            {"name": "FLT_DIG / DBL_DIG", "desc": "Kayıp olmadan saklanabilen anlamlı ondalık basamak sayısı (float için 6, double için 15)."},
            {"name": "LDBL_MAX", "desc": "Genişletilmiş duyarlıklı long double türünün maksimum değeri."}
        ]
    },
    {
        "library": "<assert.h>",
        "desc": "Program Doğrulama ve Hata Ayıklama Makroları",
        "functions": [
            {"name": "assert(ifade)", "desc": "İfade yanlış (0) ise dosya adı ve satır numarasıyla standart hata çıktısına yazıp programı derhal sonlandırır (abort)."},
            {"name": "#define NDEBUG", "desc": "<assert.h> başlığından önce tanımlanırsa kaynak koddaki tüm assert kontrollerini derleme aşamasında devre dışı bırakır."}
        ]
    },
    {
        "library": "<errno.h>",
        "desc": "Sistem ve Kütüphane Çağrıları Hata Kodları",
        "functions": [
            {"name": "errno", "desc": "Sistem veya standart kütüphane fonksiyonlarında oluşan son hata kodunu saklayan global tamsayı değişken."},
            {"name": "perror(\"msg\")", "desc": "Özel mesajınızın yanına mevcut errno değerine ait sistem hata açıklamasını ekleyerek stderr'e basar."},
            {"name": "strerror(errno)", "desc": "<string.h> ile kullanılır; errno kodunun metin karşılığını (hata mesajı dizgisini) döndürür."},
            {"name": "EDOM", "desc": "Matematiksel tanım kümesi hatası (Domain Error, örn: negatif sayının karekökü sqrt(-1))."},
            {"name": "ERANGE", "desc": "Aralık dışı taşma hatası (Range Error, hesaplama sonucunun tür sınırlarını aşması)."}
        ]
    },
    {
        "library": "<stddef.h>",
        "desc": "Standart Tür ve Sabit Tanımlamaları",
        "functions": [
            {"name": "NULL", "desc": "Hiçbir adresi göstermeyen boş işaretçi sabiti ((void*)0)."},
            {"name": "size_t", "desc": "sizeof işlecinin döndürdüğü, nesnelerin bayt boyutunu temsil eden işaretsiz tamsayı türü."},
            {"name": "ptrdiff_t", "desc": "Aynı dizi içindeki iki işaretçi arasındaki eleman farkını temsil eden işaretli tamsayı türü."},
            {"name": "offsetof(tur, uye)", "desc": "Bir struct üyesinin yapının başlangıç adresinden itibaren olan bayt ofsetini döndüren makro."},
            {"name": "wchar_t", "desc": "Geniş karakterleri temsil etmek için kullanılan tamsayı türü."}
        ]
    }
]
