#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 18:36:45 2022

@author: arjunbhat
"""
# first program in python
# input two numbers, add them together, print them out
# use this file as a starter code to show you how to ask for input and print
#results

rods_str = input('Input rods: ')

rods_float = float(rods_str)
print('You input',rods_float,'rods.')

print()
print('Conversions')

meters_float = rods_float * 5.0292
print('Meters: ',round(meters_float,3))

feet_float = meters_float / 0.3048
print('Feet: ',round(feet_float,3))

miles_float = meters_float / 1609.34
print('Miles: ',round(miles_float,3))

furlongs_float = rods_float / 40
print('Furlongs: ',round(furlongs_float,3))

avg_walk_speed = (miles_float / 3.1) * 60
print('Minutes to walk',rods_float,'rods: ',round(avg_walk_speed,3))
