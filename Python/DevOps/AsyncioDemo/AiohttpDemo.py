import asyncio
import aiohttp
import time

now = lambda: time.strftime("%Y-%m-%d %H:%m:%S")
async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = 'http://127.0.0.1:5000'
    print(f'{now()} 请求 {url}')
    result = await get(url)
    print(f'{now()} 得到响应 {result}')

start = time.time()    
tasks = [asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 结束任务，耗时{end - start} 秒')