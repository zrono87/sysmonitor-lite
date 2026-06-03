import os
import shutil
import datetime

# Configuración de umbrales (en porcentaje)
UMBRAL_ALERTA = 80.0
RUTA_LOGS = "historial_alertas.log"

def comprobar_espacio_disco():
    """Calcula el uso del disco principal y genera una alerta si supera el umbral."""
    # Obtenemos estadísticas del disco donde se ejecuta el script (raíz o C:)
    total, usado, libre = shutil.disk_usage("/")
    
    # Calculamos el porcentaje de uso
    porcentaje_usado = (usado / total) * 100
    
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"[{fecha_actual}] Comprobando estado del sistema...")
    print(f"Uso de disco actual: {porcentaje_usado:.2f}%")

    # Si supera el umbral, disparamos la alerta
    if porcentaje_usado >= UMBRAL_ALERTA:
        mensaje_alerta = f"¡ALERTA CRÍTICA! - {fecha_actual} - El uso de disco ha superado el {UMBRAL_ALERTA}% (Actual: {porcentaje_usado:.2f}%)\n"
        print(mensaje_alerta)
        registrar_en_log(mensaje_alerta)
    else:
        print("El estado del almacenamiento es óptimo.")

def registrar_en_log(mensaje):
    """Guarda la alerta en un archivo log persistente para el administrador."""
    try:
        with open(RUTA_LOGS, "a", encoding="utf-8") as f:
            f.write(mensaje)
        print(f"Alerta registrada correctamente en: {os.path.abspath(RUTA_LOGS)}")
    except Exception as e:
        print(f"Error al escribir en el archivo de log: {e}")

if __name__ == "__main__":
    comprobar_espacio_disco()
