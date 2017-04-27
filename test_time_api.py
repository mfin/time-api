import pytest
import time_api
from werkzeug.exceptions import NotFound

time = time_api.ReturnTime()

ljubljana = time.get('ljubljana')
ny = time.get('ny')

def test_ljubljana_place():
    assert ljubljana['place'] == 'Ljubljana, Slovenia'

def test_ljubljana_timezone():
    assert ljubljana['timezone'] == 'Europe/Ljubljana'

def test_new_york_place():
    assert ny['place'] == 'New York, NY, USA'

def test_new_york_timezone():
    assert ny['timezone'] == 'America/New_York'

def test_unknown_location():
    with pytest.raises(NotFound):
        time.get('asdfghj')
