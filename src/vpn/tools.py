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

        if i > 1:
            clients.append(data[i].split())

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

if __name__ == '__main__':
    text = '''::: Clients Summary :::
Client         Public key                                        Creation date
Motus          FwVG1oKSz/ncp0RoDqg9Stk0k3353jq/jHabMq5F83w=      04 Oct 2024, 15:45, UTC
Motus-Mac      uCMGVM/Za2Q0gR8vVPh4rj9OovTJGRWb+5taoul2GnA=      04 Oct 2024, 15:52, UTC
test           8GEmIPn889GTN7JUjqKPndJvzfjw1yWHUeswdxUsxw8=      05 Oct 2024, 16:47, UTC
test2          wlmx/WmVisypMsCSkULOMq0qjQGPXWGwkIYv51yhQD8=      05 Oct 2024, 16:47, UTC
user1          BaJUYPstbwWOKnI1TJzbPkOm3rMNF2UCxLcwi3vZajU=      05 Oct 2024, 16:47, UTC
user2          pwKjs9HB9mMrDusWYzz19PTjHOAmPlmf6aeFI3fw1UE=      05 Oct 2024, 16:47, UTC
::: Disabled clients :::
[disabled]   test 
[disabled]   test2 
'''
    print(parse_clients(text))