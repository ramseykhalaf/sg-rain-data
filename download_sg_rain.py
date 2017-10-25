import itertools
import os
import sys
import urllib.error
from datetime import timedelta, datetime
from urllib.request import urlretrieve

URL_TEMPLATE = "http://www.weather.gov.sg/files/rainarea/240km/dpsri_240km_{datetime_str}0000dBR.dpsri.png"
URL_DATE_FORMAT = "%Y%m%d%H%M"
FOLDER_DATE_FORMAT = "%Y-%m-%d"
TIME_RESOLUTION = timedelta(minutes=15)
NUM_ERRORS_IGNORE = 20


def download_sg_rain(dest_folder, limit=None, start_dt=datetime.now()):
    dt_gen = datetime_desc_gen(start_dt, TIME_RESOLUTION)
    num_failures = 0

    for dt in itertools.islice(dt_gen, limit):
        dt_url = datetime_to_url(dt)
        try:
            download_to_folder(dt_url, dt, dest_folder)
            num_failures = 0
        except urllib.error.HTTPError as e:
            if num_failures > NUM_ERRORS_IGNORE:
                raise e
            else:
                num_failures += 1


def datetime_desc_gen(start_dt, step_delta):
    start_dt = round_datetime(start_dt, step_delta)
    return (start_dt - step_delta*i for i in itertools.count())


def datetime_to_url(dt):
    datetime_str = dt.strftime(URL_DATE_FORMAT)
    return URL_TEMPLATE.format(datetime_str=datetime_str)


def download_to_folder(url, dt, base_folder):
    file_name = url.split('/')[-1]
    date_folder = dt.strftime(FOLDER_DATE_FORMAT)

    folder_path = os.path.join(base_folder, date_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(base_folder, date_folder, file_name)
    download(url, file_path)


def download(url, file_path):
    if not os.path.isfile(file_path):
        print('Downloading url ' + url)
        urlretrieve(url, file_path)
        print('Download Finished')
    else:
        print("Skipping - file path exists: " + file_path)


def round_datetime(dt, delta):
    round_to = delta.total_seconds()
    seconds = (dt - dt.min).seconds
    rounding = seconds // round_to * round_to
    return dt + timedelta(0, rounding - seconds, -dt.microsecond)


if __name__ == "__main__":
    download_sg_rain(sys.argv[1])
