# Author: bbrighttaer
# Project: authservice
# Date: 10/23/2020
# Time: 5:21 AM
# File: renderers.py

from __future__ import absolute_import, division, print_function, unicode_literals

import json

from rest_framework import renderers


class OutBoundDataRenderer(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if 'ErrorDetail' in repr(data):
            response = json.dumps({'errors': data})
        else:
            response = json.dumps({'data': data})
        return response
