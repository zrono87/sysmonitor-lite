# SysMonitor-Lite 📊

Un script ligero de automatización en Python diseñado para la monitorización proactiva del almacenamiento en sistemas servidores (Linux/Windows). El script evalúa el uso de los recursos de almacenamiento local y genera registros de auditoría automatizados en caso de detectar anomalías o falta de espacio.

Ideal para administradores de sistemas que buscan una solución rápida de alertas sin sobrecargar el servidor con agentes pesados.

## 🚀 Características
* **Monitorización en tiempo real:** Cálculo automatizado del porcentaje de uso del disco principal.
* **Alertas configurables:** Sistema de umbrales (Thresholds) modificables mediante variables simples.
* **Auditoría y Logs:** Registro persistente de alertas en un archivo `.log` local con marcas de tiempo (timestamps) detalladas para análisis posterior.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Librerías nativas:** `shutil` (gestión de almacenamiento), `os` (rutas de sistema), `datetime` (control temporal). No requiere dependencias externas de terceros.

## ⚙️ Configuración básica

Puedes modificar los parámetros directamente en las primeras líneas del archivo `sysmonitor.py`:

| Variable | Tipo | Descripción | Valor por defecto |
| :--- | :--- | :--- | :--- |
| `UMBRAL_ALERTA` | Float | Porcentaje de disco usado a partir del cual salta la alarma. | `80.0` |
| `RUTA_LOGS` | String | Nombre o ruta del archivo donde se guardará el histórico. | `"historial_alertas.log"` |

## 💻 Instalación y Uso

1. Clona este repositorio en tu máquina local o en el servidor de pruebas:
```bash
git clone [https://github.com/tu-usuario/sysmonitor-lite.git](https://github.com/tu-usuario/sysmonitor-lite.git)
```

2. Entra en el directorio del proyecto:
```bash
cd sysmonitor-lite
```

3. Ejecuta el script de manera manual para comprobar que funciona:
```bash
python3 sysmonitor.py
```

### 🕒 Automatización en producción (Linux)
Para que el script se ejecute de forma totalmente automática cada hora, puedes añadirlo al **cron** de tu sistema Linux:

1. Abre el editor de cron: `crontab -e`
2. Añade la siguiente línea al final del archivo (ajustando tus rutas reales):
```bash
0 * * * * /usr/bin/python3 /ruta/a/tu/carpeta/sysmonitor-lite/sysmonitor.py
```

## 📝 Ejemplo de Salida en el Log (`historial_alertas.log`)
> ¡ALERTA CRÍTICA! - 2026-06-03 12:40:15 - El uso de disco ha superado el 80.0% (Actual: 84.52%)
> ¡ALERTA CRÍTICA! - 2026-06-03 13:00:02 - El uso de disco ha superado el 80.0% (Actual: 86.10%)

## 📈 Próximas Mejoras (Roadmap)
* Integración con la API de Telegram para enviar notificaciones push inmediatas al móvil del administrador.
* Monitorización en paralelo del uso de la memoria RAM y la carga de CPU.
