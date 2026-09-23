def generate_quizzes():
    _raw = {
    1: [
        {
            "question": "C dilinde bir programın çalışmaya başladığı ana fonksiyon hangisidir?",
            "options": [
                "main()",
                "begin()",
                "start()",
                "init()"
            ],
            "answer": 0,
            "explanation": "C programları her zaman main() fonksiyonundan çalışmaya başlar."
        },
        {
            "question": "Aşağıdakilerden hangisi C dilinde tek satırlık yorum satırı oluşturur?",
            "options": [
                "-- yorum",
                "# yorum",
                "/* yorum */",
                "// yorum"
            ],
            "answer": 3,
            "explanation": "// işareti tek satırlık yorumlar için kullanılır."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 3)",
            "options": [
                "C, derlemeli (compiled) bir dildir.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, yorumlamalı (interpreted) bir dildir.",
                "C sadece nesne yönelimli programlama için kullanılır."
            ],
            "answer": 0,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 4)",
            "options": [
                "C, yorumlamalı (interpreted) bir dildir.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, derlemeli (compiled) bir dildir.",
                "C sadece nesne yönelimli programlama için kullanılır."
            ],
            "answer": 2,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 5)",
            "options": [
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C, derlemeli (compiled) bir dildir.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, yorumlamalı (interpreted) bir dildir."
            ],
            "answer": 1,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 6)",
            "options": [
                "C, yorumlamalı (interpreted) bir dildir.",
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, derlemeli (compiled) bir dildir."
            ],
            "answer": 3,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 7)",
            "options": [
                "C, derlemeli (compiled) bir dildir.",
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, yorumlamalı (interpreted) bir dildir."
            ],
            "answer": 0,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 8)",
            "options": [
                "C programları doğrudan tarayıcıda çalışır.",
                "C, derlemeli (compiled) bir dildir.",
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C, yorumlamalı (interpreted) bir dildir."
            ],
            "answer": 1,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 9)",
            "options": [
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C, yorumlamalı (interpreted) bir dildir.",
                "C, derlemeli (compiled) bir dildir."
            ],
            "answer": 3,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        },
        {
            "question": "C programlama dilinde C Temelleri konusuyla ilgili hangisi doğrudur? (Soru 10)",
            "options": [
                "C, yorumlamalı (interpreted) bir dildir.",
                "C programları doğrudan tarayıcıda çalışır.",
                "C sadece nesne yönelimli programlama için kullanılır.",
                "C, derlemeli (compiled) bir dildir."
            ],
            "answer": 3,
            "explanation": "C kaynak kodları derleyici aracılığıyla makine koduna dönüştürülür."
        }
    ],
    2: [
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Veri Tipleri için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Veri Tipleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Veri Tipleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 2 - Veri Tipleri hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Veri Tipleri için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Veri Tipleri konusunda bu temel kurallardan biridir."
        }
    ],
    3: [
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Format Belirteçleri için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Format Belirteçleri için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Format Belirteçleri için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Format Belirteçleri için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 3 - Format Belirteçleri hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Format Belirteçleri için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Format Belirteçleri konusunda bu temel kurallardan biridir."
        }
    ],
    4: [
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 4 - scanf, getchar, fgets, buffer hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "scanf, getchar, fgets, buffer için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "scanf, getchar, fgets, buffer konusunda bu temel kurallardan biridir."
        }
    ],
    5: [
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 1;\\nprintf(\"%d\", x++);",
            "options": [
                "0",
                "1",
                "2",
                "Derleme hatası"
            ],
            "answer": 1,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 2;\\nprintf(\"%d\", x++);",
            "options": [
                "Derleme hatası",
                "3",
                "2",
                "1"
            ],
            "answer": 2,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 3;\\nprintf(\"%d\", x++);",
            "options": [
                "2",
                "Derleme hatası",
                "4",
                "3"
            ],
            "answer": 3,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 4;\\nprintf(\"%d\", x++);",
            "options": [
                "4",
                "3",
                "5",
                "Derleme hatası"
            ],
            "answer": 0,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 5;\\nprintf(\"%d\", x++);",
            "options": [
                "4",
                "5",
                "Derleme hatası",
                "6"
            ],
            "answer": 1,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 6;\\nprintf(\"%d\", x++);",
            "options": [
                "Derleme hatası",
                "5",
                "7",
                "6"
            ],
            "answer": 3,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 7;\\nprintf(\"%d\", x++);",
            "options": [
                "8",
                "Derleme hatası",
                "7",
                "6"
            ],
            "answer": 2,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 8;\\nprintf(\"%d\", x++);",
            "options": [
                "Derleme hatası",
                "9",
                "7",
                "8"
            ],
            "answer": 3,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 9;\\nprintf(\"%d\", x++);",
            "options": [
                "9",
                "8",
                "10",
                "Derleme hatası"
            ],
            "answer": 0,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        },
        {
            "question": "Aşağıdaki kodun çıktısı nedir?\\n\\nint x = 10;\\nprintf(\"%d\", x++);",
            "options": [
                "10",
                "11",
                "9",
                "Derleme hatası"
            ],
            "answer": 0,
            "explanation": "x++ post-increment operatörüdür. Önce değişkenin mevcut değeri (x) kullanılır, işlem bittikten sonra değeri 1 artırılır."
        }
    ],
    6: [
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 6 - if, else, else if, &&, ||, ! hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "if, else, else if, &&, ||, ! için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "if, else, else if, &&, ||, ! konusunda bu temel kurallardan biridir."
        }
    ],
    7: [
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "switch-case, break, default, ternary için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "switch-case, break, default, ternary için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 7 - switch-case, break, default, ternary hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "switch-case, break, default, ternary için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "switch-case, break, default, ternary konusunda bu temel kurallardan biridir."
        }
    ],
    8: [
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 8 - for döngüsü, iç içe for, break, continue hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "for döngüsü, iç içe for, break, continue için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "for döngüsü, iç içe for, break, continue konusunda bu temel kurallardan biridir."
        }
    ],
    9: [
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 9 - while, do-while, sonsuz döngü hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "while, do-while, sonsuz döngü için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "while, do-while, sonsuz döngü konusunda bu temel kurallardan biridir."
        }
    ],
    10: [
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 10 - Fonksiyonlar, return, parametre, prototip hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Fonksiyonlar, return, parametre, prototip için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Fonksiyonlar, return, parametre, prototip konusunda bu temel kurallardan biridir."
        }
    ],
    11: [
        {
            "question": "Day 11 - Scope hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Scope için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Scope için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Scope için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Scope için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 11 - Scope hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Scope için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Scope konusunda bu temel kurallardan biridir."
        }
    ],
    12: [
        {
            "question": "Day 12 - Diziler hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Diziler için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Diziler için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Diziler için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Diziler için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Diziler için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Diziler için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Diziler için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Diziler için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Diziler için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 12 - Diziler hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Diziler için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Diziler konusunda bu temel kurallardan biridir."
        }
    ],
    13: [
        {
            "question": "Day 13 - Strings hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Strings için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Strings için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Strings için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Strings için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Strings için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Strings için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Strings için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Strings için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Strings için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 13 - Strings hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Strings için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Strings konusunda bu temel kurallardan biridir."
        }
    ],
    14: [
        {
            "question": "Day 14 - Pointers temel hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Pointers temel için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Pointers temel için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Pointers temel için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Pointers temel için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Pointers temel için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Pointers temel için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Pointers temel için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Pointers temel için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Pointers temel için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 14 - Pointers temel hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Pointers temel için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Pointers temel konusunda bu temel kurallardan biridir."
        }
    ],
    15: [
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 15 - Pointer aritmetiği, array-pointer ilişkisi hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Pointer aritmetiği, array-pointer ilişkisi için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Pointer aritmetiği, array-pointer ilişkisi konusunda bu temel kurallardan biridir."
        }
    ],
    16: [
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "2D diziler, matris için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "2D diziler, matris için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "2D diziler, matris için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 16 - 2D diziler, matris hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "2D diziler, matris için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "2D diziler, matris konusunda bu temel kurallardan biridir."
        }
    ],
    17: [
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Structs, unions, typedef için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Structs, unions, typedef için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Structs, unions, typedef için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Structs, unions, typedef için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 17 - Structs, unions, typedef hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Structs, unions, typedef için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Structs, unions, typedef konusunda bu temel kurallardan biridir."
        }
    ],
    18: [
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 18 - malloc, calloc, realloc, free, memory leaks hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "malloc, calloc, realloc, free, memory leaks için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "malloc, calloc, realloc, free, memory leaks konusunda bu temel kurallardan biridir."
        }
    ],
    19: [
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 19 - fopen, fclose, fprintf, fscanf, fgets hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fopen, fclose, fprintf, fscanf, fgets için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "fopen, fclose, fprintf, fscanf, fgets konusunda bu temel kurallardan biridir."
        }
    ],
    20: [
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 20 - fread, fwrite, fseek, ftell, binary files hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "fread, fwrite, fseek, ftell, binary files için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "fread, fwrite, fseek, ftell, binary files konusunda bu temel kurallardan biridir."
        }
    ],
    21: [
        {
            "question": "Day 21 - Bitwise operators hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Bitwise operators için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Bitwise operators için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bitwise operators için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bitwise operators için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Bitwise operators için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bitwise operators için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bitwise operators için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Bitwise operators için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bitwise operators için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 21 - Bitwise operators hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bitwise operators için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Bitwise operators konusunda bu temel kurallardan biridir."
        }
    ],
    22: [
        {
            "question": "Day 22 - enum, bit fields hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "enum, bit fields için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "enum, bit fields için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "enum, bit fields için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "enum, bit fields için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "enum, bit fields için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "enum, bit fields için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "enum, bit fields için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "enum, bit fields için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "enum, bit fields için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 22 - enum, bit fields hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "enum, bit fields için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "enum, bit fields konusunda bu temel kurallardan biridir."
        }
    ],
    23: [
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Function pointers, callbacks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Function pointers, callbacks için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 23 - Function pointers, callbacks hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Function pointers, callbacks için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Function pointers, callbacks konusunda bu temel kurallardan biridir."
        }
    ],
    24: [
        {
            "question": "Day 24 - Linked list operations hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Linked list operations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Linked list operations için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Linked list operations için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Linked list operations için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Linked list operations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Linked list operations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Linked list operations için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Linked list operations için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Linked list operations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 24 - Linked list operations hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Linked list operations için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Linked list operations konusunda bu temel kurallardan biridir."
        }
    ],
    25: [
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Stack, Queue implementations için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Stack, Queue implementations için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 25 - Stack, Queue implementations hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Stack, Queue implementations için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Stack, Queue implementations konusunda bu temel kurallardan biridir."
        }
    ],
    26: [
        {
            "question": "Day 26 - Advanced recursion hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Advanced recursion için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Advanced recursion için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Advanced recursion için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Advanced recursion için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Advanced recursion için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Advanced recursion için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Advanced recursion için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Advanced recursion için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Advanced recursion için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 26 - Advanced recursion hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Advanced recursion için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Advanced recursion konusunda bu temel kurallardan biridir."
        }
    ],
    27: [
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Sorting algorithms için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Sorting algorithms için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Sorting algorithms için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Sorting algorithms için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 27 - Sorting algorithms hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Sorting algorithms için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 1,
            "explanation": "Sorting algorithms konusunda bu temel kurallardan biridir."
        }
    ],
    28: [
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Searching algorithms, Big O için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 2,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur."
            ],
            "answer": 0,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Searching algorithms, Big O için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 28 - Searching algorithms, Big O hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Searching algorithms, Big O için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Searching algorithms, Big O konusunda bu temel kurallardan biridir."
        }
    ],
    29: [
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 29 - Header files, multi-file projects, #ifndef guards hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Header files, multi-file projects, #ifndef guards için kural 1 doğrudur.",
                "Tanımsız davranıştır."
            ],
            "answer": 2,
            "explanation": "Header files, multi-file projects, #ifndef guards konusunda bu temel kurallardan biridir."
        }
    ],
    30: [
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 1: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 2: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 3: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 4: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Preprocessor directives, advanced topics için kural 1 doğrudur."
            ],
            "answer": 3,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 5: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 1,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 6: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 7: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Çalışma zamanı hatası oluşur.",
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 1,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 8: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Bu işlem derleme hatası verir.",
                "Tanımsız davranıştır."
            ],
            "answer": 0,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 9: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Tanımsız davranıştır.",
                "Çalışma zamanı hatası oluşur.",
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 2,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        },
        {
            "question": "Day 30 - Preprocessor directives, advanced topics hakkında soru 10: Aşağıdaki ifadelerden hangisi doğrudur?",
            "options": [
                "Preprocessor directives, advanced topics için kural 1 doğrudur.",
                "Çalışma zamanı hatası oluşur.",
                "Tanımsız davranıştır.",
                "Bu işlem derleme hatası verir."
            ],
            "answer": 0,
            "explanation": "Preprocessor directives, advanced topics konusunda bu temel kurallardan biridir."
        }
    ]
}
    return _raw

QUIZZES = generate_quizzes()