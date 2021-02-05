# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbers.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 00:12:52 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 00:40:25 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

filename = "numbers.txt"

with open(filename) as file_object:
	for line in file_object:
		if ',' in line:
			print(line[:-2])
		else:
			print(line)
