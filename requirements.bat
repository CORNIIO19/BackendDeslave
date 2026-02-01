@echo off
REM =========================
REM Setup del backend en Windows
REM =========================

echo =====================================================
echo Creando entorno virtual para el backend
echo =====================================================

REM 1️⃣ Crear entorno virtual
python -m venv venv

IF ERRORLEVEL 1 (
    echo Error creando el entorno virtual. Verifica que Python esté instalado.
    exit /b 1
)

echo =====================================================
echo Activando entorno virtual
echo =====================================================

REM 2️⃣ Activar entorno virtual
call venv\Scripts\activate.bat

REM 3️⃣ Actualizar pip
python -m pip install --upgrade pip

REM 4️⃣ Instalar dependencias
echo =====================================================
echo Instalando dependencias del backend
echo =====================================================

pip install fastapi uvicorn[standard] httpx rasterio numpy pydantic

REM ✅ Opcional: si tienes más librerías, agregarlas arriba

echo =====================================================
echo Instalación completada
echo =====================================================

echo Para ejecutar el backend:
echo call venv\Scripts\activate.bat
echo uvicorn app.main:app --reload
pause
