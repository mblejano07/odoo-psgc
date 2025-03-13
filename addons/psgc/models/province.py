from odoo import models, fields

class Province(models.Model):
    _name = 'psgc.province'
    _description = 'Province'

    id = fields.Char(string='ID', required=True)  # Or you can use Integer if necessary
    code_correspondence = fields.Char(string='Code Correspondence')
    name = fields.Char(string='Province Name', required=True)
    province_code = fields.Char(string='Province Code', required=True)
    geo_level = fields.Char(string='Geographical Level')
    old_name = fields.Char(string='Old Name')
    income_classification = fields.Selection([
        ('1st', '1st Income Class'),
        ('2nd', '2nd Income Class'),
        ('3rd', '3rd Income Class'),
        ('4th', '4th Income Class'),
        ('5th', '5th Income Class'),
    ], string='Income Classification')
    region_code = fields.Char(string='Region Code')
    region_correspondence = fields.Char(string='Region Correspondence')
    region_id = fields.Many2one('psgc.region', string='Region', required=True)  # Link to Region model
