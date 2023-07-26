# Arquitectura por capas, mezclado con Hexagonal y DD

La arquitectura por capas es un patrón de diseño de software

Hexagonal es un patrón de diseño de software.

Domain Driven Design (DDD) es un enfoque para el desarrollo de software que prioriza el diseño de software 
para satisfacer las necesidades de las empresas en lugar de enfocarse en la tecnología subyacente.

Se pretende hacer código mantenible y escalable en el futuro.

![image](image.png)


# UI

La capa de cliente es la capa que contiene la interfaz de usuario de la aplicación.
Puede ser una aplicación web, una aplicación móvil o una aplicación de escritorio etc..


# Domain

Este será el núcleo de la aplicación. Es la capa donde se incluyen todas las reglas de negocio relacionadas con el problema a resolver.

Esta capa debe mantenerse alejada de las dependencias tanto como sea posible. 

Las bibliotecas de terceros no deben agregarse tanto como sea posible, ya que no deben tomar otras capas como referencia


# Application

Esta es la capa que contiene la lógica de negocio de la aplicación.

La capa de aplicación solo puede depender del dominio.


# Infrastructure
# Repository

La capa de infrastructura solo puede depender de la capa de applicación y dominio.

 El patrón de diseño Repositorio separa la lógica de acceso a datos 
 de diferentes fuentes. La idea básica es crear una especie de capa 
 abstracta entre la aplicación y el almacenamiento de datos. 
 Esta capa abstracta se llama repositorio. 
 Proporciona un conjunto de métodos para que la aplicación interactúe con los datos.

 Los métodos más comunes son:
 - Guardar
 - Eliminar
 - Actualizar
 - Recuperar

 El patron de diseño de repositorio tiene una serie de ventajas:

- Aumenta la flexibilidad
- Aumenta la escalabilidad
- Aumenta la mantenibilidad

# __init__.py

Este archivo es necesario para que Python trate los directorios como paquetes.