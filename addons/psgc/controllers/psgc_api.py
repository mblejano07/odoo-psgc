import json
from odoo import http
from odoo.http import request, Response

class PSGCApiController(http.Controller):

    @http.route('/api/psgc/regions', type='http', auth='public', methods=['GET'], csrf=False)
    def get_regions(self):
        """Retrieve all regions"""
        regions = request.env['psgc.region'].sudo().search([])
        data = json.dumps({'regions': regions.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/provinces/<int:region_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_provinces(self, region_id):
        """Retrieve provinces based on a region"""
        provinces = request.env['psgc.province'].sudo().search([('region_id', '=', region_id)])
        data = json.dumps({'provinces': provinces.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/cities/<int:province_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_cities(self, province_id):
        """Retrieve cities based on a province"""
        cities = request.env['psgc.city'].sudo().search([('province_id', '=', province_id)])
        data = json.dumps({'cities': cities.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/barangays/<int:city_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_barangays(self, city_id):
        """Retrieve barangays based on a city"""
        barangays = request.env['psgc.barangay'].sudo().search([('city_id', '=', city_id)])
        data = json.dumps({'barangays': barangays.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)
