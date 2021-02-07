# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 13:00:01 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/07 14:43:07 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def make_file(filename, func):
    try:
        f = open(filename, "w", encoding="UTF-8")
    except OSError as e:
        print(e)
    else:
        func(f)
        f.close()


d_sorted = sorted(d.items(), key=lambda x:(int(x[1]['position']), int(x[1]['number'])))


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
