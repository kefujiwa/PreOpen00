# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 00:12:52 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 21:18:45 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

filename = "numbers.txt"

try:
    with open(filename, "r", encoding="UTF-8") as file_object:
        content = file_object.read()
        print(content.replace(",", ""))
except OSError as e:
    print(e)
