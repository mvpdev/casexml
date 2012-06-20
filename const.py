#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8
# maintainer: katembu

import os

#PUSH CASEXML TO COMMCARE DIRECTLY
SUBMIT_TO_COMMCARE = False

#COMMCARE DOMAIN URL
#COMMCARE_URL = "https://www.commcarehq.org/a/mvp/receiver/"
COMMCARE_URL = ""

#SAVE FORMS
STORE_FORM = True

#FORM LOCATION
CURRENT_FILE = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_FILE)
STORE_LOCATION  = os.path.join(PROJECT_ROOT, 'output')
