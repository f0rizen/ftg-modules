# Just calculator
# by @f0rizen, @AtiksX

from .. import loader, utils

import logging
import asyncio
import telethon

logger = logging.getLogger(__name__)

async def register(cb):
	cb(CALCULATORMod())

@loader.tds
class CALCULATORMod(loader.Module):
	"""Just calculator module"""
	strings = {"name": "Calculator"}

	async def calculatecmd(self, message):
		"""This command can count a equality"""
		args = message.text.split(' ')
		if len(args)!=2:
			await utils.answer(message, "<strong>You didn't specifyed args</strong>")
			return
		argss=args[1].replace(' ','')
		if len(argss)<=2:
			await message.edit("<strong>I can't count this math expression(1)</strong>")
			return
		
		#Кто прочитал тот сдохнет ¯\_(ツ)_/¯		
		try:
			result=eval(argss)
		except:
			await message.edit("<strong>I can't count this math expression(2)</strong>")
			return
		
		if type(result)==int:
			await message.edit(f'<strong>{argss}={int(result)}</strong>')
			return
		if type(result)==float:
			await message.edit(f'<strong>{argss}={float(result)}</strong>')
			return
		else:
			await message.edit("<strong>I can't count this math expression(3)</strong>")
			return
		

