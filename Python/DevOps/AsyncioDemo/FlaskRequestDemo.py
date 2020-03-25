import asyncio,requests,time

async def get(url):
    #request不是异步请求，无法并行，耗时和串行一致
    return requests.get(url)

async def request():
    url = 'http://127.0.0.1:5000'
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 请求 {url}')
    response = await get(url)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 得到响应 {response.text}')
    
start = time.time()    
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 结束任务，耗时{end - start} 秒')