from fastapi import APIRouter

from subprocess import run, check_output

router = APIRouter(prefix='api/vpn')

@router.post("/add")
async def add():
    config_name = ''
    res = run(['pivpn', 'add', '-n', config_name], encoding='utf-8')
    return res.stdout

@router.get("/clients")
async def clients():
    res = check_output(['pivpn', 'clients'], encoding='utf-8')
    return res

@router.get("/clients_all")
async def clients_all():
    res = check_output(['pivpn', 'list'], encoding='utf-8')
    return res

@router.post("/on/{config_name}")
async def on(config_name: str):
    res = run(['pivpn', 'on', config_name, '-y'], encoding='utf-8')
    return res.stdout

@router.post("/off/{config_name}")
async def off(config_name: str):
    res = run(['pivpn', 'off', config_name, '-y'], encoding='utf-8')
    return res.stdout

@router.delete("/delete/{config_name}")
async def delete(config_name: str):
    res = run(['pivpn', 'remove', config_name, '-y'], encoding='utf-8')
    return res.stdout