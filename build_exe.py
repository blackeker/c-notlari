# -*- coding: utf-8 -*-
"""
Single-file Standalone Executable (.exe) Derleme Betiği
PyInstaller kullanarak projeyi Windows üzerinde bağımsız tek bir .exe haline getirir.
"""

import os
import sys
import subprocess
import shutil

def build_executable():
    print("=" * 60)
    print("  C DİLİ EĞİTİM UYGULAMASI - TEK DOSYA (.EXE) PAKETLEME")
    print("=" * 60)

    project_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(project_dir, "dist")
    build_dir = os.path.join(project_dir, "build")

    # Temizlik
    for folder in [dist_dir, build_dir]:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
            except Exception as e:
                print(f"Uyarı: {folder} temizlenemedi: {e}")

    # PyInstaller Parametreleri
    # --onefile: Taşınabilir tek .exe
    # --windowed: Konsol penceresiz masaüstü UI
    # --add-data: Web arayüzü ve müfredat verilerini gömme
    cmd = [
        sys.executable,
        "-m", "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name=C_Egitim_Uygulamasi",
        f"--add-data={os.path.join(project_dir, 'web')};web",
        f"--add-data={os.path.join(project_dir, 'data')};data",
        os.path.join(project_dir, "app.py")
    ]

    print("PyInstaller çalıştırılıyor...")
    print("Komut:", " ".join(cmd))
    print("-" * 60)

    result = subprocess.run(cmd)

    if result.returncode == 0:
        exe_path = os.path.join(dist_dir, "C_Egitim_Uygulamasi.exe")
        print("\n" + "=" * 60)
        print("  PAKETLEME BAŞARIYLA TAMAMLANDI!")
        print(f"  Oluşturulan EXE Konumu: {exe_path}")
        print("=" * 60)
    else:
        print("\nHATA: Paketleme işlemi başarısız oldu!")
        sys.exit(1)

if __name__ == "__main__":
    build_executable()
