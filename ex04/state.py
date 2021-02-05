# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 01:37:42 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 01:59:15 by kefujiwa         ###   ########.fr        #
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

if len(sys.argv) == 2:
	for city_id, city_name in capital_cities.items():
		if city_name == sys.argv[1]:
			for state_name, state_id in states.items():
				if state_id == city_id:
					print(state_name)
					sys.exit()
	print("Unknown capital city")
