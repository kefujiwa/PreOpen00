# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/04 16:20:26 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/11 21:32:00 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

v_int = 42
v_str_n = "42"
v_str_s = "quarante-deux"
v_float = 42.0
v_bool = True
v_list = [42]
v_dict = {42: 42}
v_tuple = (42,)
v_set = set()
sep = "is type of"

def my_var():
    print(v_int, sep, type(v_int))
    print(v_str_n, sep, type(v_str_n))
    print(v_str_s, sep, type(v_str_s))
    print(v_float, sep, type(v_float))
    print(v_bool, sep, type(v_bool))
    print(v_list, sep, type(v_list))
    print(v_dict, sep, type(v_dict))
    print(v_tuple, sep, type(v_tuple))
    print(v_set, sep, type(v_set))

my_var()
