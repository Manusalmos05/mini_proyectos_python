# 🚀 API de Gestión de Clientes — FastAPI

API REST desarrollada con **Python y FastAPI** para gestionar clientes mediante operaciones CRUD: crear, consultar, actualizar y eliminar registros.

Este proyecto nace como ejercicio práctico para comprender cómo funciona una **API REST en un entorno backend real**, desde la recepción de una petición HTTP hasta la validación de los datos y la respuesta al cliente.

Aunque la persistencia de datos se realiza actualmente mediante un archivo **CSV**, la aplicación está estructurada de forma que la lógica de la API y la gestión de los datos permanecen separadas.

---

## 🎯 Objetivo del proyecto

El objetivo principal es poner en práctica los conceptos fundamentales del desarrollo backend:

* Diseño de endpoints REST.
* Métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`).
* Validación de datos con **Pydantic**.
* Gestión de errores HTTP.
* Serialización de objetos a JSON.
* Separación entre lógica de API y acceso a datos.
* Creación de documentación automática con FastAPI.
* Implementación de operaciones CRUD.

Más allá de crear una API que "funcione", el proyecto busca entender **qué ocurre cuando una aplicación cliente realiza una petición al backend y cómo se procesa esa información**.

---

## 🛠️ Tecnologías utilizadas

| Tecnología           | Uso                                   |
| -------------------- | ------------------------------------- |
| 🐍 Python            | Lenguaje principal                    |
| ⚡ FastAPI            | Framework para construir la API REST  |
| 📦 Pydantic          | Validación y modelado de datos        |
| 📄 CSV               | Persistencia de datos                 |
| 🔄 JSON              | Formato de intercambio de información |
| 📚 Swagger / OpenAPI | Documentación y pruebas de endpoints  |

---

## 🏗️ Arquitectura

La aplicación sigue una estructura sencilla en la que cada parte tiene una responsabilidad concreta:

```text
Cliente
   │
   │ HTTP Request
   ▼
┌─────────────────────┐
│      FastAPI        │
│                     │
│  Endpoints REST     │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│      Pydantic       │
│                     │
│ Validación de datos │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│      database.py    │
│                     │
│ CRUD de clientes    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│       CSV           │
│                     │
│ Persistencia datos  │
└─────────────────────┘
```

Esta separación permite entender uno de los principios fundamentales del desarrollo backend: **la API no debería encargarse directamente de toda la lógica de acceso a los datos**.

---
## 🧩 Validación con Pydantic

Uno de los aspectos importantes del proyecto es el uso de modelos de **Pydantic** para controlar los datos que recibe la API.

Por ejemplo:

```python
class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)
```

De esta forma, FastAPI puede validar automáticamente características como:

* Longitud del DNI.
* Longitud del nombre.
* Longitud del apellido.
* Tipo de los datos recibidos.

Además, se implementó una validación personalizada:

```python
@field_validator("dni")
def validar_dni(cls, dni):
```

que permite comprobar que el DNI sea válido y que no exista previamente en la base de datos.

---

## ⚠️ Gestión de errores

La API utiliza `HTTPException` para devolver respuestas HTTP apropiadas cuando una operación no puede realizarse.

Por ejemplo:

```python
raise HTTPException(
    status_code=404,
    detail="cliente no encontrado"
)
```

Esto permite que el consumidor de la API pueda distinguir fácilmente entre una operación correcta y diferentes situaciones de error.

---

## 💡 Qué he aprendido con este proyecto

Este proyecto me ha servido para comprender mejor **cómo se construyen las APIs desde el backend**.

Durante su desarrollo he trabajado conceptos como:

* Arquitectura de una API REST.
* Funcionamiento de las peticiones HTTP.
* Métodos y códigos de estado HTTP.
* Validación de información recibida.
* Modelos Pydantic.
* Operaciones CRUD.
* Manejo de excepciones.
* Serialización JSON.
* Separación de responsabilidades.
* Documentación automática mediante OpenAPI.

También me ha permitido entender que una API no es simplemente un conjunto de URLs, sino una **capa de comunicación entre diferentes partes de una aplicación**.


---

## 👩‍💻 Sobre el proyecto

Este proyecto forma parte de mi proceso de aprendizaje y especialización en **desarrollo backend con Python**.

Mi objetivo no es únicamente aprender frameworks, sino comprender cómo se construyen las aplicaciones que utilizamos diariamente y cómo diferentes sistemas se comunican entre sí mediante APIs.

**Cada proyecto es una oportunidad para convertir teoría en código y seguir construyendo experiencia real como desarrolladora junior.** 🚀

---

### ⭐ Si te resulta interesante

Si estás interesado/a en desarrollo backend, APIs REST o Python, puedes explorar el código del proyecto y seguir mi evolución a través de GitHub.
