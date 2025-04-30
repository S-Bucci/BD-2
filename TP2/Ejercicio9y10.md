## **Trabajo Práctico 2**

### Punto 9

**Replica set:** Nos permite tenes un nodo principal que replica la información de este a nodos secundarios. Nos da alta disponibilidad
ya que si un nodo principal se cae, un nodo secundario toma su papel y pasa a ser principal. Esto nos da tolerancia a fallos y a que la información esté
siempre disponible para su uso. Esta forma de guardado acelera la velocidad de lectura porque los nodos secundarios pueden leer al mismo y el primario escribir.<br>

**Sharding:** El sharding (que consiste en repartir los datos de una database en diferentes máquinas) es útil por varias razones. Una de ellas es que incrementa la velocidad de lectura/escritura ya que se pueden centrar en un shard mientras que las otras pueden hacer otro tipo de operaciones. También permite incrementar la capacidad de almacenamiento ya que las diferentes máquinas en las que están los shard pueden ser escaladas verticalmente (añadiendo espacio o RAM). Otra ventaja es que permite que, en el caso que una de las shard no se pueda utilizar temporalmente, se pueda mantener acceso al resto de la base de datos.<br>

### Punto 10

**Paso 1: Crear un usuario con permisos de lectura/escritura**

Ingresar el siguiente código en la consola de mongo:
```
db.createUser({ <br>
  user: "nuevo_usuario", <br>
  pwd: "contraseña_segura", <br>
  roles: [ { role: "readWrite", db: "miBaseDeDatos" } ] <br>
})
```

En user ingresar el nombre del usuario nuevo. <br>
En pwd ingresar la contraseña del usuario nuevo. <br>
En "miBaseDeDatos" ingresar el nombre de la base de datos de la cual se quiera hacer el backup. <br>

**Paso 2: Como hacer un backup en mongodb**

En la consola de mongo, ingresar el siguiente código:
```
mongodump --db=miBaseDeDatos --out=/ruta/del/backup
```
En "miBaseDeDatos" ingresar el nombre de la base de datos de la cual se quiera hacer el backup. <br>
"ruta/del/backup" hace referencia a la dirección de la carpeta donde estarían usualmente los backups. <br>

**Paso 3: Como restaurar una base de datos desde un backup en mongodb**

En la consola de mongo, ingresar el siguiente código:
```
mongorestore --db=miBaseDeDatos /ruta/del/backup/miBaseDeDatos
```
En "miBaseDeDatos" ingresar el nombre de la base de datos destino. <br>
"ruta/del/backup/miBaseDeDatos" hace referencia a la dirección de la cual se quiere hacer el restore. <br>