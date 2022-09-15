# Для телеграмм бота ввод в одну строку
from my_ui import write_line, in_txt
import re
from complex_num import complex_num
from integer import integer
from calc_fraction import calc_fraction
import math

# пример ввода комплексных (-5i)+(5+7i) => 5+2i;   (8-8i)*(-5+2i) => -40+16i
# пример ввода целых -5+9 => 4
# пример ввода рациональных -5/6*9/7 => -15/14
# пример объема  0.02*0.01*5 => 0.001 куб. м. или 1.0 литров
# пример перевода в двоичную cистему 254 => 11111110


def auto_in(a):
        a = re.sub('=|\s', '', a)
        a = re.sub('.', ',', a)
        comp_reg = re.fullmatch(r'\(([+-]?\d+|[+-]?\d+i|[+-]*\s*\d+\s*[+-]\s*\d+[i]|[+-]*\s*\d+[i]\s*[+-]\s*\d+)\)[+-/*]'
                                r'\(([+-]?\d+|[+-]?\d+i|[+-]*\s*\d+\s*[+-]\s*\d+[i]|[+-]*\s*\d+[i]\s*[+-]\s*\d+)\)', a)
        int_reg = re.fullmatch(r'[+-]?\d+[+-/*]\d+', a)
        rac_reg = re.fullmatch(r'[+-]?\d+/\d+[+-/*]\d+/\d+', a)
        vol_reg = re.fullmatch(r'[.\d]+\*[.\d]+\*[.\d]+', a)
        one_int = re.fullmatch(r'[+-][.\d]+[+-][.\d]', a)
        float_num = re.fullmatch(r'[+-]?\d/\./\d+/\d+[+-/*]\d+/\d+', a)
        if not comp_reg and not int_reg and not rac_reg and not vol_reg and not one_int and not float_num:
            return("Сам такое считай!")
        if comp_reg:
            comp = re.split(r'\)|\(', a)
            comp_first = comp[1]
            comp_two = comp[3]
            comp_act = comp[2]
            result = complex_num(comp_first, comp_two, comp_act)
            return("Это выражение комплексных чисел = " + result)
        if int_reg:
            num1 = re.split(r'([+-]?\d+)[\+\-\*/]\d+', a)[1]
            act = re.split(r'[+-]?\d+([\+\-\*/])\d+', a)[1]
            num2 = re.split(r'[+-]?\d+[\+\-\*/](\d+)', a)[1]
            result = integer(act, int(num1), int(num2))
            return("Это выражение целых чисел = " + str(result))
        if rac_reg:
            act = re.split(r'/\d+([\+\-\*/])\d+/', a)[1]
            num_spl = re.split(r'/|(\d)[\+\-\*](\d)', a)
            my_list = [x for x in num_spl if x]
            a, b, c, d = my_list
            result = calc_fraction(act, int(a), int(b), int(c), int(d))
            return("Это выражение рациональных чисел = " + str(result))
        if vol_reg:
            num1 = re.split(r'\*', a)
            result = float(num1[0]) * float(num1[1]) * float(num1[2])
            return("Это объем = " + str(result) + " куб. м. или " + str(result*1000)+ " литров")
        if one_int:
            result = (bin(int(a))).replace('0b', '')
            return("В двоичной системе = " + str(result))
        if float_num:
            num1 = re.split(r'\+', a)

        return

