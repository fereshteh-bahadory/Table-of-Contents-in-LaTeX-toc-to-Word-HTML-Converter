import re

Path = "Your Path here"

output_file_path = fr"{Path}\content_list_pr.html"
MAX_LENGTH = 120

with open(output_file_path, 'w', encoding='utf-8') as out_file:
    out_file.write('<html><head><meta charset="utf-8"></head>')
    out_file.write('<body dir="ltr" style="font-family:\'Times New Roman\', Arial; font-size:12pt; line-height:2.0;">\n')
    
    with open(fr"{Path}\file.toc", 'r', encoding='utf-8') as file:
        content = file.read()
    
    for line in content.split('\n'):
        if "\\contentsline" in line:
            parts = line.split("}")
            if "section*" in line or "chapter*" in line:
                title = parts[1].replace("{","")
                title = title.replace("\u200c", chr(8204))
                page = parts[2].replace("{","")
            else:
                title = parts[2].replace("{","")
                title = title.replace("\u200c", chr(8204))
                page = parts[3].replace("{","")
    
            if "\\numberline" in line:
                line_parts = line.split('}{')
                line_number = line_parts[1]
                brace_start = line_number.find('{')
                brace_end = line_number.find('}', brace_start)
                number_sec = line_number[brace_start+1:brace_end]
                title = number_sec + " " + title
            
            #To change the font of the formula, we can ignore this line
            title = re.sub(r'(\$.*?\$)', r'<span style="font-style: italic; font-family:serif;">\1</span>', title)

            indent = ""
            if "chapter" in line or "section*" in line or "chapter*" in line:
                indent = ""
            elif "subsubsection" in line:
                indent = "      "
            elif "section" in line:
                indent = "  "
            
            title_with_indent = indent + title
            title_with_dots = title_with_indent.ljust(MAX_LENGTH, ".")
            
            table_f = f'<div style="font-family:monospace; white-space: pre-wrap; margin:0; text-align: left;">{title_with_dots} {page}</div>\n'
            
            out_file.write(table_f)

        out_file.write('</body></html>')
