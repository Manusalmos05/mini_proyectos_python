# 📋 Task Manager

## Sobre el proyecto

Este proyecto consiste en una aplicación de consola desarrollada en Python para gestionar tareas mediante operaciones CRUD (Crear, Consultar, Actualizar y Eliminar), utilizando MySQL como sistema de persistencia.

Su funcionalidad es deliberadamente sencilla. El verdadero objetivo del proyecto ha sido desarrollar una aplicación backend bien estructurada, aplicando principios de diseño, organización del código y buenas prácticas que se utilizan habitualmente en entornos profesionales.

Más que el resultado final, este repositorio pretende mostrar mi forma de desarrollar software.

---

## ¿Qué demuestra este proyecto?

Durante el desarrollo de esta aplicación he puesto en práctica competencias fundamentales para un desarrollador Backend Junior:

* Diseño de aplicaciones siguiendo una arquitectura por capas.
* Programación Orientada a Objetos (POO).
* Separación de responsabilidades entre la interfaz de usuario, la lógica de negocio y el acceso a datos.
* Implementación completa de operaciones CRUD.
* Integración con bases de datos MySQL.
* Validación de datos antes de acceder a la base de datos.
* Gestión de excepciones y control de errores.
* Organización modular del proyecto para facilitar su mantenimiento.
* Escritura de código limpio, reutilizable y documentado.

El objetivo ha sido construir una base sólida sobre la que seguir desarrollando proyectos de mayor complejidad.

---

## Arquitectura del proyecto

La aplicación está organizada siguiendo una arquitectura por capas, donde cada componente tiene una responsabilidad concreta:

```text
UI (Menu)
        │
        ▼
TaskService
        │
        ▼
TaskRepository
        │
        ▼
MySQL
```

Esta separación permite que cada parte de la aplicación evolucione de forma independiente, favoreciendo la mantenibilidad, la escalabilidad y la reutilización del código.

---

## Tecnologías utilizadas

* Python
* MySQL
* MySQL Connector/Python
* SQL
* Git

---

## Funcionalidades

* Crear tareas.
* Listar todas las tareas.
* Buscar tareas por ID.
* Marcar tareas como completadas.
* Eliminar tareas.
* Validación de datos de entrada.
* Persistencia de datos en MySQL.

---

## Lo que he aprendido

Este proyecto me ha permitido reforzar conocimientos fundamentales del desarrollo backend, especialmente en:

* Diseño de aplicaciones mediante capas.
* Organización y estructuración de proyectos Python.
* Comunicación entre la lógica de negocio y la base de datos.
* Modelado de entidades.
* Validación de reglas de negocio.
* Gestión de conexiones con MySQL.
* Desarrollo de código mantenible y fácil de extender.

---

## Sobre este repositorio

Este proyecto forma parte de mi portfolio como desarrolladora backend junior.

Mi intención con este repositorio no es demostrar que puedo desarrollar una aplicación compleja, sino evidenciar que conozco los fundamentos necesarios para construir software de forma ordenada, mantenible y escalable.

Cada proyecto que incorporo a mi portfolio tiene un objetivo de aprendizaje diferente y busca reflejar mi evolución como desarrolladora. Considero que una buena arquitectura, un código limpio y una correcta separación de responsabilidades son tan importantes como la funcionalidad de la propia aplicación.

Si eres reclutador o responsable técnico, agradeceré cualquier comentario o sugerencia que me ayude a seguir mejorando como profesional.
