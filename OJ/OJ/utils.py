
def log_sql(sql):
    f = open('log.sql','a')
    f.write( '\n' +sql )
    f.close()