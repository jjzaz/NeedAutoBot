import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import urllib.request as urllib2
import datetime
import asyncio

bot = commands.Bot(command_prefix='.')


token = 'NDgxMDk3MjY0Njg5ODQwMTM5.Dr29Jg.SyaiWRRZRfbAv3pBpdLhiMLGmUM'

today = datetime.datetime.now()

months = {'January':1,
         'Febuary':2,
         'March':3,
         'April':4,
         'May':5,
         'June':6,
         'July':7,
         'August':8,
         'September':9,
         'October':10,
         'November':11,
         'December':12}
@bot.event
async def on_ready():
    print('Bot ready!')
async def run_news():

    await bot.wait_until_ready()
    source = urllib2.urlopen('https://www.crunchyroll.com/news')

    soup = BeautifulSoup(source, 'lxml')

    urls = []

    posted = []

    while not bot.is_closed:
        today_month = today.month
        today_day = str(today.day)
        today_year = today.year

        head = soup.find('li', class_='news-item').a['href']

        url_date = soup.find('div', class_='post-date').text

        month = url_date.split(' ')[16]

        url_month = months[month]
        date = url_date.split(' ')[17]

        if date.startswith('0'):
            url_date = date[1:2]
        else:
            url_date = date[:1]

        if head not in urls:
            urls.append(urls)
        else:
            pass

        if url_month == today_month:
            if url_date == today_day:
                if head not in posted:
                    await bot.send_message(bot.get_channel('507859422081712128'),'Crunchroll posted a news :: Link ::{} On {} {} {}.'.format(head, url_date, month, today_year))
                    posted.append(head)
                else:
                    pass
            else:
                pass
        asyncio.sleep(5)

@bot.command(pass_context=True)
async def clean(ctx, amount=99):
    channel = ctx.message.channel
    msgs = []
    if amount > 100:
        amount = 99
    mess = 0
    async for i in bot.logs_from(channel):
        mess += 1
    if amount > mess:
        amount = mess

    async for messagess in bot.logs_from(channel, limit=int(amount) + 1):
        msgs.append(messagess)
    await bot.delete_message()
    await bot.say('`{}` Messages deleted'.format(amount))







bot.loop.create_task(run_news())
bot.run(token)

