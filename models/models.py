# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import logging
import re
from odoo.exceptions import ValidationError

class canso(models.Model):
    _name = 'examen.canso'
    _description = 'examen.canso'

    name = fields.Char(string="Nom canço", help='Este es el nom de la canço')
    clients = fields.Many2many('res.partner', help='Una canço pot tindre molts clients')
    popularitat = fields.Integer(default='0')

class client(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    favorit_canso =  fields.Many2many('examen.canso', 'name', help='Una canço pot tindre molts clients')

class canso_wizard(models.TransientModel):
    _name = 'examen.canso_wizard'

    cansons_new = fields.Many2one('examen.canso', help='Una canço pot tindre molts clients')
    puntuacion = fields.Integer(default='0')

    #Al apretar en lanzar wizard
    @api.model
    def action_nueva_canso_wizard(self):
        action = self.env.ref('examen.action_nueva_canso_wizard').read()[0]
        return action