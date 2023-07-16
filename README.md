# PROYECTO FINAL PYTHON-DJANGO

Web diseñada para vender productos usados y/o nuevos.

Este proyecto cuenta con 3 aplicaciones principales:
- Inicio (Productos),
- Mensajería (Mensajes) y
- Usuarios.

## INICIO
Cuando ingresamos al server lo primero que vemos es el Inicio (landing page).

El nav y el footer se encuentran en un HTML base y solo vamos cambiando lo que necesitemos de este en las diferentes vistas para no repetir código. El nav contiene 4 botones para ir a diferentes páginas: Inicio, Productos, Sobre Mí y Mensajería (esta última solo disponible para usuarios registrados) y 2 botones más para el Usuario (login y registrarse que luego de estar loggeado cambia a 1 solo botón --> logout).

- El botón de Inicio nos devulve a la página principal,
- El botón de Productos nos lleva a una página en donde podemos visualizar una lista de productos disponibles,
- El botón de Sobre Mí nos lleva a una página con una breve descripción de mí y
- El botón de Mensajes nos lleva a otra página donde se pueden visualizar los mensajes que ese usuario recibió y/o envió.

## USUARIOS
Los usuarios pueden registrarse o loggearse.

El registro pide ciertos datos básicos para que al crear publicaciones estas generen automáticamente en el cuerpo del producto esos datos para poder ser contactados.

Los Usuarios también pueden modificar su perfil.

## PRODUCTOS
En el apartado de productos encontramos una lista de productos. Acá los usuarios pueden cargar cosas que ya no usen para que otros usuarios puedan contactarse con ellos y comprar esos productos.
- Cuando un usuario no está loggeado solo puede ver la funcionalidad de "ver más". 
- Cuando el usuario está loggeado puede ver otros 2 botones
    - Eliminar y
    - Modificar.

También cuenta con un filtro para buscar productos por nombre.

## MENSAJERÍA
En la página de mensajería se pueden enviar mensajes a otros usuarios solicitándoles más información sobre los productos o para coordinar ventas. Se puede ver:
- Mensajes Enviados y
- Mensajes Recibidos.

---
### COMENTARIOS
Un usuario que no está loggeado puede ingresar solo a ciertas páginas. Si este supiera la dirección html le va a pedir que se loggee para continuar.

---
### VIDEO DEMOSTRATIVO
https://drive.google.com/file/d/14RcCp5HTt9OQp-6bjBUuvlVS1T0xamUT/view?usp=sharing


