import asyncio,time

async def task():
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} task 开始')
    await asyncio.sleep(2)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} task 结束')
    
loop = asyncio.get_event_loop()
tasks = [task() for _ in range(5)]
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 结束调用协程任务，耗时{end - start} 秒')