from tag import d

'''
    Работа с токенами
    поиск фраз
'''
def dialog():
    client = []
    operator = []
    for i in d:
        for j in i['messages']:
            if('text' in j):
                if(len(j['_id'])<=6):
                    client.append(j['text'])
                else:
                    operator.append(j['text'])
    return [client,operator]