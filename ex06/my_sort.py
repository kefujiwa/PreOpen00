# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    my_sort.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kefujiwa <kefujiwa@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/06 02:48:17 by kefujiwa          #+#    #+#              #
#    Updated: 2021/02/06 03:20:28 by kefujiwa         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d = {
'Hendrix':'1942',
'Allman':'1946',
'King':'1925',
'Clapton':'1945',
'Johnson':'1911',
'Berry':'1926',
'Vaughan':'1954',
'Cooder':'1947',
'Page':'1944',
'Richards':'1943',
'Hammett':'1962',
'Cobain':'1967',
'Garcia':'1942',
'Beck':'1944',
'Santana':'1947',
'Ramone':'1948',
'White':'1975',
'Frusciante':'1970',
'Thompson':'1949',
'Burton':'1939',
}

d_sorted = sorted(d.items(), key=lambda x:(x[1], x[0]))
for name in dict(d_sorted).keys():
	print(name)
