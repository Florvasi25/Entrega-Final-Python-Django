# TERCERA PRE-ENTREGA

Este proyecto cuenta con 3 vistas principales:
- Inicio
- Usuarios
- Productos

## INICIO
Cuando ingresamos al server lo primero que vemos es el Inicio (landing page).

El nav y el footer se encuentran en un HTML base y solo vamos cambiando lo que necesitemos de este en las diferentes vistas para no repetir código. El nav contiene 3 botones: Inicio, Usuarios y Productos.

El botón de Inicio nos devulve a la página principal.
El botón de Usuarios nos lleva a una nueva vista que cuenta con dos opciones:
- Crear Usuario
- Listar Usuarios
El botón de Productos nos lleva a otra vista en donde podemos visualizar una lista de productos disponibles.

## USUARIOS
En el apartado de Usuarios contamos con 2 botones: 
- Crear Usuario
- Buscar Usuarios

Crear Usuario nos muestra un formulario con 4 campos:
- Nombre, Edad, Email y Teléfono.
Completando estos 4 campos y luego presionando en enviar, el usuario queda guardado en la base de datos.

Estos usuarios guardados se pueden buscar en la vista "Buscar Usuarios"
Esta vista podemos un campo de texto en el que podemos buscar los usuarios existentes en la base de dato por Nombre.

## PRODUCTOS
En el apartado de productos encontramos una lista de productos de tecnología.
Esta lista está visible al 100% para todos los usuarios y de la única manera en la que se puede interactuar por ahora es realizando una búsqueda sobre esa lista mediante el nombre del producto.

---
### COMENTARIOS
Las 2 vistas se pensaron de manera diferente:
- Usuario: interacción del usuario. Creación y búsqueda pueden realizarse mediante el server.
- Productos: interacción del usuario limitada. Las búsquedan pueden realizarse a través del server pero la creación y modificación de los datos solo se pueden hacer a través del superuser (user: admin - password: 11111).


