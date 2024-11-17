pyinstaller --onefile --icon=icon.ico --add-data "extensiones.json;." OrganizaDescargas.py
$destino = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps"
Copy-Item -Path ".\dist\OrganizaDescargas.exe" -Destination $destino
