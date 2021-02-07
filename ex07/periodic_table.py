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


def convert_txt_to_dict():
    try:
        f = open("periodic_table.txt", "r", encoding="UTF-8")
    except OSError as e:
        print(e)
        return None
    else:
        d = {}
        for line in f:
            line = line.split("=")
            d[line[0].strip()] = {}
            tmp = line[1].split(",")
            for item in tmp:
                item = item.split(":")
                d[line[0].strip()][item[0].strip()] = item[1].strip()
        f.close()
        return d


def write_html(f):
    title = "Periodic Table of the Elements"
    elms = convert_txt_to_dict()
    f.write('<!DOCTYPE html>\n')
    f.write('<html lang="en">\n')
    f.write('<head>\n')
    f.write('<meta charset="UTF-8"\n')
    f.write('meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>' + title + '</title>\n')
    f.write('<link rel="stylesheet" href="periodic_table.css">\n')
    f.write('</head>\n')
    f.write('\n')
    f.write('<body class="container">\n')
    f.write('<h1 class="title">' + title + '</h1>\n')
    f.write('<section class="table-container">\n')
    f.write('<table>\n')
    i = 1
    for row in range(7):
        f.write('<tr>\n')
        for col in range(18):
            if (row == 0 and 1 <= col and col <= 16) or ((row == 1 or row == 2) and 2 <= col and col <= 11):
                f.write('<td class="empty">\n')
            elif (row == 5 or row == 6) and col == 2:
                i += 15
                name = "Lanthanides" if row == 5 else "Actinides"
                number = "57 - 71" if row == 5 else "89 - 103"
                f.write('<td class="cell">\n')
                f.write('<h4 class="name">' + name + '</h4>\n')
                f.write('<ul>\n')
                f.write('<li class="number">No.<span class="number-fontsize">' + number + '</span></li>\n')
                f.write('</ul>\n')
            else:
                for elem in elms:
                    num = int(elms[elem]["number"])
                    color = ""
                    if num == i:
                        if i == 1 or (6 <= i <= 9) or (15 <= i <= 17) or (34 <= i <= 35) or elms[elem]["position"] == "16":
                            color = "yellow"
                        elif elms[elem]["position"] == "0":
                            color = "red"
                        elif elms[elem]["position"] == "1":
                            color = "purple"
                        elif 2 <= int(elms[elem]["position"]) <= 11:
                            color = "blue"
                        elif i == 5 or i == 14 or 32 <= i <= 33 or 51 <= i <= 52 or i == 84:
                            color = "moss"
                        elif 12 <= int(elms[elem]["position"]) <= 15:
                            color = "green"
                        elif elms[elem]["position"] == "17":
                            color = "orange"
                        f.write('<td id="' + str(i) + '" class="cell ' + color + '">\n')
                        f.write('<h4 class="name">' + elem + '</h4>\n')
                        f.write('<ul>\n')
                        f.write('<li class="number">No.<span class="number-fontsize">' + elms[elem]["number"] + '</span></li>\n')
                        f.write('<li class="symbol">' + elms[elem]["small"] + '</li>\n')
                        f.write('<li class="molar">' + elms[elem]["molar"] + '</li>\n')
                        f.write('<li class="electron">' + elms[elem]["electron"] + ' electron</li>\n')
                        f.write('</ul>\n')
                i += 1
            f.write('</td>\n')
        f.write('</tr>\n')
    f.write('</table>\n')
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>\n')


def write_css(f):
    f.write('@charset "UTF-8";\n')
    f.write('* {')
    f.write('box-sizing: border-box;')
    f.write('}\n')
    f.write('body {')
    f.write('font-family: BlinkMacSystemFont, -apple-system, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "D    roid Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;')
    f.write(' font-size: 10px;')
    f.write('}\n')
    f.write('body, h1, h4, ul, li {')
    f.write('margin: 0; padding: 0; list-style-type: none;')
    f.write('}\n')
    f.write('.title {')
    f.write('font-family: "Hiragino Kaku Gothic ProN", "Hiragino Sans", Meiryo, sans-serif; margin: 20px auto; text-align:     center;')
    f.write('}\n')
    f.write('table {')
    f.write('display: flex; width: 1440px; margin: 0 auto;')
    f.write('}\n')
    f.write('.cell {')
    f.write('height: 100px; width: 80px; border: solid 1px #a0a0a0; text-align: center; vertical-align: top;')
    f.write('}\n')
    f.write('li {')
    f.write('padding-top: 2px;')
    f.write('}\n')
    f.write('.name {')
    f.write('border-bottom: dashed 0.2px #666; padding: 3px 0;')
    f.write('}\n')
    f.write('.number-fontsize {')
    f.write('font-size: 1.2em;')
    f.write('}\n')
    f.write('.symbol {')
    f.write('font-size: 3em; padding: 0;')
    f.write('}\n')
    f.write('.yellow {')
    f.write('background: linear-gradient(110deg, rgba(255, 255, 0, 0.2), rgba(255, 255, 0, 0.3));')
    f.write('}\n')
    f.write('.red {')
    f.write('background: linear-gradient(110deg, rgba(255, 0, 0, 0.2), rgba(255, 0, 0, 0.3));')
    f.write('}\n')
    f.write('.purple {')
    f.write('background: linear-gradient(110deg, rgba(64, 64, 255, 0.2), rgba(64, 64, 255, 0.3));')
    f.write('}\n')
    f.write('.blue {')
    f.write('background: linear-gradient(110deg, rgba(0, 128, 255, 0.2), rgba(0, 128, 255, 0.3));')
    f.write('}\n')
    f.write('.moss {')
    f.write('background: linear-gradient(110deg, rgba(140, 190, 0, 0.2), rgba(140, 190, 0, 0.3));')
    f.write('}\n')
    f.write('.green {')
    f.write('background: linear-gradient(110deg, rgba(0, 255, 0, 0.2), rgba(0, 255, 0, 0.3));')
    f.write('}\n')
    f.write('.orange {')
    f.write('background: linear-gradient(110deg, rgba(255, 152, 0, 0.2), rgba(255, 152, 0, 0.3));')
    f.write('}\n')


make_file("periodic_table.html", write_html)
make_file("periodic_table.css", write_css)
