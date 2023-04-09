import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA5NDY2MjMzNjExNzIzMTY4OQ.Gh5Xss.Rc9OGczMCV7tGm52-9CFFSotJ4sZ-h5DxvW-bI'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    client.run(TOKEN)