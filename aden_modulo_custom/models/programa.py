from odoo import models, fields, api

class Programa(models.Model):
    _name = 'programa.model'
    _description = "Modelo de Programa"

    nombre = fields.Char('Nombre')
    descripcion = fields.Text('Descripción')

    @api.multi
    def get_alumnos_inscriptos(self):
        inscripciones = self.env['inscripcion.model'].search([('programa_id', '=', self.id)])
        alumnos_inscriptos = []

        for inscripcion in inscripciones:
            alumno = inscripcion.alumno_id
            alumnos_inscriptos.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'legajo': alumno.legajo,
                'fecha_nacimiento': alumno.fecha_nacimiento,
                'email': alumno.email,
                'telefono': alumno.telefono,
                'pais': {
                    'id': alumno.pais.id,
                    'nombre': alumno.pais.name,
                }
            })

        return alumnos_inscriptos
