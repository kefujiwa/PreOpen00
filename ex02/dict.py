# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dict.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 00:51:29 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 00:57:55 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

data = [['Caleb' , 24],
['Calixte' , 84],
['Calliste', 65],
['Calvin' , 12],
['Cameron' , 54],
['Camil' , 32],
['Camille' , 5],
['Can' , 52],
['Caner' , 56],
['Cantin' , 4],
['Carl' , 1],
['Carlito' , 23],
['Carlo' , 19],
['Carlos' , 26],
['Carter' , 54],
['Casey' , 2]]

di = {k: v for [v, k] in data}
for key, value in di.items():
	print(f"{key} : {value}")
