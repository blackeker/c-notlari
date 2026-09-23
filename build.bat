@echo off
chcp 65001 > nul
echo ============================================================
echo   30 Gunluk (150 Derslik) C Dili Egitim Uygulamasi - Build Scripti
echo ============================================================
echo.

python build_exe.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Tek dosya C_Egitim_Uygulamasi.exe basariyla dist/ klasorune olusturuldu.
) else (
    echo.
    echo Bir hata olustu!
)

pause
