# -*- coding: utf-8 -*-
"""
30 Günlük C Dili Eğitim & Derleme Masaüstü Uygulaması
Ana Uygulama Giriş Noktası (PyWebView App Entry)
"""

import os
import sys
import webview

from data.lessons_data import LESSONS
from data.quizzes_data import QUIZZES
from data.cheatsheet_data import CHEATSHEET
from data.snippets_data import SNIPPETS
from compiler import CompilerEngine
from storage import StorageManager

def get_asset_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class AppAPI:
    def __init__(self):
        self.compiler = CompilerEngine()
        self.storage = StorageManager()

    def get_curriculum(self):
        return LESSONS

    def get_quizzes(self):
        return QUIZZES

    def get_cheatsheet(self):
        return CHEATSHEET

    def get_snippets(self):
        return SNIPPETS

    def get_compiler_info(self):
        return self.compiler.get_compiler_info()

    def compile_and_run(self, code_content, stdin_input=""):
        return self.compiler.compile_and_run(code_content, stdin_input)

    def get_progress(self):
        return self.storage.get_state()

    def mark_completed(self, lesson_id, is_completed):
        return self.storage.mark_lesson_completed(lesson_id, is_completed)

    def set_active_lesson(self, lesson_id):
        self.storage.set_active_lesson(lesson_id)

    def save_draft(self, lesson_id, code_content):
        self.storage.save_code_draft(lesson_id, code_content)

    def get_draft(self, lesson_id):
        return self.storage.get_code_draft(lesson_id)

    def save_theme(self, theme_name):
        self.storage.state["theme"] = theme_name
        self.storage.save()

    def export_notes(self):
        full_md = "# 30 GÜNLÜK (150 DERSLİK) C DİLİ EĞİTİM NOTLARI\n\n"
        full_md += "> Bu belge C Dili Eğitim Portalı tarafından üretilmiştir.\n\n"
        
        for les in LESSONS:
            full_md += f"---\n\n## {les['title']} ({les['day_title']})\n\n"
            full_md += les['theory'] + "\n\n"
            full_md += "### Örnek Kod:\n```c\n" + les['starter_code'] + "\n```\n\n"
            
        return full_md

def main():
    api = AppAPI()
    html_path = get_asset_path("web/index.html")

    window = webview.create_window(
        title="C Dili 30 Günlük (150 Derslik) İleri Eğitim & Derleme Portalı",
        url=f"file:///{html_path.replace('\\', '/')}",
        js_api=api,
        width=1340,
        height=880,
        min_size=(980, 680),
        resizable=True
    )

    webview.start(debug=False)

if __name__ == "__main__":
    main()
