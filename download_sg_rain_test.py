import itertools
import unittest.mock
from datetime import datetime, timedelta

import download_sg_rain


def test_url_gen():
    date = datetime(2017, 10, 30, 12, 30)
    url = download_sg_rain.datetime_to_url(date)
    assert url == "http://www.weather.gov.sg/files/rainarea/240km/dpsri_240km_2017103012300000dBR.dpsri.png"


def test_date_list():
    num_five_mins_in_one_day = 288  # 24*60/5
    start_dt = datetime(2017, 10, 30, 12, 31)

    dt_gen = download_sg_rain.datetime_desc_gen(start_dt, timedelta(minutes=5))

    dt_list = list(itertools.islice(dt_gen, num_five_mins_in_one_day+1))

    assert dt_list[0] == datetime(2017, 10, 30, 12, 30)
    assert dt_list[1] == datetime(2017, 10, 30, 12, 25)
    assert dt_list[-1] == datetime(2017, 10, 29, 12, 30)


def test_datetime_rounding():
    dt = datetime(2017, 10, 30, 12, 31, 25)

    round_dt = download_sg_rain.round_datetime(dt, timedelta(minutes=5))

    assert round_dt == datetime(2017, 10, 30, 12, 30, second=0)
    assert round_dt == download_sg_rain.round_datetime(round_dt, timedelta(minutes=5))


def test_download_sg_rain():
    with unittest.mock.patch("download_sg_rain.download") as mock_download:
        start_dt = datetime(2017, 10, 30, 12, 31, 59)
        limit = 2
        download_sg_rain.download_sg_rain("test_folder", limit, start_dt)

        file_name = "dpsri_240km_2017103012300000dBR.dpsri.png"
        expected = unittest.mock.call("http://www.weather.gov.sg/files/rainarea/240km/" + file_name,
                                      "test_folder/2017-10-30/" + file_name)

        assert mock_download.mock_calls[0] == expected
        assert len(mock_download.mock_calls) == limit

    




