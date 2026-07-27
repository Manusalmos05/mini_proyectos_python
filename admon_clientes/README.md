## 🎯 Valor Técnico y Competencias Desarrolladas

Este proyecto simula un escenario de desarrollo profesional donde se implementa una aplicación de consola empresarial utilizando una arquitectura limpia y desacoplada. Está diseñado específicamente para demostrar habilidades sólidas en el manejo de bases de datos, patrones de diseño y desarrollo orientado a objetos en Python.

### 🧠 Aprendizajes Clave
* **Arquitectura en Capas (Patrón DAO):** Implementación del patrón *Data Access Object* (DAO) para separar de forma estricta la lógica de negocio (capa de presentación/menú) de la persistencia de datos (MySQL), facilitando la escalabilidad y el mantenimiento del código.
* **Gestión Eficiente de Recursos y Conexiones:** Control del ciclo de vida de las conexiones a la base de datos mediante bloques `try-except-finally`, asegurando la liberación manual de recursos (`cursor.close()`) para prevenir fugas de memoria y bloqueos en entornos de producción.
* **Resolución de Bugs en Tiempo de Ejecución:** Diagnóstico y corrección de errores críticos de tipado (como la diferencia entre atributos de estado de cursores de red frente a llamadas a métodos en conectores nativos de bases de datos).

### 🛠️ Competencias Técnicas Empleadas
* **Python Avanzado:** Uso de decoradores estructurales (`@classmethod`, `@staticmethod`) para optimizar el comportamiento de los métodos según su contexto de ejecución.
* **Modelado de Datos Dinámico:** Mapeo relacional manual (ORM conceptual) transformando tuplas crudas de SQL (`fetchall()`) en objetos fuertemente tipados (`Cliente`).
* **Robustez en SQL:** Construcción de consultas preparadas paramétricas (`%s`) para mitigar vulnerabilidades críticas de seguridad como la *Inyección SQL*.
* **Defensive Programming:** Diseño de flujos de control basados en manejo de excepciones robusto para capturar errores de entrada de usuario (`ValueError`) sin provocar la caída de la aplicación.
