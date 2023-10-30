from odoo import models, fields

class Inscripcion(models.Model):
    _name = 'inscripcion.model'
    _description = 'Modelo de Inscripción'

    alumno_id = fields.Many2one('alumno.model', 'Alumno')
    programa_id = fields.Many2one('programa.model', 'Programa')