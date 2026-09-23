# -*- coding: utf-8 -*-
"""
C Dili Egitim Uygulamasi - Entegrasyon Testleri
"""
import sys
import os

def test_lessons():
    from data.lessons_data import LESSONS, get_lesson_by_id, get_lessons_by_day, get_curriculum_stats

    print(f"  Toplam Ders: {len(LESSONS)}")
    assert len(LESSONS) == 150, f"150 ders bekleniyor, {len(LESSONS)} bulundu"

    for day in range(1, 31):
        day_lessons = get_lessons_by_day(LESSONS, day)
        assert len(day_lessons) == 5, f"Gun {day}: 5 ders bekleniyor, {len(day_lessons)} bulundu"

    lesson = get_lesson_by_id(LESSONS, "1.1")
    assert lesson is not None, "Ders 1.1 bulunamadi"
    assert lesson["day"] == 1
    assert lesson["sub_index"] == 1

    stats = get_curriculum_stats(LESSONS)
    assert stats["toplam_ders"] == 150

    for les in LESSONS:
        assert "id" in les and "theory" in les and "starter_code" in les and "title" in les
        assert len(les["theory"]) > 50, f"Ders {les['id']}: Teori cok kisa"
        assert len(les["starter_code"]) > 20, f"Ders {les['id']}: Starter kod cok kisa"
        assert "day_title" in les
        assert "sub_index" in les

    print("  [OK] Ders verileri testi basarili")


def test_quizzes():
    from data.quizzes_data import QUIZZES

    assert len(QUIZZES) == 30, f"30 gun quiz bekleniyor, {len(QUIZZES)} bulundu"

    total_questions = 0
    answer_dist = {0: 0, 1: 0, 2: 0, 3: 0}

    for day in range(1, 31):
        questions = QUIZZES[day]
        assert len(questions) >= 5, f"Gun {day}: En az 5 soru bekleniyor"
        total_questions += len(questions)
        for q in questions:
            assert all(k in q for k in ("question", "options", "answer", "explanation"))
            assert len(q["options"]) == 4
            assert 0 <= q["answer"] <= 3
            answer_dist[q["answer"]] += 1

    print(f"  Toplam Soru: {total_questions}")
    print(f"  Cevap Dagilimi: {answer_dist}")
    non_zero = sum(v for k, v in answer_dist.items() if k != 0)
    assert non_zero > 0, "Tum cevaplar 0 indeksinde!"
    print("  [OK] Quiz verileri testi basarili")


def test_compiler():
    from compiler import CompilerEngine

    compiler = CompilerEngine()
    info = compiler.get_compiler_info()
    print(f"  Derleyici: {info}")

    if not info["available"]:
        print("  [SKIP] GCC/Clang bulunamadi")
        return

    result = compiler.compile_and_run(
        '#include <stdio.h>\nint main(){printf("TEST OK\\n");return 0;}'
    )
    assert result["success"] == True, f"Derleme basarisiz: {result.get('stderr','')}"
    assert "TEST OK" in result["stdout"]
    print("  [OK] Derleyici testi basarili")


def test_storage():
    from storage import StorageManager
    import tempfile, json

    tmp_dir = tempfile.mkdtemp()
    tmp_file = os.path.join(tmp_dir, "test_settings.json")

    sm = StorageManager.__new__(StorageManager)
    sm.filepath = tmp_file
    sm.state = sm.get_default_state()

    sm.mark_lesson_completed("1.1", True)
    sm.mark_lesson_completed("1.2", True)
    assert "1.1" in sm.state["completed_lessons"]
    sm.mark_lesson_completed("1.1", False)
    assert "1.1" not in sm.state["completed_lessons"]

    sm.set_active_lesson("5.3")
    assert sm.state["active_lesson_id"] == "5.3"

    sm.save_code_draft("1.1", '#include <stdio.h>\nint main(){return 0;}')
    assert sm.get_code_draft("1.1") == '#include <stdio.h>\nint main(){return 0;}'

    assert sm.save() == True
    assert os.path.exists(tmp_file)

    os.remove(tmp_file)
    os.rmdir(tmp_dir)
    print("  [OK] Depolama testi basarili")


def test_snippets():
    from data.snippets_data import SNIPPETS
    assert len(SNIPPETS) >= 5
    for s in SNIPPETS:
        assert "id" in s and "title" in s and "code" in s
        assert len(s["code"]) > 50
    print(f"  Toplam Snippet: {len(SNIPPETS)}")
    print("  [OK] Snippet testi basarili")


def test_cheatsheet():
    from data.cheatsheet_data import CHEATSHEET
    assert len(CHEATSHEET) >= 5
    for lib in CHEATSHEET:
        assert "library" in lib and "desc" in lib and "functions" in lib
        assert len(lib["functions"]) >= 2
    print(f"  Toplam Kutuphane: {len(CHEATSHEET)}")
    print("  [OK] Cheatsheet testi basarili")


def test_all():
    print("\n" + "=" * 55)
    print("  C EGITIM UYGULAMASI - ENTEGRASYON TESTLERI")
    print("=" * 55 + "\n")

    tests = [
        ("Ders Verileri", test_lessons),
        ("Quiz Verileri", test_quizzes),
        ("Derleyici Motoru", test_compiler),
        ("Depolama Yoneticisi", test_storage),
        ("Snippet Verileri", test_snippets),
        ("Cheatsheet Verileri", test_cheatsheet),
    ]

    passed = failed = 0
    for name, func in tests:
        print(f"[TEST] {name}:")
        try:
            func()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {e}")
            failed += 1
        print()

    print("=" * 55)
    print(f"  Sonuc: {passed} basarili, {failed} basarisiz")
    print("=" * 55 + "\n")
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    test_all()
