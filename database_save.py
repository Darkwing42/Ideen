import json

def ask_for_database(username, password, database, host):
    global database_data
    datbase_data = {}
    database_data['limsdb'] = {'username': + username,
                                'passwd': + password,
                               'host': + host,
                               'database': + database}
s = json.dumps(database_data)
with open('/home/darkwing/database.json', '+w'):
    f.write(s)

def read_database_json():
    import json
    f = open('/home/darkwing/database.json', 'r')
    s = f.read()
    database = json.loads(s)
    username = database['limsdb']['username']
    password = database['limsdb']['password']
    host = database['limsdb']['host']
    database = database['limsdb']['database']
