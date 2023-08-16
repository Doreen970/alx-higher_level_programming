#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_all = 0
    total_weight = 0

    for score, weight in my_list:
        sum_all += score * weight
        total_weight += weight

    return sum_all / total_weight
