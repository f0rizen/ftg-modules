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
			await utils.answer(message, "You didn't specifyed args")
			return
		a = 0
		b = 0
		c = ''
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + str(args[i])
		i = 0
		while i < len(allargs) and allargs[i] >= '0' and allargs[i] <= '9':
			a = a * 10 + int(allargs[i]);
			i += 1
		if allargs[i] != '+' and allargs[i] != '-' and allargs[i] != '/' and allargs[i] != '*' and allargs[i] != '^':
			await utils.answer(message, "I can't count this math expression")
			return
		c = allargs[i]
		i += 1;
		while i < len(allargs) and allargs[i] >= '0' and allargs[i] <= '9':
			b = b * 10 + int(allargs[i]);
			i += 1
		if b == 0 and c == '/':
			await utils.answer(message, "I can't count this math expression")
			return
		# КТО ПРОЧИТАЛ ТОТ ЗДОХНЕТ
		ans = ""
		if c == '+':
			ans = str(a) + "+" + str(b) + "=" + str(a + b)
			await message.edit(ans)
			return
		if c == '-':
			ans = str(a) + "-" + str(b) + "=" + str(a - b)
			await message.edit(ans)
			return
		if c == '*':
			ans = str(a) + "*" + str(b) + "=" + str(a * b)
			await message.edit(ans)
			return
		if c == '/':
			ans = str(a) + "/" + str(b) + "=" + str(a // b)
			await message.edit(ans)
			return
		if c == '^':
			ans = str(a) + "^" + str(b) + "=" + str(a ** b)
