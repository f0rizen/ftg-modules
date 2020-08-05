# Just calculator
# by @f0rizen

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
		allargs = ""
		if len(args[1])<=3:
			await message.edit("<strong>I can't count this math expression</strong>")
			return
		
		#Кто прочитал тот сдохнет ¯\_(ツ)_/¯
		for i in range(0, len(args[1])):
			allargs = allargs + str(args[i])
			
		try:
			result=eval(allargs)
		except NameError:
			await message.edit("<strong>I can't count this math expression</strong>")
			return
		
		try:
			await message.edit(f'<strong>{allargs}={int(result)}</strong>')
		except ValueError:
			await message.edit("<strong>I can't count this math expression</strong>")
			return
