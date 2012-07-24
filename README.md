casexml
=======
An application for generating and pushing CaseXML to commcareHQ

This applications both works for CSV document or Dictionary and it auto fill data to casexml template.
This template is then pushed to commcare or saved in the output folder.

How it works:

    # Create a casexml template using

    # Prepare the data to export into a csv file. Ensure the headings is one word for each row.

    # CSV heading should match the template tags

    # To run: $ python casexml.py format filename_location template_name

Variables
==========
format:             This is  format of data you want to read. It can be either csv, or dict for dictionary 

filename_location:  This is the exact file_name. Use absolute location of tttthe file and dont forget to add file extension.

template_name:      Name of the template you want to populate and save. This should be an xml file.

example:
========
To generate casexml for data in Patient.csv and the casexml template is patient.xml use this command.

$python casexml.py csv Patient.csv template/patient.xml

