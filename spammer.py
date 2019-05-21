import asyncio
from telethon import TelegramClient, sync, events

api_id = 876151
api_hash = '5b63f3c0ab2d11044b91da83de70e327'
phone_number = '+'
myId = 417840631

client = TelegramClient('botA', api_id, api_hash)

async def main():
  await client.connect()
  if not (await client.is_user_authorized()):
    await client.send_code_request(phone_number) #should i wrap with func and then await???
    await client.sign_in(phone_number, input('Please input your code:'))
  print('Telegram Client running')
  fict = await client.get_participants('fictonline')
  print(fict)
  await client.run_until_disconnected()
  asyncio.create_task
  # msgs = client.get_messages('Telegram')



loop = asyncio.get_event_loop()
loop.run_until_complete(main())
