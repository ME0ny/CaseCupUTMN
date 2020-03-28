from tag import d

def dialog():
    ans = {}
    for i in d:
        for j in i['messages']:
            if('text' in j):
                ans[j['_id']]=j['text']
    return ans