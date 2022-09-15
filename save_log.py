import datetime
now = datetime.datetime.now()

def save_logs(inp):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        f.write(str(now) + ' ' + inp + '\n')

