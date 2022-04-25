#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Uploading air pressure and temperature data from BMP390 with Raspberry Pi to Google spread sheet.

Usage:
Just uploading
./upload_gs.py JSON_KEYFILE SPREADSHEET_KEY WORKSHEET_NAME

Logging CSV file
./upload_gs.py JSON_KEYFILE SPREADSHEET_KEY WORKSHEET_NAME >> `date +%Y%m%d`.csv
"""

import sys
import datetime
import board
import adafruit_bmp3xx
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials


args = sys.argv

# Setup sensor
i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
bmp.pressure_oversampling = 32
bmp.temperature_oversampling = 32
bmp.filter_coefficient = 128

# Setup Google spread sheet
json_keyfile_name = args[1]
spreadsheet_key = args[2]
worksheet_name = args[3]

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_name, scope)
gc = gspread.authorize(credentials)
ws = gc.open_by_key(spreadsheet_key).worksheet(worksheet_name)

# Read a current time and sensor data
dt_now = datetime.datetime.now()
timestamp = dt_now.strftime("%Y-%m-%d %H:%M")
pressure = "{:.2f}".format(bmp.pressure)
temperature = "{:.2f}".format(bmp.temperature)

# Output readings
print(timestamp + "," + pressure + "," + temperature)
ws.append_row([timestamp, float(pressure), float(temperature)], value_input_option='USER_ENTERED')