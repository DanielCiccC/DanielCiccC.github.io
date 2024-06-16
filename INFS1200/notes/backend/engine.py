import os
from typing import Final

import sqlalchemy as sa

USER_NAME: Final[str] = "root"
HOST: Final[str] = "localhost"
PORT: Final[int] = 13306
PASSWORD: Final[str] = "Password"
DATABASE: Final[str] = "MechAssistTransaction"
ENGINE_URL: sa.URL = sa.URL.create(
    "mysql+mysqlconnector",
    username=USER_NAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DATABASE,
)

engine = sa.create_engine(ENGINE_URL, echo=True)
