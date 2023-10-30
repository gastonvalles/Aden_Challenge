from odoo import api, fields, models

class Alumno(models.Model):
    _name = 'alumno.model'

    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    legajo = fields.Char(string='Nro de Legajo')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    email = fields.Char(string='Email')
    telefono = fields.Char(string='Teléfono')
    pais = fields.Many2one('res.country', string='País')
