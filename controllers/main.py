# -*- coding: utf-8 -*-
import base64
import werkzeug
import werkzeug.urls
from openerp import http, SUPERUSER_ID
from openerp.http import request
from openerp.tools.translate import _


class shuttle_website(http.Controller):
    
    def populate_values(self):
        values = []
        cr, context = request.cr, request.context
        vehicle_ids = request.registry['fleet.vehicle'].search(cr, SUPERUSER_ID,[])
        driver_ids = request.registry('res.partner').search(cr,SUPERUSER_ID,[('is_driver','=',True)])
        driver_info =  request.registry('res.partner').read(cr,SUPERUSER_ID,driver_ids,['name','operator'])
        # sorting drivers based on operators
        operator_driver = {}
        for i in driver_info:
            if i.get('operator',False):
                if i.get('operator',False)[0] in operator_driver.keys():
                    operator_driver[i['operator'][0]].append({
                                                           'id':i['id'],
                                                           'name':i['name']
                                                           })
                else:
                    operator_driver.update({
                                            i.get('operator',False)[0]:[{
                                                                     'id':i['id'],
                                                                     'name':i['name']
                                                                     }]
                                            })
        for vehicle in request.registry('fleet.vehicle').browse(cr,SUPERUSER_ID,vehicle_ids,context):
            if vehicle.operator and vehicle.operator.id in operator_driver.keys():
                # looking for drivers for the operator in the driver_info
                values.append(
                              {
                                           'name':vehicle.name,
                                           'id':vehicle.id,
                                           'current_driver':vehicle.driver_id.id,
                                           'driver_ids':operator_driver[vehicle.operator.id]
                                           }
                               )
            else:
                values.append(
                               {
                                           'name':vehicle.name,
                                           'id':vehicle.id,
                                           'current_driver':vehicle.driver_id.id,
                                           'driver_ids':driver_info
                                           }
                               ) 
        return values       
    
    @http.route(['/page/change_driver'], type='http', auth="user", website=True,methods=['post'])
    def write_changed_drivers(self, **kwargs):
        cr, context = request.cr, request.context
        vehicle = request.registry['fleet.vehicle']
        for i in kwargs:
            if kwargs.get(i,False):
                driver_id = int(kwargs.get(i,False))
                vehicle.write(cr,SUPERUSER_ID,int(i),{
                                             'driver_id':driver_id
                                             },context)
        
        values = self.populate_values()
        return request.website.render("shuttle_website.render_fleet_driver", {'info':values,'acknowledge':True})
    
    @http.route(['/page/home_change_driver'], type='http', auth="user", website=True)
    def load_values(self, **kwargs):
        values = self.populate_values()
        return request.website.render("shuttle_website.render_fleet_driver", {'info':values,'acknowledge':False})

