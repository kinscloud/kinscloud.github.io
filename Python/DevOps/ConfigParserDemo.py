import configparser

config = configparser.ConfigParser()

config.read(r'C:\Users\Administrator\AppData\Roaming\pip\pip.ini')

print('遍历配置信息：')

for section in config.sections():
    print(f'section is [{section}]')
    for key in config[section]:
        print(f'key is [{key}],value is [{config[section][key]}]')
        
print('通过键获取相应的值：')
print(f'index-url is [{config["global"]["index-url"]}]')
print(f'trusted-host is [{config["global"]["trusted-host"]}]')

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression':'yes',
    'CompressionLevel':'9',
}
config['kinscloud.org']={}
config['kinscloud.org']['User']='kin'
config['kins.cloud']={}
topsecret = config['kins.cloud']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] ='no'
config['DEFAULT']['ForwardX11'] ='yes'
with open('example.ini','w') as configfile:
    config.write(configfile)
    
with open('example.ini','r') as f:
    print(f.read())