from pydantic import BaseModel

class NewVPNConfig(BaseModel):
    config_name: str

class VPNConfig(NewVPNConfig):
    config: str

class Clients(BaseModel):
    clients_list: List[str]


