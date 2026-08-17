# 🛒 REST API para gestión de e-commerce con FastAPI

> **Proyecto backend desarrollado con Python y FastAPI para simular la arquitectura y el funcionamiento de una aplicación de comercio electrónico real.**

Este proyecto nació con un objetivo concreto: **pasar de aprender FastAPI a entender realmente cómo funciona una API en una aplicación moderna.**

La aplicación permite gestionar diferentes partes del flujo de compra de un e-commerce: **usuarios, autenticación, productos, categorías, carrito de compras y pedidos**, conectando la lógica de negocio con una base de datos relacional.

Más allá de crear endpoints, el proyecto me permitió trabajar con conceptos fundamentales del desarrollo backend que se utilizan en aplicaciones reales: **peticiones HTTP, validación de datos, autenticación, autorización, persistencia de información, operaciones CRUD, relaciones entre entidades y separación de responsabilidades.**

---

## 🚀 ¿Qué he construido?

La API está organizada alrededor de los principales recursos de una aplicación de comercio electrónico:

* 👤 **Usuarios** — registro, autenticación y gestión de usuarios.
* 🔐 **Autenticación y autorización** — protección de rutas mediante tokens y control de acceso.
* 📦 **Productos** — creación, consulta, actualización y eliminación de productos.
* 🏷️ **Categorías** — organización y búsqueda de productos por categoría.
* 🛒 **Carrito de compras** — incorporación y gestión de productos antes de realizar un pedido.
* 🧾 **Pedidos** — creación y gestión del proceso de compra.
* 💾 **Persistencia de datos** — almacenamiento y recuperación de información mediante una base de datos relacional.
* 🧪 **Testing** — pruebas específicas para funcionalidades de autenticación y productos.

---

## 🧠 Lo que aprendí desarrollando este proyecto

Este proyecto supuso un paso importante en mi aprendizaje de backend porque me permitió dejar de ver una API como una colección de endpoints y empezar a entender **qué problema resuelve dentro de una aplicación**.

### 🔄 Entender el flujo completo de una petición

Trabajé con el flujo que existe detrás de una operación aparentemente sencilla:

```text
Cliente
   ↓
HTTP Request
   ↓
Endpoint / Router
   ↓
Validación de datos
   ↓
Autenticación / autorización
   ↓
Lógica de negocio
   ↓
Base de datos
   ↓
HTTP Response
```

Esto me ayudó a comprender cómo una aplicación frontend puede comunicarse con un backend y cómo la API actúa como punto de comunicación entre diferentes partes del sistema.

### 🔐 Seguridad y autenticación

Implementé un sistema de autenticación basado en **tokens**, trabajando con rutas protegidas y dependencias de FastAPI.

Esto me permitió comprender conceptos como:

* Autenticación mediante usuario y contraseña.
* Generación y validación de tokens.
* Protección de endpoints.
* Dependencias para obtener el usuario autenticado.
* Control de acceso a determinadas operaciones.

### 💾 Bases de datos y ORM

Trabajé con modelos relacionados para representar entidades como:

**Usuarios → Pedidos → Productos → Carrito**

El proyecto utiliza una separación entre los modelos de persistencia y los esquemas utilizados para validar los datos que entran y salen de la API.

También incorporé **migraciones con Alembic**, lo que me permitió entender cómo evolucionar la estructura de una base de datos a medida que cambia una aplicación.

### 🧩 Separación de responsabilidades

Una de las partes más importantes del proyecto fue aprender a organizar el código para evitar concentrar toda la lógica en los endpoints.

La aplicación separa responsabilidades mediante diferentes módulos:

```text
app/
├── api/
│   └── v1/
├── crud/
├── models/
├── schemas/
├── db/
├── deps/
├── test/
├── alembic/
└── main.py
```

Esta organización me permitió entender mejor cómo estructurar un backend mantenible y preparado para seguir creciendo.

---

## 🛠️ Tecnologías utilizadas

| Tecnología               | Uso                                     |
| ------------------------ | --------------------------------------- |
| 🐍 **Python**            | Lenguaje principal                      |
| ⚡ **FastAPI**            | Desarrollo de la REST API               |
| 🔐 **OAuth2 / JWT**      | Autenticación y protección de rutas     |
| ✅ **Pydantic**           | Validación y serialización de datos     |
| 🗄️ **SQLAlchemy**       | ORM y comunicación con la base de datos |
| 🔄 **Alembic**           | Migraciones de base de datos            |
| 📚 **Swagger / OpenAPI** | Documentación y pruebas de la API       |
| 🧪 **Pytest**            | Testing                                 |

FastAPI genera automáticamente documentación interactiva basada en OpenAPI, permitiendo probar los endpoints directamente desde Swagger UI.

---

## 📡 Principales recursos de la API

La API está versionada mediante `/api/v1`, con routers independientes para las diferentes funcionalidades del sistema.

```text
/api/v1/auth
/api/v1/productos
/api/v1/categorias
/api/v1/carrito
/api/v1/pedido
```

Esta estructura permite mantener los recursos separados y facilita la evolución futura de la API.

---

## 🧪 Testing

El proyecto incorpora pruebas automatizadas para funcionalidades importantes del backend, incluyendo:

* 🔐 Autenticación.
* 📦 Gestión de productos.

```text
test/
├── test_auth.py
└── test_productos.py
```

Esto me permitió empezar a trabajar con una mentalidad diferente: **no limitarme a comprobar manualmente que una funcionalidad funciona, sino crear pruebas que permitan verificarla de forma reproducible.**

---

## 💡 ¿Por qué este proyecto?

Quise construir algo más cercano a un escenario profesional que una API basada únicamente en un CRUD sencillo.

Un e-commerce obliga a resolver diferentes problemas que aparecen habitualmente en aplicaciones reales:

**¿Quién está realizando la petición?**

↓

**¿Tiene permisos para realizarla?**

↓

**¿Los datos recibidos son válidos?**

↓

**¿Existe el producto solicitado?**

↓

**¿Hay stock disponible?**

↓

**¿Qué ocurre con el carrito?**

↓

**¿Cómo se transforma esa información en un pedido?**

Este tipo de problemas me ayudó a entender que desarrollar backend no consiste únicamente en crear endpoints, sino en **diseñar cómo circula, se valida, se protege y se persiste la información dentro de una aplicación.**

---

## 🎯 Habilidades desarrolladas

Este proyecto me permitió reforzar especialmente:

* Desarrollo de **REST APIs**.
* Programación backend con **Python**.
* Diseño y organización de aplicaciones con **FastAPI**.
* Manejo de **HTTP y endpoints**.
* Autenticación y autorización.
* Validación de datos con **Pydantic**.
* ORM y persistencia con **SQLAlchemy**.
* Operaciones **CRUD**.
* Relaciones entre entidades.
* Migraciones con **Alembic**.
* Organización modular del código.
* Gestión de dependencias en FastAPI.
* Testing de funcionalidades.
* Documentación y pruebas mediante **Swagger/OpenAPI**.
* Resolución y depuración de errores durante el desarrollo.

---

## 📈 Próximos pasos

Este proyecto forma parte de mi proceso de aprendizaje en desarrollo backend y representa una base sobre la que continuar incorporando funcionalidades y buenas prácticas utilizadas en entornos profesionales.

Mi objetivo no es únicamente aprender un framework concreto, sino **comprender cómo se construyen aplicaciones backend y cómo las diferentes piezas de un sistema trabajan juntas.**

---

### 👩‍💻 Sobre el proyecto

Desarrollado como proyecto personal para consolidar mis conocimientos de **Python, FastAPI, APIs REST, bases de datos y desarrollo backend**.

**Estoy construyendo proyectos para convertir conocimientos teóricos en experiencia práctica.** 🚀
