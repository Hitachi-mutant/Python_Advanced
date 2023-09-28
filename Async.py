'''Асинхронний REST API запит:
Створіть програму, яка асинхронно взаємодіє з публічним REST API за допомогою aiohttp, 
отримуючи та оброблюючи дані з відповідей. (https://russianwarship.rip/api-documentation/v2)'''

# import aiohttp
# import asyncio

# async def main():

#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")

# asyncio.run(main())



# import requests

# def make_request1():
#     url = 'https://russianwarship.rip/2023-08-21'
#     result = requests.get(url)
#     print(result)

# def make_request2():
#     url = 'https://russianwarship.rip/2023-08-20'
#     result = requests.get(url)
#     print(result)

# def make_request3():
#     url = 'https://russianwarship.rip/2023-08-19'
#     result = requests.get(url)
#     print(result)

# if __name__ == '__main__':
#     make_request1()
#     make_request2()
#     make_request3()


import asyncio

async def function_1(a, b):
    print(a + b)
    await asyncio.sleep(1)

async def function_2(a, b):
    print(a * b)
    await asyncio.sleep(3)

async def main():
    # Create tasks for function_1 and function_2
    task1 = asyncio.create_task(function_1(1, 2))
    task2 = asyncio.create_task(function_2(1, 2))

    await asyncio.sleep(1)

    # Cancel both tasks
    task1.cancel()
    task2.cancel()

if __name__ == '__main__':
    asyncio.run(main())
