def application(environ, start_response):
    
    string = environ['QUERY_STRING']
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    body = string.replace('&', '\n')
    
    start_response(status, headers )
    return [ body ]