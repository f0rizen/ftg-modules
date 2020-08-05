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
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "<strong>You didn't specifyed args</strong>")
			return
		allargs = ""
		#Кто прочитал тот сдохнет ¯\_(ツ)_/¯
		for i in range(0, len(args)):
			allargs = allargs + str(args[i])
		result=eval(allargs)
		try:
			await message.edit(f'{allargs}={int(result)}')
		except ValueError:
			await message.edit("<strong>I can't count this math expression</strong>")
