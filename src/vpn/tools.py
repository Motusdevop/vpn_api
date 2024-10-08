from datetime import datetime

def parse_clients(text: str) -> dict:
    data = text.split('\n')

    flag = False

    clients = []
    disabled_clients = []

    result = {'clients': [], 'disabled_clients': []}

    for i in range(len(data)):

        if data[i].startswith(':::') and i != 0:
            break

        if flag:
            clients.append(data[i].split())

        if data[i].startswith('Client'):
            flag = True

    for line in data:
        if line.startswith('[disabled]'):
            disabled_clients.append(line.split()[1])

    for item in clients:
        date = datetime.strptime(' '.join(item[2:]), '%d %b %Y, %H:%M, %Z')

        client: dict = {
            'config_name': item[0],
            'public_key': item[1],
            'creation_date': date.strftime('%d.%m.%Y %H:%M') + ' UTC'
        }

        result['clients'].append(client)

    for item in disabled_clients:
        result['disabled_clients'].append({'config_name': item})

    return result