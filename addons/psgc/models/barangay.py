from odoo import models, fields

class Barangay(models.Model):
    _name = 'psgc.barangay'
    _description = 'Barangay'

    name = fields.Char(string='Name', required=True)
    brgy_code = fields.Char(string='Barangay Code', required=True)
    code_correspondence = fields.Char(string='Code Correspondence')
    geo_level = fields.Char(string='Geographical Level')
    old_name = fields.Char(string='Old Name')
    city_class = fields.Char(string='City Class')
    urb_rur = fields.Selection([
        ('U', 'Urban'),
        ('R', 'Rural'),
        ('-', '-')
    ], string='Urban/Rural', default='R')
    city = fields.Char(string='City Code')
    city_correspondence = fields.Char(string='City Correspondence')
    city_id = fields.Many2one('psgc.city', string='City/Municipality')
