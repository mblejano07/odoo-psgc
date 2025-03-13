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

    @http.route('/api/psgc/regions/<int:region_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_region(self, region_id):
        """Retrieve a specific region by ID"""
        region = request.env['psgc.region'].sudo().browse(region_id)
        data = json.dumps({'region': region.read(['id', 'name'])[0]})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/provinces/<int:region_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_provinces(self, region_id):
        """Retrieve provinces based on a region"""
        provinces = request.env['psgc.province'].sudo().search([('region_id', '=', region_id)])
        data = json.dumps({'provinces': provinces.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/provinces/specific/<int:province_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_province(self, province_id):
        """Retrieve a specific province by ID"""
        province = request.env['psgc.province'].sudo().browse(province_id)
        data = json.dumps({'province': province.read(['id', 'name'])[0]})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/cities/<int:province_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_cities(self, province_id):
        """Retrieve cities based on a province"""
        cities = request.env['psgc.city'].sudo().search([('province_id', '=', province_id)])
        data = json.dumps({'cities': cities.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/cities/specific/<int:city_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_city(self, city_id):
        """Retrieve a specific city by ID"""
        city = request.env['psgc.city'].sudo().browse(city_id)
        data = json.dumps({'city': city.read(['id', 'name'])[0]})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/barangays/<int:city_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_barangays(self, city_id):
        """Retrieve barangays based on a city"""
        barangays = request.env['psgc.barangay'].sudo().search([('city_id', '=', city_id)])
        data = json.dumps({'barangays': barangays.read(['id', 'name'])})
        return Response(data, content_type='application/json', status=200)

    @http.route('/api/psgc/barangays/specific/<int:barangay_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_barangay(self, barangay_id):
        """Retrieve a specific barangay by ID"""
        barangay = request.env['psgc.barangay'].sudo().browse(barangay_id)
        data = json.dumps({'barangay': barangay.read(['id', 'name'])[0]})
        return Response(data, content_type='application/json', status=200)
