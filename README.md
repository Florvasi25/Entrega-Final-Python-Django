# proyecto_final_python

Este proyecto cuenta con 2 vistas principales:
- Inicio
- Usuarios

El inicio es donde se abre el proyecto (landing page). Este cuenta con 2 botones en el nav, Inicio y Usuarios.
El nav y el footer se encuentran en un HTML base y solo vamos cambiando lo que necesitemos de este en las diferentes vistas para no repetir código.

El botón de Inicio nos devulve a la página principal y el botón de Usuarios nos lleva a una nueva vista que cuenta con dos opciones:
- Crear Usuario
- Listar Usuarios

Crear Usuario nos muestra un formulario con 4 campos:
- Nombre, Edad, Email y Teléfono.
Completando estos 4 campos y luego presionando en enviar, el usuario queda guardado en la base de datos.

Estos usuarios guardados se pueden visualizar en la vista "Listar Usuarios"
Esta vista podemos ver la lista de todos los usuarios creados. También cuenta con un campo de texto en el que podemos filtrar por Nombre los usuarios que querramos encontrar en esa lista.



