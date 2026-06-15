import re

#make an HTML file to write the contents
output_file_path = r"F:\learn programming\python and django\py doc latex\content_list.html"
MAX_LENGTH=120

#This function is added to convert digits to Persian digits
def to_persian_digits(text):
    persian = '۰۱۲۳۴۵۶۷۸۹'
    result = ''
    for ch in str(text):
        if ch.isdigit():
            result += persian[int(ch)]
        else:
            result += ch
    return result


#open .doc file 
with open(output_file_path, 'w', encoding='utf-8') as out_file:
    #just to organise the HTML file
    out_file.write('<html><head><meta charset="utf-8"></head>')
    out_file.write('<body dir="rtl" style="font-family:\'B Nazanin\', \'Vazirmatn\', Tahoma; font-size:14pt; line-height:2.2;">\n')
    
    with open(r"F:\learn programming\python and django\py doc latex\main.toc",'r', encoding='utf-8') as file:
        content=file.read()
    
    for line in content.split('\n'):
        #Split different parts of every line to read the title and page number of each line
        if "\\contentsline" in line:
            parts=line.split("}")
            #Since stared sections have different order, we should separate them to read the context properly
            if "section*" in line or "chapter*" in line:
                title=parts[1].replace("{","")
                title=title.replace("\u200c",chr(8204))
                page=parts[2].replace("{","")
                page = to_persian_digits(page)
            else:
                title=parts[2].replace("{","")
                title=title.replace("\u200c",chr(8204))
                page=parts[3].replace("{","")
                page = to_persian_digits(page)
                
    
            if "\\numberline" in line:
                line_parts=line.split('}{')
                line_number=line_parts[1]
                brace_start=line_number.find('{')
                brace_end=line_number.find('}',brace_start)
                number_sec=line_number[brace_start+1:brace_end]
                number_sec_fa = to_persian_digits(number_sec)
                title=number_sec_fa+" " +title

            #Order and tidy formulas in the content list, if there are any
            title = re.sub(r'(\$.*?\$)', r'<span dir="ltr" style="font-family:Tahoma;">\1</span>', title)

            #Content list indentation
            indent=""
            if "chapter" in line or "section*" in line or "chapter*" in line:
                indent=""
            elif "subsubsection" in line:
                indent="      "
            elif "subsection" in line:
                indent="    "
            elif "section" in line:
                indent="  "
            
            title_with_indent = indent + title
            title_with_dots = title_with_indent.ljust(MAX_LENGTH, ".")
            table_f = f'<div style="font-family:monospace, \'B Nazanin\'; white-space: pre-wrap; margin:0; text-align: right;">{title_with_dots} {page}</div>\n'
            out_file.write(table_f)
