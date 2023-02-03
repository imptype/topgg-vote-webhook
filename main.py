import os
import aiohttp
from fastapi import FastAPI, Request, Response

app = FastAPI()

webhook = os.getenv('DISCORD_WEBHOOK_URL')
auth = os.getenv('TOPGG_AUTH_TOKEN')

@app.get('/')
async def root():
  return 'Hello World!'

@app.post('/vote')
async def vote(request : Request, response : Response):

  if request.headers.get('Authorization') != auth:
    response.status_code = 401 # Unauthorized
    return 401

  data = await request.json()
  text = '<@{}> upvoted <@{}>!'.format(data['user'], data['bot'])
  payload = {'content': text}
  
  async with aiohttp.ClientSession() as session:
    async with session.post(webhook, json = payload) as resp:
      # https://discord.com/developers/docs/resources/webhook#execute-webhook
      # returns 204 No Content if successful
      if resp.status == 204:
        response.status_code = 200
      else:
        response.status_code = resp.status
        
  return response.status_code
