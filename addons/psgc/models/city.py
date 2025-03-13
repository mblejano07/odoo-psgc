from odoo import models, fields

class City(models.Model):
    _name = "psgc.city"
    _description = "City/Municipality"
    _rec_name = "name"

    code_correspondence = fields.Char(string="Code Correspondence", required=True)
    name = fields.Char(string="City/Municipality Name", required=True)
    city_code = fields.Char(string="City Code", required=True)
    
    classification = fields.Selection([
        ('Municipality', 'Municipality'),
        ('City', 'City'),
        ('SubMun', 'Sub-Municipality'), 
    ], string="Classification", required=True)

    old_name = fields.Char(string="Old Name")
    city_class = fields.Char(string="City Class")
    
    income_classification = fields.Selection([
        ('1st', '1st Class'),
        ('2nd', '2nd Class'),
        ('3rd', '3rd Class'),
        ('4th', '4th Class'),
        ('5th', '5th Class'),
        ('6th', '6th Class'),
        ('Special', 'Special'),
    ], string="Income Classification")

    province_id = fields.Many2one('psgc.province', string="Province", required=True)
    province_code = fields.Char(string="Province Code", required=True)
    province_correspondence = fields.Char(string="Province Correspondence")
