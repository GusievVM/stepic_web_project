def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    indexes = [0, len(QUERY_STRING)]
    endSymbol = len(QUERY_STRING) - 1
    lengthQuery = len(QUERY_STRING)
    j = 1
    
    i = 0
    #for i in  range(len(QUERY_STRING)):
    while i < lengthQuery:
        if QUERY_STRING[i] == '&':
            if i != endSymbol:
                indexes.insert(j, i)
                j += 1
        i += 1

    body = [ QUERY_STRING[ 0:indexes[1] ] ]
    indexesLastUsed = len(indexes) - 1
    
    if len(indexes) > 2:
        k = 1
        while k < indexesLastUsed:
        #for k in (len(indexes) - 1):
            body.append( QUERY_STRING[ (indexes[k] + 1) : indexes[ (k+1) ]] )
            k += 1
    start_response(status, headers )
    return [ body ]