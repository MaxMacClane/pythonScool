# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join
from district.central_street.house1 import room1 as cen_h1r1
from district.central_street.house1 import room2 as cen_h1r2
from district.central_street.house2 import room1 as cen_h2r1
from district.central_street.house2 import room2 as cen_h2r2

from district.soviet_street.house1 import room1 as sov_h1r1
from district.soviet_street.house1 import room2 as sov_h1r2
from district.soviet_street.house2 import room1 as sov_h2r1
from district.soviet_street.house2 import room2 as sov_h2r2

cen_str_h1_r1 = ', '.join(cen_h1r1.folks) + ','
cen_str_h1_r2 = ', '.join(cen_h1r2.folks) + ','
cen_str_h2_r1 = ', '.join(cen_h2r1.folks)
cen_str_h2_r2 = ', '.join(cen_h2r2.folks) + ','

sov_str_h1r1 = ', '.join(sov_h1r1.folks) + ', '
sov_str_h1r2 = ', '.join(sov_h1r2.folks) + ', '
sov_str_h2r1 = ', '.join(sov_h2r1.folks) + ', '
sov_str_h2r2 = ', '.join(sov_h2r2.folks) + '. '

print('In the aria live: ', cen_str_h1_r1, cen_str_h1_r2, cen_str_h2_r1, cen_str_h2_r2,
      sov_str_h2r1, sov_str_h1r2, sov_str_h2r1, sov_str_h2r2)

print('test')