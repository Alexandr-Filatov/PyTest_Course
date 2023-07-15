import requests
from conftests import SERVICE_URL

from src.baseclasses.response import Response
from src.schems.post import POST_SCHEMA



def test_getting_post(recieved_=None):
    r = requests.get(url=SERVICE_URL)
    response = Response(r)


    response.assert_status_code(200).validate(POST_SCHEMA)
