import re

Path = "Your Path here"

#make an html file to write the contents
output_file_path = fr"{Path}\content_list_pr.html"
MAX_LENGTH=120
#open .doc file 
with open(output_file_path, 'w', encoding='utf-8') as out_file:
    #just to organise the HTML file
    out_file.write('<html><head><meta charset="utf-8"></head>')
    out_file.write('<body dir="rtl" style="font-family:\'B Nazanin\', \'Vazirmatn\', Tahoma; font-size:14pt; line-height:2.2;">\n')
    
    with open(fr"{Path}\file.toc",'r', encoding='utf-8') as file:
        content=file.read()
    
    for line in content.split('\n'):
        #Split different parts of every line to read the title and page number of each line
        if "\\contentsline" in line:
            parts=line.split("}")
            #Since starred sections have a different order, we should separate them to read the context properly
            if "section*" in line or "chapter*" in line:
                title=parts[1].replace("{","")
                title=title.replace("\u200c",chr(8204))
                page=parts[2].replace("{","")
            else:
                title=parts[2].replace("{","")
                title=title.replace("\u200c",chr(8204))
                page=parts[3].replace("{","")
    
            if "\\numberline" in line:
                line_parts=line.split('}{')
                line_number=line_parts[1]
                brace_start=line_number.find('{')
                brace_end=line_number.find('}',brace_start)
                number_sec=line_number[brace_start+1:brace_end]
                title=number_sec+" " +title
            #Order and tidy formulas in the content list, if there is any
            title = re.sub(r'(\$.*?\$)', r'<span dir="ltr" style="font-family:Tahoma;">\1</span>', title)

            #Content list indentation
            indent=""
            if "chapter" in line or "section*" in line or "chapter*" in line:
                indent=""
            elif "subsubsection" in line:
                indent="      "
            elif "section" in line:
                indent="  "
            
            title_with_indent = indent + title
            title_with_dots = title_with_indent.ljust(MAX_LENGTH, ".")
            table_f = f'<div style="font-family:monospace, \'B Nazanin\'; white-space: pre-wrap; margin:0; text-align: right;">{title_with_dots} {page}</div>\n'
            out_file.write(table_f)
        out_file.write('</body></html>')
