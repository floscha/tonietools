import os
from typing import Optional

from tonietools.tonie_api import TonieAPI


def get_tonies_api():
    api = TonieAPI(os.environ["TONIE_MAIL"], os.environ["TONIE_PASSWORD"])
    api.households_update()
    api.households[os.environ["TONIE_HOUSEHOLD"]].creativetonies_update()
    return api


def upload(api, file_name, title, household_id: Optional[str] = None, tonie_id: Optional[str] = None):
    (
        api.households[household_id or os.environ["TONIE_HOUSEHOLD"]]
        .creativetonies[tonie_id or os.environ["TONIE_ID"]]
        .upload(file_name, title)
    )
