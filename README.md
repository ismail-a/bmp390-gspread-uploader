# bmp390-gspread-uploader
Uploading air pressure and temperature data from bmp390 with Raspberry Pi to Google spread sheet

## Installation
setupRPi.sh helps to initialize your Raspberry Pi to use I2C interface.
```
# setupRPi.sh
```

If you have already setup your Raspberry Pi and not need the above setup, you only have to install requirements.
```
$ pip3 install -r requirements.txt
```

Run.

- JSON_KEYFILE: On your Google Cloud Platform Console
- SPREADSHEET_KEY: Can be found in the URL of your Google spread sheet
```
$ ./upload_gs.py JSON_KEYFILE SPREADSHEET_KEY WORKSHEET_NAME
```

You may use crontab for logging into CSV and uploading to Google spread sheet every minute.
```
*/1 * * * * PATH_TO_SCRIPT/upload_gs.gy JSON_KEYFILE SPREADSHEET_KEY WORKSHEET_NAME >> PATH_TO_CSV/`date +\%Y\%m\%d`.csv
```