Puedes simplemente ejecutar el .exe de la carpeta "dist". 
Te recomiendo que copies su contenido en la carpeta con las variables de entorno. 
Para ello, abre una powershell la carpeta raiz extraida y ejecuta:

$destino = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps"
Copy-Item -Path ".\dist\OrganizaDescargas.exe" -Destination $destino

O preguntale a chatgpt como hacerlo.

Si quieres añadir tus propias extensiones, entonces es mas complicado:

Se debe tener installado pyinstaller. Pregunta a chatgpt como hacerlo si no sabes.
Si actualizas extensiones.json, ejecuta update.ps1 con powershell. 
	Para ello deberás darle permisos por ser un programa desconocido. 
	También puedes abrirlo, copiarlo, y ejecutarlo tu desde la carpeta raiz extraída.
Si desea editar los destinos, abre OrganizaDescargas.py, edite las rutas en las primeras líneas de código, guárdalo y ejecuta update.ps1
El registro de movimientos se guardará en Documentos como movimiento_archivos.log pero también podrás cambiarlo a tu gusto.
Una vez hecho esto, simplemente escribe OrganizaDescargas en powershell, cmd o en la barra de búsqueda (al escribirlo, debería aparecer como un comando ejecutable)
	Si esto no funciona, copia el .exe de la carpeta "dist" tras update.ps1 en la ruta de tus variables del sistema, o ejecuta el .exe directamente.
Puedes borrar la carpeta extraída una vez hayas movido el .exe a donde desees.

Si tienes cualquier duda o problema, @Kero3110 en Discord

------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can simply run the .exe from the "dist" folder. 
I recommend that you copy its contents to the folder with the environment variables. 
To do this, open a powershell in the extracted root folder and execute:

$destination = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps"
Copy-Item -Path ".\dist\OrganizaDescargas.exe" -Destination $destino

Or ask chatgpt how to do it.

If you want to add your own extensions, then it's more complicated:

You must have pyinstaller installed. Ask chatgpt how to do it if you don't know.
If you update extensions.json, run update.ps1 with powershell. 
	To do this you must give it permissions because it is an unknown program. 
	You can also open it, copy it, and run it yourself from the extracted root folder.
If you want to edit the destinations, open OrganizaDescargas.py, edit the routes in the first lines of code, save it and run update.ps1
The movement log will be saved in Documents as movement_files.log but you can also change it to your liking.
Once this is done, simply type OrganizaDescargas in powershell, cmd or in the search bar (when you type it, it should appear as an executable command)
	If this doesn't work, copy the .exe from the "dist" folder after update.ps1 to the path of your system variables, or run the .exe directly.
You can delete the extracted folder once you have moved the .exe to where you want.

If you have any questions or problems, @Kero3110 on Discord



