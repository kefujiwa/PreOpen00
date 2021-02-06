# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 13:00:01 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 17:57:21 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

fileTxt = "periodic_table.txt"
fileHtml = "periodic_table.html"
fileCss = "periodic_table.css"
d = {}

with open(fileTxt) as file_object:
	for line in file_object:
		line = line.split('=')
		tmp = line[1].split(',')
		d[line[0].strip()] = {}
		for item in tmp:
			item = item.split(':')
			d[line[0].strip()][item[0].strip()] = item[1].strip()

d_sorted = sorted(d.items(), key=lambda x:(int(x[1]['position']), int(x[1]['number'])))

with open(fileHtml, mode='w') as file_html:
	file_html.write("<!doctype html>\n<html lang=\"ja\">\n<head>\n<meta charset=\"UTF-8\">\n<title>The Periodic Table of the Elements</title>")
	file_html.write("<link href=\"periodic_table.css\" rel=\"stylesheet\" type=\"text/css\">\n</head>\n")
	file_html.write("<body>\n<h1 class=\"table_title\">The Periodic Table of the Elements</h1>\n")
	file_html.write("<table class=\"table\">\n")
	file_html.write("<tr>\n")
	for column in range(18):
		if column == 0:
			file_html.write(f"<td class=\"row row{column}\">\n")
		elif column == 1:
			file_html.write(f"<td class=\"row row{column} one-box purple\">")
		elif column > 1 and column <= 11:
			file_html.write(f"<td class=\"row row{column} three-box blue\">")
		elif column > 11 and column < 16:
			file_html.write(f"<td class=\"row row{column} one-box\">")
		elif column == 16:
			file_html.write(f"<td class=\"row row{column} one-box yellow\">")
		else:
			file_html.write(f"<td class=\"row row{column} orange\">\n")
		for cell in d_sorted:
			if int(cell[1]['position']) == column:
				file_html.write(f"<div class=\"cell cell{cell[1]['number']} {cell[0]}\">\n")
				file_html.write(f"<h4 class=\"cell_title\">{cell[0]}</h4>\n")
				file_html.write(f"<ul>\n")
				file_html.write(f"<li class=\"number\">No {cell[1]['number']}</li>\n")
				file_html.write(f"<li class=\"small\">{cell[1]['small']}</li>\n")
				file_html.write(f"<li class=\"molar\">{cell[1]['molar']}</li>\n")
				file_html.write(f"<li class=\"electron\">{cell[1]['electron']} electron</li>\n")
				file_html.write("</ul>\n")
				file_html.write("</div>\n")
		if column == 2:
			file_html.write("<div class=\"cell lan\">\n")
			file_html.write("<h4>Lanthanides</h4>")
			file_html.write("<ul>\n")
			file_html.write("<li>No 57 - 71</li>")
			file_html.write("</ul>\n")
			file_html.write("</div>\n")
			file_html.write("<div class=\"cell act\">\n")
			file_html.write("<h4>Actinides</h4>")
			file_html.write("<ul>\n")
			file_html.write("<li>No 89 - 103</li>")
			file_html.write("</ul>\n")
			file_html.write("</div>\n")
		file_html.write("</td>\n")
	file_html.write("</tr>\n")
	file_html.write("</table>\n")

with open(fileCss, mode='w') as file_css:
	file_css.write("@charset \"UTF-8\";")
	file_css.write("* {\n\tbox-sizing: border-box;\n}")
	file_css.write("body {\n\tfont-family: \"メイリオ\", Meiryo, Osaka, \"ＭＳ Ｐゴシック\", \"MS PGothic\", sans-serif;\n\tfont-size: 10px;\n\tcolor: #5b5b5b;\n\t}\n")
	file_css.write("body, h1, h4, ul, li {\n\tmargin: 0px;\n\tpadding: 0px;\n\tlist-style-type: none;\n\t}\n")
	file_css.write(".table_title {\n\tmargin: 20px auto;\n\ttext-align: center;\n}")
	file_css.write(".table {\n\tdisplay: flex;\n\twidth: 1440px;\n\tmargin: 0 auto;\n}")
	file_css.write(".one-box {\n\tpadding-top: 100px\n}")
	file_css.write(".three-box {\n\tpadding-top: 300px\n}")
	file_css.write(".cell {\n\theight: 100px;\n\twidth: 80px;\n\tborder: solid 1px #fff;\n\ttext-align: center;\n}")
	file_css.write(".purple .cell {\n\tbackground: linear-gradient(110deg, rgba(64, 64, 255, 0.2), rgba(64, 64, 255, 0.25));\n}")
	file_css.write(".blue .cell {\n\tbackground: linear-gradient(110deg, rgba(0, 128, 255, 0.2), rgba(0, 128, 255, 0.3));\n}")
	file_css.write(".orange .cell {\n\tbackground: linear-gradient(110deg, rgba(255, 152, 0, 0.2), rgba(255, 152, 0, 0.3));\n}")
	file_css.write(".yellow .cell, .cell1, .cell6, .cell7, .cell8, .cell15, .cell16, .cell34 {\n\tbackground: linear-gradient(110deg, rgba(255, 255, 0, 0.2), rgba(255, 255, 0, 0.3));\n}")
	file_css.write(".cell3, .cell11, .cell19, .cell37, .cell55, .cell87 {\n\tbackground: linear-gradient(110deg, rgba(255, 0, 0, 0.2), rgba(255, 0, 0, 0.25));\n}")
	file_css.write(".cell5, .cell14, .cell32, .cell33, .cell51, .cell52, .cell84 {\n\tbackground: linear-gradient(110deg, rgba(140, 190, 0, 0.2), rgba(140, 190, 0, 0.3));\n}")
	file_css.write(".cell13, .cell31, .cell49, .cell50, .cell81, .cell82, .cell83, .cell113, .cell114, .cell115, .cell116 {\n\tbackground: linear-gradient(110deg, rgba(0, 255, 0, 0.2), rgba(0, 255, 0, 0.3));\n}")
	file_css.write(".cell.lan, .cell.act {\n\tbackground: none;\n\tbackground-color: #fff\n}")
