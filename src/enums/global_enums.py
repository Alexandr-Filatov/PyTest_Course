from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Recieve status code is not equal to expected"
    WRONG_ELEMENTS_COUNTS = "Number of elements is not equal to expected"