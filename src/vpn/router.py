from fastapi import APIRouter, Depends, HTTPException

from subprocess import run, check_output

from authentication.tools import authenticate_user

from vpn.schemas import NewVPNConfig, VPNConfig, Clients
from vpn.tools import parse_clients

router = APIRouter(prefix='/api/vpn')


@router.post("/add")
async def add(new_config: NewVPNConfig, authorized: bool = Depends(authenticate_user)):
    if authorized:
        config_name = new_config.config_name

        config = 'config'
        res = run(['pivpn', 'add', '-n', config_name], encoding='utf-8')

        with open(f'/home/pivpn/configs/{config_name}.conf') as f:
            config = f.read()

        return {config_name: config}
    else:
        raise HTTPException(status_code=401)


# @router.get("/clients")
# async def clients(authorized: bool = Depends(authenticate_user)):
#     res = check_output(['pivpn', 'clients'], encoding='utf-8')
#     return res

@router.get("/clients")
async def clients(authorized: bool = Depends(authenticate_user)) -> Clients:
    if authorized:
        res = check_output(['pivpn', 'list'], encoding='utf-8')

        return Clients(**parse_clients(res))
    else:
        raise HTTPException(status_code=401)

@router.post("/on/{config_name}")
async def on(config_name: str, authorized: bool = Depends(authenticate_user)):
    if authorized:
        res = run(['pivpn', 'on', config_name, '-y'], encoding='utf-8')
        return res.stdout
    else:
        raise HTTPException(status_code=401)


@router.post("/off/{config_name}")
async def off(config_name: str, authorized: bool = Depends(authenticate_user)):
    if authorized:
        res = run(['pivpn', 'off', config_name, '-y'], encoding='utf-8')
        return res.stdout
    else:
        raise HTTPException(status_code=401)


@router.delete("/delete/{config_name}")
async def delete(config_name: str, authorized: bool = Depends(authenticate_user)):
    if authorized:
        res = run(['pivpn', 'remove', config_name, '-y'], encoding='utf-8')
        return res.stdout
    else:
        raise HTTPException(status_code=401)

