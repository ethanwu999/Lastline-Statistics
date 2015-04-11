# Lastline-Statistics
This is to show topN related data of Lastline Download and Mail

to run it please edit the bottom def main() part to filled with your own credential

this is a python3 program, run by: python3 ll_statistic.py

for UI version: https://youtu.be/7xLMjiQTvaA


#For Download:
top md5:
    score
    src_host
    dst_host
    application_protocol
    file_name
    extracted_filename
    content_disposition_filename
    llfiletype
    file_type
    
top src_host:
    dst_host
    application_protocol
    file_name
    extracted_filename
    llfiletype
    content_disposition_filename
    file_type
    
top dst_host:
    src_host
    application_protocol
    file_name
    extracted_filename
    llfiletype
    content_disposition_filename
    file_type
    
#For Mail:
top sender:
    recipient
    subject
    file_type
    llfiletype
    md5
    file_name

top recipient:
    sender
    subject
    file_type
    llfiletype
    md5
    file_name

top subject:
    sender
    recipient
    file_type
    llfiletype
    md5
    file_name

top md5:
    sender
    recipient
    file_type
    llfiletype
    subject
    file_name    
