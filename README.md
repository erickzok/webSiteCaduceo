# Página web para Gestión de Actividades Profesionales

Este proyecto consiste en una aplicación web desarrollada utilizando Flask en Python, diseñada para la gestión de actividades profesionales. La aplicación permite a los profesionales registrar sus actividades y al administrador visualizar estas actividades, junto con sus respectivas fechas y atributos adicionales. Además, la aplicación incluye un chatbot que permite a los usuarios realizar consultas sobre las actividades realizadas por un profesional específico.

## Funcionalidades principales:

1. **Inicio de Sesión:** Los usuarios pueden iniciar sesión en la plataforma utilizando sus credenciales, luego seran redirigidos a la pagina de inicio.

![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/d43ddec8-497f-414f-a670-eea29a946842)

![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/3ce39737-5605-4171-bedf-c59ccd64c627)

3. **Registro de Actividades:** Los profesionales pueden registrar sus actividades, incluyendo detalles como fecha, duración, descripción, etc.
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/f2cbc4cc-fcd6-429c-b71a-74126aa2e634)
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/4ef0f9c2-3114-4c57-8ccf-a8b6d4b9551a)


5. **Registro de nuevos usuarios**: Los profesionales nuevos pueden registrarse con su DNI y otros datos, sin embargo solo puede haber 1 cuenta asociada un numero de DNI.
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/f7fe2a4f-6343-4ce9-9906-503f47c3ddf7)


6. **Visualización de Actividades:** El administrador puede visualizar las actividades registradas por los profesionales, incluyendo detalles completos de cada actividad.
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/3e804a2b-e49b-4db2-8e0a-138f6c834b55)

7. **Chatbot de Consultas:** La aplicación cuenta con un chatbot que permite a los usuarios realizar consultas sobre las actividades realizadas por un profesional en particular y el tiempo dedicado a ellas.
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/b7608e6b-4099-48fa-817d-34f69667f2ce)

## Tecnologías utilizadas:

- **Flask:** Framework de desarrollo web en Python.
- **MySQL:** Sistema de gestión de bases de datos relacional para almacenar la información de actividades.
- **OpenAI API:** Se utiliza para el desarrollo del chatbot y responder preguntas sobre las actividades registradas.
- **PythonAnywhere:** Plataforma de alojamiento web para desplegar la aplicación.

## Modelo Relacional:

El modelo relacional asociado a la aplicación se muestra en la figura 1. Este modelo representa la estructura de la base de datos utilizada para almacenar la información de las actividades profesionales, incluyendo tablas para usuarios, actividades y cualquier otra entidad relacionada.
![image](https://github.com/erickzok/webSiteCaduceo/assets/121067321/d68839df-632e-4789-98ea-e04f5c6d06b0)

## Instrucciones de Despliegue:

1. Clona el repositorio desde GitHub.
2. Configura el entorno virtual y las dependencias de Flask.
3. Configura la base de datos MySQL y realiza las migraciones necesarias.
4. Obtén una API key de OpenAI y configúrala en el proyecto.
5. Despliega la aplicación en PythonAnywhere.

## Uso de la Aplicación:

1. Inicia sesión con tus credenciales.
2. Los profesionales pueden registrar nuevas actividades desde su panel.
3. El administrador puede acceder a la sección de visualización de actividades.
4. Usa el chatbot para realizar consultas sobre las actividades de un profesional específico.

## Contribuciones:

¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación, siéntete libre de hacer un fork del repositorio y enviar tus pull requests.

## Autor:

Este proyecto fue desarrollado por *erickzok* como parte de apoyo al área de contabilidad de para la empresa ***.

¡Gracias por utilizar nuestra aplicación! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto conmigo;).
