import os

from openai import OpenAI
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session

from mixins import SingletonMixin


class Context(SingletonMixin):

    def __init__(self, engine: sa.Engine):
        super().__init__()
        self._engine = engine
        # self._openai_client: OpenAI = OpenAI(
        #     # This is the default and can be omitted
        #     api_key=os.getenv("OPENAI_API_KEY"),
        # )

    @property
    def engine(self) -> sa.Engine:
        return self._engine

    @property
    def sessionmaker(self):
        return sessionmaker(self.engine)

    @property
    def openai_client(self) -> OpenAI:
        return self._openai_client

    def session(self) -> Session:
        return self.sessionmaker()
