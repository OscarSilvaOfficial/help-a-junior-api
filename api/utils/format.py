def server_log(addr, port):
    addr = 'localhost' if addr == '0.0.0.0' else addr
    print(f'Server running at | http://{addr}:{port}/')