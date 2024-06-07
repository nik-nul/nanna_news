# template_lib.py BEGIN
headp = """% HEAD BEGIN
\\documentclass[letterpaper, 12pt]@@@@article^^^^
\\usepackage@@@@graphicx^^^^
\\usepackage@@@@multicol^^^^
\\usepackage@@@@anysize^^^^
\\usepackage@@@@fontspec^^^^
\\usepackage[fontset=none]@@@@ctex^^^^
\\usepackage@@@@tabularx^^^^
\\usepackage[breaklinks=true, colorlinks=true]@@@@hyperref^^^^
\\setlength\\columnsep@@@@30pt^^^^
\\marginsize@@@@30pt^^^^@@@@30pt^^^^@@@@10pt^^^^@@@@20pt^^^^
\\setmainfont[]@@@@TeX Gyre Bonum^^^^
\\setCJKmainfont[BoldFont=Noto Serif CJK SC Bold, ItalicFont=FandolKai]@@@@Noto Sans CJK SC^^^^
\\setlength@@@@\\parindent^^^^@@@@0cm^^^^
\\begin@@@@document^^^^
\\begin@@@@center^^^^
    \\Huge\\textbf@@@@南哪大专历史学院醒前消息^^^^
\\end@@@@center^^^^
\\vspace@@@@4mm^^^^
\\hrule
\\renewcommand\\tabularxcolumn[1]@@@@m@@@@#1^^^^^^^^
\\begin@@@@tabularx^^^^@@@@\\textwidth^^^^@@@@>@@@@\\hsize.2\\hsize^^^^X>@@@@\\hsize.6\\hsize^^^^X>@@@@\\hsize.2\\hsize^^^^X^^^^
    \\begin@@@@flushleft^^^^
        {date}\\, No.{no}
    \\end@@@@flushleft^^^^
    &
    \\begin@@@@center^^^^
        \\textit@@@@“{saying}”^^^^
    \\end@@@@center^^^^
    &
    \\begin@@@@flushright^^^^
        \\textbf@@@@南京市鼓楼区^^^^
    \\end@@@@flushright^^^^
\\end@@@@tabularx^^^^
\\vspace@@@@-3.5mm^^^^
\\hrule
\\vspace@@@@4mm^^^^
% HEAD END
""" # date, no, saying; @@@@ -> {, ^^^^ -> }

partbp = """\centerline@@@@\huge\\textbf@@@@{part_name}^^^^^^^^
\\begin@@@@multicols^^^^@@@@2^^^^
""" # part_name; @@@@ -> {, ^^^^ -> }

partmp = """\\section@@@@{sec_name}^^^^
{sec_cont}
""" # \url{} in sec_cont -> \\sloppy\\url@@@@^^^^ ;sec_name, sec_cont; @@@@ -> {, ^^^^ -> }

parte = """\\end{multicols} 
\\hrule
\\vspace{4mm}
"""

appb = """% APPENDIX BEGIN
\\centerline{\\huge\\textbf{附录}}
\\begin{figure}[htbp]
    \\centering
"""

appm = """    \\begin@@@@minipage^^^^[b]@@@@0.32\\textwidth^^^^
        \\centering
        \\includegraphics[width=0.5\\textwidth]@@@@{with_ext}^^^^
        \\caption@@@@{no_ext}^^^^
    \\end@@@@minipage^^^^
""" # swith_ext, no_ext; @@@@ -> {, ^^^^ -> }

appe = """\end{figure}
\end{document}"""
# template_lib.py END
