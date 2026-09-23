# -*- coding: utf-8 -*-
"""
C Derleyici ve Çalıştırıcı Motoru (Compiler & Runner Engine)
Sistemdeki GCC/Clang/MSVC derleyicilerini otomatik tespit eder,
C kodunu derler ve çalıştırır.
"""

import os
import sys
import shutil
import subprocess
import tempfile
import time
import atexit

class CompilerEngine:
    def __init__(self):
        self.compiler_path = self.find_compiler()
        self.temp_dir = os.path.join(tempfile.gettempdir(), "c_education_app")
        os.makedirs(self.temp_dir, exist_ok=True)
        atexit.register(self.cleanup)

    def cleanup(self):
        """Uygulama kapanırken temp dosyalarını temizler."""
        try:
            if os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir, ignore_errors=True)
        except Exception:
            pass

    def find_compiler(self):
        """Sistemdeki GCC veya Clang derleyicisini otomatik tespit eder."""
        candidates = [
            r"C:\msys64\mingw64\bin\gcc.exe",
            r"C:\msys64\ucrt64\bin\gcc.exe",
            r"C:\msys64\mingw32\bin\gcc.exe",
            r"C:\MinGW\bin\gcc.exe",
            shutil.which("gcc"),
            shutil.which("clang"),
            shutil.which("cl"),
        ]

        for cand in candidates:
            if cand and os.path.exists(cand):
                return cand
        return None

    def get_compiler_info(self):
        """Derleyici durum bilgisini döndürür."""
        if self.compiler_path:
            return {
                "available": True,
                "path": self.compiler_path,
                "name": os.path.basename(self.compiler_path).upper()
            }
        else:
            return {
                "available": False,
                "path": "",
                "name": "Derleyici Bulunamadı (GCC / Clang gereklidir)"
            }

    def compile_and_run(self, code_content, stdin_input=""):
        """
        C kodunu derler ve çalıştırır.
        """
        if not self.compiler_path:
            return {
                "success": False,
                "stage": "setup",
                "stdout": "",
                "stderr": (
                    "HATA: Sistemde GCC veya Clang derleyicisi bulunamadı!\n"
                    "Lütfen MinGW-w64 / MSYS2 veya GCC kurup PATH ortam değişkenine ekleyin.\n"
                    "Algılanan konum kontrol edildi: C:\\msys64\\mingw64\\bin\\gcc.exe"
                ),
                "exit_code": -1,
                "elapsed_time": 0.0
            }

        c_file = os.path.join(self.temp_dir, "program.c")
        exe_file = os.path.join(self.temp_dir, "program.exe")

        # Önceki exe kalıntısını sil
        if os.path.exists(exe_file):
            try:
                os.remove(exe_file)
            except Exception:
                pass

        # Kodu temp.c dosyasına yaz
        with open(c_file, "w", encoding="utf-8") as f:
            f.write(code_content)

        # Environment PATH ayarla (Derleyici DLL'lerinin bulunabilmesi için)
        env = os.environ.copy()
        compiler_dir = os.path.dirname(self.compiler_path)
        if compiler_dir not in env.get("PATH", ""):
            env["PATH"] = compiler_dir + os.pathsep + env.get("PATH", "")

        # 1. DERLEME ADIMI
        start_compile = time.time()
        compile_cmd = [self.compiler_path, c_file, "-o", exe_file, "-Wall"]
        
        try:
            compile_proc = subprocess.run(
                compile_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
                timeout=15
            )
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "stage": "compile",
                "stdout": "",
                "stderr": "DERLEME HATASI: Derleme işlemi 15 saniyelik zaman aşımına uğradı.",
                "exit_code": -1,
                "elapsed_time": time.time() - start_compile
            }

        if compile_proc.returncode != 0 or not os.path.exists(exe_file):
            return {
                "success": False,
                "stage": "compile",
                "stdout": compile_proc.stdout,
                "stderr": compile_proc.stderr,
                "exit_code": compile_proc.returncode,
                "elapsed_time": time.time() - start_compile
            }

        compile_warnings = compile_proc.stderr

        # 2. ÇALIŞTIRMA ADIMI
        start_exec = time.time()
        try:
            exec_proc = subprocess.run(
                [exe_file],
                input=stdin_input,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
                timeout=10
            )
            elapsed = round(time.time() - start_exec, 3)

            return {
                "success": exec_proc.returncode == 0,
                "stage": "execution",
                "stdout": exec_proc.stdout,
                "stderr": exec_proc.stderr if exec_proc.stderr else compile_warnings,
                "exit_code": exec_proc.returncode,
                "elapsed_time": elapsed
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "stage": "execution",
                "stdout": "",
                "stderr": "ÇALIŞMA ZAMANI HATASI: Program 10 saniyelik zaman aşımına uğradı! (Sonsuz döngü veya beklemede kalma oluşmuş olabilir)",
                "exit_code": -1,
                "elapsed_time": 10.0
            }
        except Exception as e:
            return {
                "success": False,
                "stage": "execution",
                "stdout": "",
                "stderr": f"Çalıştırma Hatası: {str(e)}",
                "exit_code": -1,
                "elapsed_time": 0.0
            }
