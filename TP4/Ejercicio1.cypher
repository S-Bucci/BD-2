// ====================================
// EJERCICIO 1: SISTEMA DE GESTIÓN DE PROYECTOS
// ====================================

// 1. MODELADO - Crear nodos y relaciones

// Crear Departamentos
CREATE (d1:Departamento {nombre: "Desarrollo", ubicacion: "Piso 3"})
CREATE (d2:Departamento {nombre: "Marketing", ubicacion: "Piso 2"})
CREATE (d3:Departamento {nombre: "Recursos Humanos", ubicacion: "Piso 1"})

// Crear Empleados
CREATE (e1:Empleado {nombre: "Juan Pérez", email: "juan.perez@empresa.com", cargo: "Desarrollador Senior"})
CREATE (e2:Empleado {nombre: "María García", email: "maria.garcia@empresa.com", cargo: "Analista de Marketing"})
CREATE (e3:Empleado {nombre: "Carlos López", email: "carlos.lopez@empresa.com", cargo: "Desarrollador Junior"})
CREATE (e4:Empleado {nombre: "Ana Martínez", email: "ana.martinez@empresa.com", cargo: "Especialista en RRHH"})

// Crear Proyectos
CREATE (p1:Proyecto {nombre: "Sistema ERP", descripcion: "Implementación de sistema ERP", fechaInicio: "2024-01-15", fechaFin: "2024-06-30"})
CREATE (p2:Proyecto {nombre: "Campaña Digital", descripcion: "Campaña de marketing digital", fechaInicio: "2024-02-01", fechaFin: "2024-04-30"})
// Establecer relaciones: Empleados pertenecen a Departamentos
MATCH (e1:Empleado {nombre: "Juan Pérez"}), (d1:Departamento {nombre: "Desarrollo"})
CREATE (e1)-[:PERTENECE_A]->(d1)

MATCH (e2:Empleado {nombre: "María García"}), (d2:Departamento {nombre: "Marketing"})
CREATE (e2)-[:PERTENECE_A]->(d2)

MATCH (e3:Empleado {nombre: "Carlos López"}), (d1:Departamento {nombre: "Desarrollo"})
CREATE (e3)-[:PERTENECE_A]->(d1)

MATCH (e4:Empleado {nombre: "Ana Martínez"}), (d3:Departamento {nombre: "Recursos Humanos"})
CREATE (e4)-[:PERTENECE_A]->(d3)

// Asignar empleados a proyectos con horas semanales
MATCH (e1:Empleado {nombre: "Juan Pérez"}), (p1:Proyecto {nombre: "Sistema ERP"})
CREATE (e1)-[:ASIGNADO_A {horasSemanales: 40}]->(p1)

MATCH (e2:Empleado {nombre: "María García"}), (p2:Proyecto {nombre: "Campaña Digital"})
CREATE (e2)-[:ASIGNADO_A {horasSemanales: 35}]->(p2)

MATCH (e3:Empleado {nombre: "Carlos López"}), (p1:Proyecto {nombre: "Sistema ERP"})
CREATE (e3)-[:ASIGNADO_A {horasSemanales: 30}]->(p1)

MATCH (e3:Empleado {nombre: "Carlos López"}), (p2:Proyecto {nombre: "Campaña Digital"})
CREATE (e3)-[:ASIGNADO_A {horasSemanales: 10}]->(p2)

MATCH (e4:Empleado {nombre: "Ana Martínez"}), (p1:Proyecto {nombre: "Sistema ERP"})
CREATE (e4)-[:ASIGNADO_A {horasSemanales: 15}]->(p1)

// Asignar líderes a proyectos
MATCH (e1:Empleado {nombre: "Juan Pérez"}), (p1:Proyecto {nombre: "Sistema ERP"})
CREATE (e1)-[:LIDERA]->(p1)

MATCH (e2:Empleado {nombre: "María García"}), (p2:Proyecto {nombre: "Campaña Digital"})
CREATE (e2)-[:LIDERA]->(p2)
/ 2. CONSULTAS

// Obtener el nombre del proyecto, su líder y los empleados asignados
MATCH (p:Proyecto)<-[:LIDERA]-(lider:Empleado)
MATCH (p)<-[:ASIGNADO_A]-(empleado:Empleado)
RETURN p.nombre AS Proyecto, 
       lider.nombre AS Lider, 
       COLLECT(empleado.nombre) AS EmpleadosAsignados

// Calcular el total de horas semanales por proyecto
MATCH (p:Proyecto)<-[r:ASIGNADO_A]-(e:Empleado)
RETURN p.nombre AS Proyecto, 
       SUM(r.horasSemanales) AS TotalHorasSemanales

// Listar los empleados que trabajan en más de un proyecto
MATCH (e:Empleado)-[:ASIGNADO_A]->(p:Proyecto)
WITH e, COUNT(p) AS numProyectos
WHERE numProyectos > 1
RETURN e.nombre AS Empleado, numProyectos AS CantidadProyectos