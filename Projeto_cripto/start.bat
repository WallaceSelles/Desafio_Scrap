@echo off
echo =====================================
echo     Iniciando Coleta de Criptomoedas
echo =====================================

echo.
echo [1/2] Executando Web Scraping...
python -m scraping.main

echo.
echo [2/2] Executando Coleta via API...
python -m api.main

echo.
echo =====================================
echo     Finalizado! Verifique a pasta /output
echo =====================================
pause
