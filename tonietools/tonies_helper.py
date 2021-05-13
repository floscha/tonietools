import os
from typing import List, Optional

from tonietools.tonie_api import TonieAPI


def get_tonies_api():
    api = TonieAPI(os.environ["TONIE_MAIL"], os.environ["TONIE_PASSWORD"])
    api.households_update()
    api.households[os.environ["TONIE_HOUSEHOLD"]].creativetonies_update()
    return api


def list_households() -> List[str]:
    api = TonieAPI(os.environ["TONIE_MAIL"], os.environ["TONIE_PASSWORD"])
    api.households_update()
    return list(api.households.keys())


def list_tonies(household_id: Optional[str] = None) -> List[str]:
    api = TonieAPI(os.environ["TONIE_MAIL"], os.environ["TONIE_PASSWORD"])
    api.households_update()
    api.households[os.environ["TONIE_HOUSEHOLD"]].creativetonies_update()
    return api.households[household_id or os.environ["TONIE_HOUSEHOLD"]]


def upload(
    api,
    file_name,
    title,
    household_id: Optional[str] = None,
    tonie_id: Optional[str] = None,
):
    (
        api.households[household_id or os.environ["TONIE_HOUSEHOLD"]]
        .creativetonies[tonie_id or os.environ["TONIE_ID"]]
        .upload(file_name, title)
    )
