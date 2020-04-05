from tag import d,d2

def dialog():
    ans = ''
    for i in d:
        for j in i['messages']:
            if('text' in j):
                ans+=j['_id']+';'+j['text']+';\n'
    return ans