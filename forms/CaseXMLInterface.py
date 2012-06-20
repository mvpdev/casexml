#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
# maintainer: katembu

from datetime import date, datetime

from django.utils.translation import ugettext as _
from django.template import Context, Template
import time
import uuid

ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'


class CaseXMLInterface(object):

    # Template
    template_name = ""
    data = {}
    
    def __init__(self, data, template):

        # load template
        self.data = data
        self.data['instanceid'] = uuid.uuid4().hex
        self.data['caseid'] = uuid.uuid4().hex
        self.data['timestart'] = self._format_datetime(datetime.utcnow())
        self.data['timeend'] = self._format_datetime(datetime.utcnow())
        self.template_name = template
        self.load_template()

    def _format_datetime(self, time):
        return time.strftime(ISO_FORMAT)
   
    def set_template(self, set_temp):
        return set_temp
                 
    def load_template(self):
        fp = open('%(template)s' \
                % {'template': self.template_name})
        self.template = Template(fp.read())
        fp.close()

    def render(self):
        ''' returns the CaseXML formatted Form to Submit to Commcare '''
        rendered = self.template.render(Context(self.data))
        return rendered
