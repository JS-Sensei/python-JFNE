def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', '')
    }
    print(conn_params)
    # We then connect to the db(commented out)
    # db.connect(**conn_params)

connect() # Will take the default parameters {'user': '', 'host': '127.0.0.1', 'pwd': '', 'port': 5432}
connect(host='127.0.0.42', port=5433) # {'user': '', 'host': '127.0.0.42', 'pwd': '', 'port': 5433}
connect(port=5431, user='fab', pwd='gandalf') # {'user': 'fab', 'host': '127.0.0.1', 'pwd': 'gandalf', 'port': 5431}