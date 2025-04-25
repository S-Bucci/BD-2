## **Trabajo Práctico 2**

### Punto 1

Se recomienda `RESTRICT` si se desea conservar el historial de cursos y evitar pérdidas accidentales de información.

### Punto 2

![Imagen Punto 2](/TP1/imagenes/Punto2.png)

### Punto 3

**CREATE TABLE** cuentas (
    id *INT* **AUTO_INCREMENT** **PRIMARY** KEY,
    saldo *DECIMAL(10,2)* **NOT NULL**
);

**INSERT INTO** cuentas (saldo) **VALUES** (300.00);

**SET TRANSACTION ISOLATION LEVEL READ COMMITTED**;

**START TRANSACTION**;

`-- Leer el saldo actual de la cuenta con id=1`<br>
**SELECT** saldo **FROM** cuentas **WHERE** id = 1;

`-- Actualizar el saldo (sumar 100)`<br>
**UPDATE** cuentas
**SET** saldo = saldo + 100
**WHERE** id = 1;

`-- Simular alguna pausa (para observar efectos de concurrencia)`<br>
`-- Por ejemplo, no hacer COMMIT aún o esperar un tiempo.`<br>

`-- Finalmente, hacer COMMIT`<br>
**COMMIT**;

**START TRANSACTION**;

`-- Leer el saldo actual de la cuenta con id=1`<br>
**SELECT** saldo **FROM** cuentas **WHERE** id = 1;

`-- Actualizar el saldo (sumar 50)`<br>
**UPDATE** cuentas
**SET** saldo = saldo + 50
**WHERE** id = 1;

`-- COMMIT para confirmar los cambios`<br>
**COMMIT**;

**`Al ejecutar este código por partes (y repetir algunas veces a partir de el primer START TRANSACTION) pudimos encontrar un error de concurrencia, ya que solo se agregaron a la base de datos los $100 de la primera transacción. Esto es con el nivel de aislamiento de READ COMMITTED.`**<br>
**`Después hicimos lo mismo pero con un nivel de aislamiento SERIALIZABLE y no tuvimos errores de concurrencia.`**

### Punto 4

**Consulta ejecutada `SIN` indice, sobre la tabla producto**<br>
![Imagen Punto 4.1](/TP1/imagenes/Punto4-1.png)

**Consulta ejecutada `CON` indice, sobre la tabla producto**<br>
![Imagen Punto 4.2](/TP1/imagenes/Punto4-2.png)

**En esta captura se puede apreciar que después de crear el índice la velocidad de lectura aumentó considerablemente, pasando de 46 milésimas a 31.**<br>
![Imagen Punto 4.3](/TP1/imagenes/Punto4-3.png)

### Punto 5

**SELECT * FROM productos WHERE marca_id = 10 AND stock * precio > 40000;**<br>
Devolvió 7929 columnas y tardo 16 milésimas<br>
<br>
**CREATE INDEX idx_precio_stock ON productos(precio, stock);**<br>
Devolvió 7929 columnas y tardo 15 milésimas<br>
<br>
**CREATE INDEX idx_marca_id ON productos(marca_id);**<br>
Devolvió 7929 columnas y tardo 16 milésimas<br>

### Punto 6

![Imagen Punto 6](/TP1/imagenes/Punto6.png)

### Punto 7

Da error porque el usuario no tiene permisos para insertar datos.<br>
![Imagen Punto 7](/TP1/imagenes/Punto7.png)

### Punto 8

-- Tabla principal<br>
**CREATE TABLE** clientes (<br>
    id **INT AUTO_INCREMENT PRIMARY** KEY,<br>
    nombre **VARCHAR(100)**,<br>
    email **VARCHAR(100)**<br>
);

-- Tabla de auditoría<br>
**CREATE TABLE** auditoria_clientes (<br>
    id **INT AUTO_INCREMENT PRIMARY** KEY,<br>
    accion **VARCHAR(10)**,<br>
    cliente_id **INT**,<br>
    datos_viejos **JSON**,<br>
    datos_nuevos **JSON**,<br>
    fecha **DATETIME DEFAULT CURRENT_TIMESTAMP**<br>
);

**DELIMITER $$**

**CREATE TRIGGER** t_auditoria_clientes<br>
**AFTER UPDATE ON** clientes<br>
**FOR EACH ROW**<br>
**BEGIN**<br>
    **INSERT INTO** auditoria_clientes (<br>
        accion,<br>
        cliente_id,<br>
        datos_viejos,<br>
        datos_nuevos<br>
    ) **VALUES** (<br>
        '**UPDATE**',<br>
        OLD.id,<br>
        **JSON_OBJECT**('nombre', OLD.nombre, 'email', OLD.email),<br>
        **JSON_OBJECT**('nombre', NEW.nombre, 'email', NEW.email)<br>
    );<br>
**END$$**

**DELIMITER** ;


**INSERT INTO** clientes (nombre, email) **VALUES**<br>
('Ana Torres', 'ana.torres@email.com'),<br>
('Luis Ramírez', 'luis.ramirez@email.com'),<br>
('María Gómez', 'maria.gomez@email.com'),<br>
('Carlos Díaz', 'carlos.diaz@email.com'),<br>
('Sofía Herrera', 'sofia.herrera@email.com');

**SELECT * FROM** clientes;

**UPDATE** clientes **SET** nombre = 'Juan P. Gómez' **WHERE** id = 1;<br>
**UPDATE** clientes **SET** nombre = 'Carla Campos', email = 'carla.campos@gmail.com' **WHERE** id = 1;<br>

**SELECT * FROM** auditoria_clientes;

![Imagen Punto 8](/TP1/imagenes/Punto8.png)

### Punto 9

**!/bin/bash**<br>

**Configuraciones**<br>
<br>
USER="simon"<br>
PASSWORD="simon"<br>
DATABASE="test"<br>
BACKUP_DIR="/home/simon/backups/mysql"<br>
DATE=$(date +%F_%H-%M-%S)<br>
FILENAME="$DATABASE-$DATE.sql"<br>

**-- Crear directorio si no existe**<br>
mkdir -p "$BACKUP_DIR"<br>

**-- Comando de mysql**<br>
mysqldump -u $USER -p$PASSWORD $DATABASE > "$BACKUP_DIR/$FILENAME"<br>

**-- Configuración del cron**<br>

crontab -e<br>
10 03 * * * /home/simon/backup.sh<br>

**-- Ese es el crontab usado (la hora era en realidad 00:10 pero linux está en UTC)**<br>

![Imagen Punto 9.1](/TP1/imagenes/Punto9-1.png)<br>
**Prueba de que se ejecutó el script y que hizo el backup**<br>

![Imagen Punto 9.2](/TP1/imagenes/Punto9-2.png)<br>
**Base de datos completa**<br>

![Imagen Punto 9.3](/TP1/imagenes/Punto9-3.png)<br>
**Base de datos luego de eliminar la tabla clientes**<br>

![Imagen Punto 9.4](/TP1/imagenes/Punto9-4.png)<br>
**Recuperacion de la base de datos "test"**

![Imagen Punto 9.5](/TP1/imagenes/Punto9-5.png)<br>
**Prueba de que se recuperaron los datos**