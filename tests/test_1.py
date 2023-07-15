import requests
from conftests import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from jsonschema import validate



def test_getting_post(recieved_=None):
    response = requests.get(url=SERVICE_URL)
    recieved_posts = response.json()

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(recieved_posts) == 3, GlobalErrorMessages.WRONG_ELEMENTS_COUNTS.value