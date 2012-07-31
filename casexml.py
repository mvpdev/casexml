#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

import os
import sys
import csv

from django.conf import settings
settings.configure()

from utils import transmit_form, save_casexmlform, check_file

import const as CONST

#Form Templates
from forms import CaseXMLInterface


class Main:

    format = ""
    file_name = ""
    save = True
    template = ""
    submit = False

    def __init__(self):
        ''' Get arguments '''
        args = sys.argv
        if len(args):
            try:
                self.format = args[1].lower()
                self.file_name = args[2]
                self.template = args[3]
            except:
                self.format = ""
                self.file_name = ""
                self.template = ""

            if self.format not in ('csv'):
                self.help()
            else:
                if not check_file(self.file_name, "csv"):
                    print "Invalid file location or file does not exist." \
                          "Check if it has a .csv extenion"
                else:
                    self.export_csv()
        else:
            self.help()

    def help(self):
        print (u"------------------------------------------\n"
                "GENERATE CASEXML USING DATA AND TEMPLATE \n"
                "------------------------------------------\n"
                "Contains function to generate Casexml and save or \n"
                "submit to CommcareHq\n"
                "To run:\n $ python casexml.py csvfile template "
                "\n\nOPTIONS:\n-------- \n"
                "csvfile     A full path of csv file to be exported to"
                " CommcareHQ ")

    def export_csv(self):
        info = {}
        #Check if template exist before
        if not check_file(self.template, "xml"):
            print "Template doesnot exist, or invalid template. Check if " \
                    "it has a .xml extenion"
            return 0

        try:
            data = csv.reader(open(self.file_name, 'rb'))
        except:
            print "Data doesnt exist"

        #Remove Header
        header = data.next()
        info = {}
        #Loop through each row and get data
        for x in data:
            for label, value in zip(header, x):
                info[label] = value

            form = CaseXMLInterface(info, self.template)
            save_casexmlform(form)
            transmit_form(form)


if __name__ == '__main__':
    main = Main()
