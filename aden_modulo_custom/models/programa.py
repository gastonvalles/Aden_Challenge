from odoo import models, fields, api

class Programa(models.Model):
    _name = 'programa.model'
    _description = 'Modelo de Programa'

    nombre = fields.Char('Nombre')
    descripcion = fields.Text('Descripción')
