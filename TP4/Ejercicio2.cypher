// ====================================
// EJERCICIO 2: BIBLIOTECA UNIVERSITARIA EXTENDIDA
// ====================================

// 1. MODELADO - Crear nodos y relaciones

// Crear Carreras
CREATE (c1:Carrera {nombre: "Ingeniería en Sistemas", codigo: "IS"})
CREATE (c2:Carrera {nombre: "Administración de Empresas", codigo: "AE"})
CREATE (c3:Carrera {nombre: "Psicología", codigo: "PSI"})

// Crear Estudiantes
CREATE (est1:Estudiante {nombre: "Pedro González", legajo: "12345", email: "pedro.gonzalez@uni.edu"})
CREATE (est2:Estudiante {nombre: "Laura Fernández", legajo: "12346", email: "laura.fernandez@uni.edu"})
CREATE (est3:Estudiante {nombre: "Diego Romero", legajo: "12347", email: "diego.romero@uni.edu"})

// Crear Categorías
CREATE (cat1:Categoria {nombre: "Tecnología", descripcion: "Libros sobre tecnología y programación"})
CREATE (cat2:Categoria {nombre: "Administración", descripcion: "Libros sobre gestión empresarial"})
CREATE (cat3:Categoria {nombre: "Psicología", descripcion: "Libros sobre psicología y comportamiento"})
CREATE (cat4:Categoria {nombre: "Matemáticas", descripcion: "Libros sobre matemáticas y estadística"})

// Crear Libros
CREATE (l1:Libro {titulo: "Algoritmos y Estructuras de Datos", isbn: "978-1234567890", autor: "Robert Sedgewick", anio: 2019})
CREATE (l2:Libro {titulo: "Principios de Administración", isbn: "978-1234567891", autor: "Henry Fayol", anio: 2020})
CREATE (l3:Libro {titulo: "Psicología Cognitiva", isbn: "978-1234567892", autor: "John Anderson", anio: 2021})
CREATE (l4:Libro {titulo: "Estadística Aplicada", isbn: "978-1234567893", autor: "Ronald Walpole", anio: 2018})
// Establecer relaciones: Estudiantes pertenecen a Carreras
MATCH (est1:Estudiante {nombre: "Pedro González"}), (c1:Carrera {nombre: "Ingeniería en Sistemas"})
CREATE (est1)-[:ESTUDIA]->(c1)

MATCH (est2:Estudiante {nombre: "Laura Fernández"}), (c2:Carrera {nombre: "Administración de Empresas"})
CREATE (est2)-[:ESTUDIA]->(c2)

MATCH (est3:Estudiante {nombre: "Diego Romero"}), (c3:Carrera {nombre: "Psicología"})
CREATE (est3)-[:ESTUDIA]->(c3)

// Establecer relaciones: Libros pertenecen a Categorías
MATCH (l1:Libro {titulo: "Algoritmos y Estructuras de Datos"}), (cat1:Categoria {nombre: "Tecnología"})
CREATE (l1)-[:PERTENECE_A]->(cat1)

MATCH (l2:Libro {titulo: "Principios de Administración"}), (cat2:Categoria {nombre: "Administración"})
CREATE (l2)-[:PERTENECE_A]->(cat2)

MATCH (l3:Libro {titulo: "Psicología Cognitiva"}), (cat3:Categoria {nombre: "Psicología"})
CREATE (l3)-[:PERTENECE_A]->(cat3)

MATCH (l4:Libro {titulo: "Estadística Aplicada"}), (cat4:Categoria {nombre: "Matemáticas"})
CREATE (l4)-[:PERTENECE_A]->(cat4)
// Crear Préstamos con fechas y estado
MATCH (est1:Estudiante {nombre: "Pedro González"}), (l1:Libro {titulo: "Algoritmos y Estructuras de Datos"})
CREATE (est1)-[:PRESTA {fechaPrestamo: "2024-07-01", fechaDevolucion: "2024-07-15", estado: "Activo"}]->(l1)

MATCH (est2:Estudiante {nombre: "Laura Fernández"}), (l2:Libro {titulo: "Principios de Administración"})
CREATE (est2)-[:PRESTA {fechaPrestamo: "2024-06-15", fechaDevolucion: "2024-06-29", estado: "Devuelto"}]->(l2)

MATCH (est3:Estudiante {nombre: "Diego Romero"}), (l3:Libro {titulo: "Psicología Cognitiva"})
CREATE (est3)-[:PRESTA {fechaPrestamo: "2024-07-05", fechaDevolucion: "2024-07-19", estado: "Devuelto"}]->(l3)

MATCH (est1:Estudiante {nombre: "Pedro González"}), (l4:Libro {titulo: "Estadística Aplicada"})
CREATE (est1)-[:PRESTA {fechaPrestamo: "2024-06-20", fechaDevolucion: "2024-07-04", estado: "Devuelto"}]->(l4)

MATCH (est2:Estudiante {nombre: "Laura Fernández"}), (l1:Libro {titulo: "Algoritmos y Estructuras de Datos"})
CREATE (est2)-[:PRESTA {fechaPrestamo: "2024-07-08", fechaDevolucion: "2024-07-22", estado: "Activo"}]->(l1)
// 2. CONSULTAS

// Obtener todos los libros actualmente prestados (estado "Activo")
MATCH (e:Estudiante)-[r:PRESTA]->(l:Libro)
WHERE r.estado = "Activo"
RETURN l.titulo AS Libro, 
       l.autor AS Autor, 
       e.nombre AS Estudiante, 
       r.fechaPrestamo AS FechaPrestamo, 
       r.fechaDevolucion AS FechaDevolucion

// Listar cuántos libros ha pedido prestado cada estudiante
MATCH (e:Estudiante)-[:PRESTA]->(l:Libro)
RETURN e.nombre AS Estudiante, 
       COUNT(l) AS CantidadLibrosPrestados

// Mostrar las categorías con más préstamos activos
MATCH (e:Estudiante)-[r:PRESTA]->(l:Libro)-[:PERTENECE_A]->(c:Categoria)
WHERE r.estado = "Activo"
RETURN c.nombre AS Categoria, 
       COUNT(r) AS PrestamosActivos
ORDER BY PrestamosActivos DESC

// Encontrar los estudiantes que no tienen préstamos activos
MATCH (e:Estudiante)
WHERE NOT EXISTS {
    MATCH (e)-[r:PRESTA]->()
    WHERE r.estado = "Activo"
}
RETURN e.nombre AS EstudianteSinPrestamosActivos, 
       e.legajo AS Legajo