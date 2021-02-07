# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 02:06:02 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/07 15:05:48 by kefujiwa         ###   ########.fr        #
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
    lst = sys.argv[1].split(',')
    for item in lst:
        item = item.lstrip()
        if not item:
            continue
        if item.title() in states:
            print(f"{capital_cities[states[item.title()]]} is the capital of {item.title()}")
        else:
            key = get_key_from_value(states, get_key_from_value(capital_cities, item.title()))
            if key:
                print(f"{item.title()} is the capital of {key}")
            else:
                print(f"{item} is neither a capital city nor a state")
