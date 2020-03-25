import asyncio,time

async def _task():
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} task 开始')
    time.sleep(2)
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} task 结束')
    return "运行结束"
    
def callback(task):
    print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 回调函数开始运行')
    print(f'状态：{task.result()}')
    
coroutine = _task()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 产生协程对象 {coroutine}, 函数并未被调用')
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop = asyncio.get_event_loop()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 开始调用协程任务')
start = time.time()
loop.run_until_complete(task)
end = time.time()
print(f'{time.strftime("%Y-%m-%d %H:%m:%S")} 结束调用协程任务，耗时{end - start} 秒')