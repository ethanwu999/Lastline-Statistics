# Lastline-Statistics
This is to show topN related data of Lastline Download and Mail


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
