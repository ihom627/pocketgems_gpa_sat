#!/usr/bin/env python

import pdb

DEBUG = 0

#find longest trend where sat increase but gpa decreases

def sat_gpa(sat_gpa_list):

    cur_sat = 0
    cur_gpa = 0 
    prev_sat = 0
    prev_gpa = 0 
    cur_start = 0
    cur_end = 0
    longest_start = 0
    longest_end = 0
    in_trend = 0
    longest_trend = 0
    current_trend = 0

    #iterate through list
    for i in range(0, len(sat_gpa_list)):
        if DEBUG == 1:
            print sat_gpa_list[i]
            print sat_gpa_list[i][0]    
            print sat_gpa_list[i][1]    

        cur_sat = sat_gpa_list[i][0]
        cur_gpa = sat_gpa_list[i][1]

        #first time through
        if i == 0:
            prev_sat = cur_sat;
            prev_gpa = cur_gpa;
            continue;

#    pdb.set_trace()

        #compare previous and current
        if cur_sat > prev_sat and cur_gpa < prev_gpa:
            if in_trend:
                cur_end = i
                current_trend += 1
            else:
                cur_start = i
                in_trend = 1
                current_trend = 1
            if DEBUG == 1:
                print "FOUND at index i = %d" % (i)

        #trend ending
        else:
            if in_trend:
                in_trend = 0
                prev_sat = cur_sat
                prev_gpa = cur_gpa
                if current_trend > longest_trend:
                    longest_trend = current_trend
                    longest_start = cur_start
                    longest_end = cur_end
            else:
                prev_sat = cur_sat
                prev_gpa = cur_gpa

    #check for a trend at the end of the list
    if in_trend == 1:
        if current_trend > longest_trend:
            longest_trend = current_trend
            longest_start = cur_start
            longest_end = cur_end

                
    if DEBUG == 1:
        print "longest_trend = %d, longest_start = %d, longest_end = %d" % (longest_trend, longest_start, longest_end)          
    return sat_gpa_list[longest_start:longest_end + 1]


################## TEST CASES #####################

# (sat, gpa)
# CASE where two trends, and the first in longer than the second 
L1 = [(1200, 3.0),(1210, 3.1),(1220, 3.3),(1300, 3.0),(1310, 2.5),(1320, 2.4),(1100, 2.3), (1110, 2.4), (1120, 2.3), (1130, 2.2), (1140, 2.4)]

# CASE where three trends, and the first in shorter than the second, but second same length 
# as the third, return the second
L2 = [(1200, 3.0),(1210, 3.1),(1220, 3.0),(1300, 3.1),(1310, 2.5),(1320, 2.4),(1100, 2.3), (1110, 2.4), (1120, 2.3), (1130, 2.2), (1140, 2.4)]

# CASE where two trends, and the second is longer than the first and terminates at the end 
L3 = [(1200, 3.0),(1210, 2.9),(1220, 2.8),(1300, 3.0),(1310, 2.5),(1320, 2.4),(1100, 2.3), (1110, 2.2), (1120, 2.1), (1130, 2.0), (1140, 1.9)]


print "this is test input list: ",  L1
monotonic_list = sat_gpa(L1)
print "this is longest monotonic trend: ", monotonic_list


print "this is test input list: ", L2
monotonic_list = sat_gpa(L2)
print "this is longest monotonic trend: ", monotonic_list


print "this is test input list: ", L3
monotonic_list = sat_gpa(L3)
print "this is longest monotonic trend: ", monotonic_list





