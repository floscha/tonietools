import os
from typing import List, Optional, Union

import eyed3
from tonie_api import TonieAPI


class Tonies:
    def __init__(
        self,
        mail: Optional[str] = None,
        password: Optional[str] = None,
    ) -> None:
        self.api = TonieAPI(
            mail or os.environ["TONIE_MAIL"], password or os.environ["TONIE_PASSWORD"]
        )

    @staticmethod
    def list_households(
        mail: Optional[str] = None, password: Optional[str] = None
    ) -> List[str]:
        api = TonieAPI(
            mail or os.environ["TONIE_MAIL"], password or os.environ["TONIE_PASSWORD"]
        )
        api.households_update()
        return list(api.households.keys())

    def list_tonies(self, household_id: Optional[str] = None) -> List[str]:
        self.api.households_update()
        self.api.households[
            household_id or os.environ["TONIE_HOUSEHOLD"]
        ].creativetonies_update()
        return self.api.households[household_id or os.environ["TONIE_HOUSEHOLD"]]

    def upload(
        self,
        file_names: Union[str, List[str]],
        household_id: Optional[str] = None,
        tonie_id: Optional[str] = None,
    ):
        self.api.households_update()
        self.api.households[
            household_id or os.environ["TONIE_HOUSEHOLD"]
        ].creativetonies_update()

        for file_name in file_names:
            title = eyed3.load(file_name).tag.title
            (
                self.api.households[household_id or os.environ["TONIE_HOUSEHOLD"]]
                .creativetonies[tonie_id or os.environ["TONIE_ID"]]
                .upload(file_name, title)
            )
