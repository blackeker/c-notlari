# -*- coding: utf-8 -*-
"""
Kullanıcı İlerlemesi ve Ayar Depolama Modülü (Storage Manager)
Kullanıcının tamamladığı dersleri, en son aktif dersini ve
editördeki kod taslaklarını settings.json dosyasında depolar.
"""

import os
import json

class StorageManager:
    def __init__(self, filename="settings.json"):
        appdata_dir = os.path.join(os.path.expanduser("~"), ".c_egitim_app")
        os.makedirs(appdata_dir, exist_ok=True)
        self.filepath = os.path.join(appdata_dir, filename)
        self.state = self.load()

    def get_default_state(self):
        return {
            "completed_lessons": [],
            "active_lesson_id": "1.1",
            "code_drafts": {},
            "theme": "dark"
        }

    def load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    default = self.get_default_state()
                    default.update(data)
                    return default
            except json.JSONDecodeError:
                import sys
                print(f"UYARI: Ayar dosyası bozuk, varsayılan ayarlar yükleniyor: {self.filepath}", file=sys.stderr)
                return self.get_default_state()
            except Exception as e:
                import sys
                print(f"UYARI: Ayar dosyası okunamadı ({e}), varsayılan ayarlar yükleniyor.", file=sys.stderr)
                return self.get_default_state()
        return self.get_default_state()

    def save(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self.state, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    def mark_lesson_completed(self, lesson_id, is_completed=True):
        completed = set(self.state.get("completed_lessons", []))
        if is_completed:
            completed.add(lesson_id)
        else:
            completed.discard(lesson_id)
        self.state["completed_lessons"] = list(completed)
        self.save()
        return self.state["completed_lessons"]

    def set_active_lesson(self, lesson_id):
        self.state["active_lesson_id"] = lesson_id
        self.save()

    def save_code_draft(self, lesson_id, code_content):
        if "code_drafts" not in self.state:
            self.state["code_drafts"] = {}
        self.state["code_drafts"][lesson_id] = code_content
        self.save()

    def get_code_draft(self, lesson_id):
        return self.state.get("code_drafts", {}).get(lesson_id, None)

    def get_state(self):
        return self.state
