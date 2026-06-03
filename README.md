# SysMonitor-Lite 📊

Un script ligero de automatización en Python diseñado para la monitorización proactiva del almacenamiento en sistemas servidores (Linux/Windows). El script evalúa el uso de los recursos del sistema y genera logs de auditoría automatizados en caso de detectar anomalías o falta de espacio.

## 🚀 Características
* **Monitorización en tiempo real:** Cálculo automatizado del porcentaje de uso del disco principal.
* **Alertas configurables:** Sistema de umbrales (Thresholds) modificables según los requisitos del servidor.
* **Auditoría y Logs:** Registro persistente de alertas en un archivo `.log` local con marcas de tiempo detalladas para su posterior análisis forense o de mantenimiento.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Librerías nativas:** `shutil` (gestión de almacenamiento), `os` (rutas de sistema), `datetime` (control temporal).

## 💻 Instalación y Uso

1. Clona este repositorio en tu máquina local o servidor:
```bash
   git clone [https://github.com/tu-usuario/sysmonitor-lite.git](https://github.com/tu-usuario/sysmonitor-lite.git)
