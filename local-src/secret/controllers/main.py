# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import odoo
import werkzeug
import logging
from odoo import _, http
from odoo.http import request
from werkzeug.utils import redirect
import random

_logger = logging.getLogger(__name__)

class Frontend(http.Controller):
    
    # Homepage
    @http.route([
        '/']
        , auth='public')
    def homepage(self, bn=None):

        # Get main page
        return request.render('secret.home', {})


    # Add a name
    @http.route('/add/', auth="public")
    def Register(self, **post):
        error = False
        secret = False
        
        if post:
            values = {
                'secret' : post['secret'].strip(),
                'ipaddress' : request.httprequest.environ['REMOTE_ADDR'],
            }
            if len(post['secret'].strip()) > 10:
                secret = request.env['secret.secret'].sudo().create(values)
                # return with a secret
                secrets = request.env['secret.secret'].search([])

                if secrets:
                    secret = random.choice(secrets)
                else:
                    # Aucun enregistrement trouvé
                    secret = None
            else:
                error = "Trop court"


        return request.render('secret.home', {
            'secret': secret,
            'error': error
        })