import datetime
from typing import List

from pydantic import BaseModel


class NewVPNConfig(BaseModel):
    config_name: str


class VPNConfig(NewVPNConfig):
    config: str


class DisabledClient(BaseModel):
    config_name: str

class Client(DisabledClient):
    config_name: str
    public_key: str
    creation_date: str

class Clients(BaseModel):
    clients: List[Client]
    disabled_clients: List[DisabledClient]
