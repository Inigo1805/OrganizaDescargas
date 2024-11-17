import os
import shutil
import logging
from pathlib import Path
import json

# Obtener el nombre de usuario actual
user_name = os.getlogin()
log_route = f"C:/Users/{user_name}/Documents/movimientos_archivos.log"
# Rutas de las carpetas
descargas_path = Path(f"C:/Users/{user_name}/Downloads")
imagenes_path = Path(f"C:/Users/{user_name}/Pictures/Descargas Imagenes")
documentos_path = Path(f"C:/Users/{user_name}/Documents/Descargas Documentos")
comprimidos_path = Path(f"C:/Users/{user_name}/Documents/Descargas Comprimidos")
audio_path = Path(f"C:/Users/{user_name}/Music/Descargas Audios")
videos_path = Path(f"C:/Users/{user_name}/Videos/Descargas Videos")
ejecutables_path = Path(f"C:/Users/{user_name}/Documents/Descargas Ejecutables")
scripts_path = Path(f"C:/Users/{user_name}/Documents/Descargas Scripts")
mods_path = Path(f"C:/Users/{user_name}/Documents/Descargas Mods")
objects_path = Path(f"C:/Users/{user_name}/3D Objects/Descargas Objetos 3D")

# Crear las carpetas de destino si no existen
imagenes_path.mkdir(parents=True, exist_ok=True)
documentos_path.mkdir(parents=True, exist_ok=True)
comprimidos_path.mkdir(parents=True, exist_ok=True)
audio_path.mkdir(parents=True, exist_ok=True)
videos_path.mkdir(parents=True, exist_ok=True)
ejecutables_path.mkdir(parents=True, exist_ok=True)
scripts_path.mkdir(parents=True, exist_ok=True)
mods_path.mkdir(parents=True, exist_ok=True)
objects_path.mkdir(parents=True, exist_ok=True)

# Obtener la ruta del directorio donde está el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo JSON
file_path = os.path.join(script_dir, 'extensiones.json')

# Abrir y leer el archivo
with open(file_path, 'r') as f:
    extensiones = json.load(f)

# Acceder a las listas
extensiones_imagenes = extensiones['extensiones_imagenes']
extensiones_documentos = extensiones['extensiones_documentos']
extensiones_comprimidos = extensiones['extensiones_comprimidos']
extensiones_audio = extensiones['extensiones_audio']
extensiones_video = extensiones['extensiones_video']
extensiones_ejecutables = extensiones['extensiones_ejecutables']
extensiones_scripts = extensiones['extensiones_scripts']
extensiones_mods = extensiones['extensiones_mods']
extensiones_modelado_3d = extensiones['extensiones_modelado_3d']

# Configuración del log
logging.basicConfig(
    filename=log_route,  # Archivo donde se guardarán los logs
    level=logging.INFO,                   # Nivel de log (INFO para registrar eventos importantes)
    format="%(asctime)s - %(message)s",    # Formato de mensaje (hora y mensaje)
)

def log_movimiento(src_file: Path, dest_file: Path) -> None:
    """Función para registrar el movimiento de archivos en el log."""
    logging.info(f"Movido: {src_file} -> {dest_file}")

# Función principal
archivos_movidos = False  # Flag para saber si se movieron archivos
def organiza_archivos(extensiones: list[str], destino: Path) -> None:
    global archivos_movidos
    # Recorre solo los archivos en la carpeta de descargas
    for file in os.listdir(descargas_path):
        src_file = Path(descargas_path) / file
        if src_file.is_file() and any(file.lower().endswith(ext) for ext in extensiones):
            dest_file = destino / file  
            # Verifica si el archivo ya existe en el destino
            dest_file_path = Path(dest_file)  # Convertir el nombre del archivo a Path
            if dest_file_path.exists():
                # Si el archivo ya existe, agrega un sufijo para evitar sobrescribirlo
                dest_file_path = destino / (dest_file_path.stem + "_copia" + dest_file_path.suffix)
                print(f"El archivo {file} ya existe en {destino}. Se renombrará a {dest_file_path.name}.")
            
            print(f"Moviendo: {src_file} a {dest_file_path}")
            shutil.move(src_file, dest_file_path)
            log_movimiento(src_file, dest_file_path)  # Registra el movimiento en el log
            archivos_movidos = True


# Organizar imágenes y documentos
organiza_archivos(extensiones_imagenes, imagenes_path)
organiza_archivos(extensiones_documentos, documentos_path)
organiza_archivos(extensiones_comprimidos, comprimidos_path)
organiza_archivos(extensiones_audio, audio_path)
organiza_archivos(extensiones_video, videos_path)
organiza_archivos(extensiones_ejecutables, ejecutables_path)
organiza_archivos(extensiones_scripts, scripts_path)
organiza_archivos(extensiones_mods, mods_path)
organiza_archivos(extensiones_modelado_3d, objects_path)
# Si no se movieron archivos
if not archivos_movidos:
    print("No hay archivos que mover")
input("\nPresiona Enter para finalizar...")