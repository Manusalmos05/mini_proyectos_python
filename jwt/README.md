# JWT User API

> Una API de usuarios construida para entender qué ocurre detrás de un login moderno: desde la validación de los datos hasta la emisión de un token y el acceso protegido a los recursos.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141.1-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![JWT](https://img.shields.io/badge/Auth-JWT%20%2B%20OAuth2-000000)](https://jwt.io/)

## Para recruiters y equipos técnicos

Este proyecto demuestra una transición consciente desde escribir endpoints hacia diseñar un backend mantenible. La API resuelve un flujo real de identidad y acceso con una estructura separada por responsabilidades:

- **Routers** para exponer la API HTTP.
- **Schemas** para validar entradas y definir respuestas públicas.
- **Services** para concentrar reglas de negocio.
- **Repositories** para desacoplar la lógica de persistencia.
- **Entities** para mapear los modelos de dominio a la base de datos.
- **Dependencies** para gestionar sesiones, repositorios, servicios y usuario autenticado.
- **Security** para hash de contraseñas y tokens JWT.

La idea central es sencilla: que cada pieza tenga un trabajo claro y que añadir una funcionalidad no implique convertir el proyecto en una clase gigantesca con demasiados sombreros.

## Qué hace el proyecto

- Registra usuarios con email validado y contraseña protegida mediante `bcrypt`.
- Rechaza emails duplicados.
- Autentica usuarios con credenciales JSON.
- Incluye un flujo compatible con `OAuth2PasswordRequestForm`.
- Genera tokens JWT con expiración configurable.
- Protege los endpoints privados con `OAuth2PasswordBearer`.
- Restringe la consulta de detalle al usuario autenticado correspondiente.
- Persiste usuarios en MySQL mediante SQLAlchemy.
- Expone documentación interactiva automática con Swagger UI y ReDoc.
- Añade una cabecera `X-Process-Time` para observar el tiempo de procesamiento de cada request.

## Tecnologías utilizadas

### Lenguaje y framework

- Python 3.13
- FastAPI
- Uvicorn
- Pydantic 2


### Seguridad y autenticación

- JSON Web Tokens (JWT)
- OAuth2 Bearer
- Hasheo de contraseñas
- Control de expiración de tokens
- Autorización basada en el usuario autenticado

### Persistencia de datos

- MySQL
- SQLAlchemy 2
- MySQL Connector/Python
- Patrón Repository
- Inyección de dependencias para sesiones de base de datos

### Diseño y calidad del código

- Arquitectura por capas
- Separación entre entidades, DTOs y modelos de entrada
- Interfaces abstractas para repositorios y servicios
- Validación declarativa con Pydantic
- Manejo de errores HTTP
- Variables de entorno para configuración sensible

## Endpoints principales

| Método | Ruta | Acceso | Propósito |
|---|---|---|---|
| `POST` | `/users/` | Público | Crear un usuario |
| `POST` | `/auth/token` | Público | Iniciar sesión con JSON |
| `POST` | `/auth/token/form` | Público | Iniciar sesión con formulario OAuth2 |
| `GET` | `/users/` | JWT | Listar usuarios |
| `GET` | `/users/{user_id}` | JWT | Consultar el propio usuario |


## Lo que he aprendido

### 1. La autenticación no termina en el login

Aprendí a diferenciar autenticación de autorización: primero se verifica quién es el usuario; después se decide qué puede consultar. Un token válido no es una licencia para acceder a cualquier recurso.

### 2. La seguridad debe formar parte del diseño

Las contraseñas nunca se almacenan en texto plano. Se transforman mediante `bcrypt`, mientras que el JWT contiene una identidad limitada y una fecha de expiración. También aprendí a mantener secretos y credenciales fuera del código fuente mediante variables de entorno.

### 3. La inyección de dependencias reduce el acoplamiento

FastAPI permite declarar dependencias directamente en los endpoints. Esto facilita crear sesiones por request, intercambiar implementaciones y mantener la lógica de infraestructura fuera de los routers.

### 4. Los contratos claros hacen APIs más confiables

Con Pydantic aprendí a validar emails, limitar contraseñas, definir DTOs de respuesta y evitar que el modelo interno de base de datos se convierta automáticamente en el contrato público de la API.

### 5. Las capas importan cuando el proyecto crece

Separar router, servicio y repositorio ayuda a localizar responsabilidades y prepara el código para evolucionar: cambiar una consulta, una regla de negocio o una implementación de persistencia no debería obligar a reescribir toda la API.

### 6. Los errores también son parte del producto

El proyecto utiliza códigos HTTP con intención: `201` al crear, `400` ante datos inválidos, `401` ante credenciales o tokens inválidos, `403` cuando falta autorización y `404` cuando un usuario no existe.

## Por qué este proyecto es importante

Un sistema de usuarios es una pieza pequeña, pero concentra varios problemas que aparecen en productos reales: identidad, datos sensibles, permisos, persistencia, contratos, errores y observabilidad. Resolverlo obliga a pensar más allá de “hacer que el endpoint responda”.

Para un equipo de selección, este proyecto sirve como evidencia de que estoy desarrollando criterio sobre:

- cómo estructurar una aplicación backend;
- cómo proteger información sensible;
- cómo diseñar contratos HTTP consistentes;
- cómo separar reglas de negocio de acceso a datos;
- cómo documentar y probar una API desde una interfaz interactiva;
- cómo identificar decisiones que deberán endurecerse antes de producción.

## Por qué aprender FastAPI es valioso para un programador junior

FastAPI es especialmente útil para aprender backend porque convierte buenas prácticas en algo visible y ejecutable:

- La documentación OpenAPI se genera automáticamente y permite probar la API desde el navegador.
- Los tipos de Python se convierten en validación y documentación, conectando teoría con comportamiento real.
- La inyección de dependencias enseña composición y desacoplamiento desde el comienzo.
- Su rendimiento y compatibilidad con ASGI acercan al desarrollador junior a patrones usados en servicios modernos.
- Su sintaxis permite concentrarse en HTTP, seguridad, datos y arquitectura sin pelearse con una capa de configuración innecesaria.

Aprender FastAPI no consiste solo en aprender otro framework. Consiste en practicar cómo construir servicios que otros desarrolladores puedan entender, integrar y mantener. Y esa habilidad viaja mucho mejor que cualquier tutorial terminado.

