# Aden Challenge

![Aden logo](https://yt3.googleusercontent.com/ytc/APkrFKZ86iJwK77hghJF8SzlUHENo49XLjLlFZYcsS0_aw=s176-c-k-c0x00ffffff-no-rj)

## Contexto

### Crear un modulo de Odoo 16 que cumpla con lo siguiente:

   - Modelo Alumno que contenga los siguientes datos:
     - Nombre
     - Apellido
     - Fecha de nacimiento
     - Nro de legajo
     - Email
     - Teléfono
     - Dirección
     - País
   - Modelo Programa que contenga nombre y descripción
   - Modelo Inscripción que permita registrar que un alumno está inscripto a un programa
   - Función dentro del modelo programa que reciba como parámetro un programa y que retorne una lista de todos los alumnos que están inscriptos en el
   programa.

#### Ejemplo de respuesta:

```python 
[
    {
        'nombre': 'Cristian',
        'apellido': 'Ruppert',
        'legajo': 12548,
        'fecha_nacimiento': '1993-10-29'
        'email': 'cristian.ruppert@aden.org',
        'telefono': '+5492616861427',
        'pais': {
            'id': 587,
            'nombre': 'Argentina'
        }
    },
    {
        'nombre': 'Philipp',
        'apellido': 'Anderson',
        'legajo': 12549,
        'fecha_nacimiento': '1989-04-30'
        'email': 'philipp.anderson@test.com',
        'telefono': '+54912311111',
        'pais': {
            'id': 587,
            'nombre': 'Argentina'
        }
    }
]
