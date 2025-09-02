# Proyecto Urban Routes

##  Descripción del proyecto
Este proyecto contiene pruebas automatizadas para validar el flujo de usuario en la aplicación **Urban Routes**.

Las pruebas están escritas utilizando la arquitectura **Page Object Model (POM)**, lo que permite una estructura clara y mantenible del código.

##  Tecnologías y técnicas utilizadas

- **Lenguaje**: Python 3.13
- **Automatización de pruebas**: Selenium WebDriver
- **Framework de pruebas**: Pytest
- **Arquitectura**: Page Object Model (POM)
- **IDE sugerido**: PyCharm

Se utilizaron técnicas como:
- Esperas explícitas para asegurar que los elementos estén disponibles antes de interactuar con ellos.
- Asserts para validar el comportamiento esperado de la interfaz.
- Localizadores robustos utilizando `By.XPATH`, `By.CLASS_NAME`.


## Algunas Pruebas implementadas

- Agregar una tarjeta de crédito como método de pago
- Verificar cantidad de helados seleccionados
- Validar que aparece el modal de “Buscar automóvil” al pedir un taxi

## Como ejecutar las pruebas
1-Clona el siguiente repositorio en tu computadora (si no lo hiciste aún): git clone git@github.com:username/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
2-Necesitas tener instalados los paquetes pip install selenium pytest
Configura el WebDriver para el navegador que usarás (ChromeDriver) y asegurate de que esté accesible en tu PATH.
Ejecuta las pruebas usando Pytest

## Autora
Adiaris Santana
GitHub: AA3425-BY
Sprint 8
