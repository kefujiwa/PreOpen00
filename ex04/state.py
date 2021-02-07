# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 01:37:42 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/07 12:20:14 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}


def get_key_from_value(d, val):
	keys = [k for k, v in d.items() if v == val]
	if keys:
		return keys[0]


if len(sys.argv) == 2:
	ret = get_key_from_value(states, get_key_from_value(capital_cities, sys.argv[1]))
	if not ret:
		ret = "Unknown capital city"
	print(ret)
