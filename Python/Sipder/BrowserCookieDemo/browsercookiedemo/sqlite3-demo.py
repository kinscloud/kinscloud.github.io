import os
import sqlite3
import requests
from win32.win32crypt import CryptUnprotectData

def getcookiefromchrome(host='.qidian.com'):
    cookiepath=os.environ['LOCALAPPDATA']+r"\Google\Chrome\User Data\Default\Cookies"
    sql="select host_key,name,encrypted_value from cookies where host_key='%s'" % host
    with sqlite3.connect(cookiepath) as conn:
        cu=conn.cursor()        
        cookies={name:CryptUnprotectData(encrypted_value)[1].decode() for host_key,name,encrypted_value in cu.execute(sql).fetchall()}
        print(cookies)
        return cookies
    
def get_firfox_cookie_path():
    cookiepath_common = os.environ['APPDATA'] + r"\Mozilla\Firefox\Profiles"
    folds_arr = os.listdir(cookiepath_common)
    folds_end = [os.path.splitext(file)[-1][1:] for file in folds_arr]

    if 'default-release' in folds_end:
        cookie_fold_index = folds_end.index('default-release')
    else:
        cookie_fold_index = folds_end.index('default')
    cookie_fold = folds_arr[cookie_fold_index]
    cookie_path = os.path.join(cookiepath_common, cookie_fold)
    return os.path.join(cookie_path, 'cookies.sqlite')


def get_cookie_from_firfox(hosts_list=None):
    cookie_file = get_firfox_cookie_path()
    print(cookie_file)

    with sqlite3.connect(cookie_file) as conn:
        
        cur=conn.cursor()
        print(cur)
        # sql = "select sql from sqlite_master where type = 'table';"
        sql = "select baseDomain, name, value from moz_cookies"
        # sql = "pragma table_info('moz_cookies');"
        if hosts_list:
            sql_where = " where "
            for hosts in hosts_list:
                sql_where += " baseDomain = '{}' or ".format(hosts)
            sql_where = sql_where[: len(sql_where) - len(' or ')]
            sql += sql_where
        print(sql)
        cookie_arr = []
        for baseDomain, name, value in cur.execute(sql).fetchall():
            if name == 'miniDialog':
                continue
            cookie_arr.append('{}={}'.format(name, value))
            
        if cookie_arr:
            return '; '.join(cookie_arr)
        
print(get_cookie_from_firfox(['.baidu.com']))