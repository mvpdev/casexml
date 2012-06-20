casexml
=======
An application for working with caseXML

This applications reads a CSV document and auto fill a casexml template.
This template is then pushed to commcare or saved in the output folder.

How it works

$ python casexml.py format filename_location template_name

Variables
==========
format:  This is  format of data you want to read. It can be either csv, or dict for dictionary
filename_location: This is the exact file_name. Use absolute location of tttthe file and dont forget to add file extesnsion
template_name: Name of the template you want to populate and save. This should be an xml file

example:
========
To generate casexml for data is Patient.csv and the casexml template is patient.xml use this command.

$python casexml.py csv Patient.csv template/patient.csv

