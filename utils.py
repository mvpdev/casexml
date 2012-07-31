#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
# maintainer: katembu
import os
from urlparse import urlparse
import httplib

from datetime import datetime
import const as CONST


def transmit_form(form):
    ''' Submit data to commcare server '''

    xml_form = form.render()
    headers = {"Content-type": "text/xml", "Accept": "text/plain"}

    try:
        DOMAIN_URL = CONST.COMMCARE_URL
        SUBMIT_CASEXML = CONST.SUBMIT_TO_COMMCARE
    except:
        SUBMIT_CASEXML = False
        DOMAIN_URL = u""

    if SUBMIT_CASEXML:

        print DOMAIN_URL

        url = DOMAIN_URL
        up = urlparse(url)
        conn = httplib.HTTPSConnection(up.netloc) if url.startswith("https") \
                                        else httplib.HTTPConnection(up.netloc)
        conn.request('POST', up.path, xml_form, headers)
        resp = conn.getresponse()
        responsetext = resp.read()
        assert resp.status == 201, 'Bad HTTP Response'
        assert "Thanks for submitting" in responsetext, "Bad response text"


def save_casexmlform(form):
    ''' save templates of casexml '''
    xml_form = form.render()
    try:
        STORE_FORM = CONST.STORE_FORM
        STORE_LOCATION = CONST.STORE_LOCATION
    except:
        STORE_FORM = False
        STORE_LOCATION = u"/tmp"

    if STORE_FORM:
        print "Saving Form in output folder"
        f = open("%(path)s/casexml_%(date)s.xml" % {\
                'path': STORE_LOCATION, \
                'date': datetime.now().strftime("%Y_%m_%d_%H:%M:%S")}, \
                'wb', buffering=1)

        f.write(str(xml_form))
        f.close()


def check_file(file_name, ftype):
    exist = True
    if not os.path.exists(file_name):
        exist = False
    if file_name.split(".")[-1] != ftype:
        exist = False

    return exist
