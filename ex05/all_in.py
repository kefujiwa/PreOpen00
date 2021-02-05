# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 02:06:02 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 02:44:27 by kefujiwa         ###   ########.fr        #
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
	lst = sys.argv[1].split(',')
	for item in lst:
		item = item.lstrip().title()
		if not item:
			continue
		if item in states:
			print(f"{capital_cities[states[item]]} is the capital of {item}")
		else:
			for city_id, city_name in capital_cities.items():
				if city_name == item:
					for state_name, state_id in states.items():
						if state_id == city_id:
							print(f"{city_name} is the capital of {state_name}")
							sys.exit()
			print(f"{item} is neither a capital city nor a state")
