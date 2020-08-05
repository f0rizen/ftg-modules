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
		if len(args[1])<=2:
			await message.edit("<strong>I can't count this math expression(1)</strong>")
			return
		
		#Кто прочитал тот сдохнет ¯\_(ツ)_/¯		
		try:
			result=eval(args[1])
		except:
			await message.edit("<strong>I can't count this math expression(2)</strong>")
			return
		
		try:
			await message.edit(f'<strong>{args[1]}={int(result)}</strong>')
		except ValueError:
			await message.edit("<strong>I can't count this math expression(3)</strong>")
			return
		a = 0
		b = 0
		c = ''
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + str(args[i])

		# ГИГАНТ МЫСЛИ
		if allargs == 'True+True':
			ans = "True+True=2"
			await message.edit(ans)
			return
		if allargs == 'True-True':
			ans = "True-True=0"
			await message.edit(ans)
			return
		if allargs == 'True*True':
			ans = "True*True=1"
			await message.edit(ans)
			return
		if allargs == 'True/True':
			ans = "True/True=1"
			await message.edit(ans)
			return
		if allargs == 'True^True':
			ans = "True^True=1"
			await message.edit(ans)
			return

		if allargs == 'True+False':
			ans = "True+False=1"
			await message.edit(ans)
			return
		if allargs == 'True-False':
			ans = "True-False=1"
			await message.edit(ans)
			return
		if allargs == 'True*False':
			ans = "True*False=0"
			await message.edit(ans)
			return
		if allargs == 'True/False':
			ans = "I can't count this math expression"
			await message.edit(ans)
			return
		if allargs == 'True^False':
			ans = "True^False=1"
			await message.edit(ans)
			return

		if allargs == 'False+True':
			ans = "False+True=1"
			await message.edit(ans)
			return
		if allargs == 'False-True':
			ans = "False-True=-1"
			await message.edit(ans)
			return
		if allargs == 'False*True':
			ans = "False*True=0"
			await message.edit(ans)
			return
		if allargs == 'False/True':
			ans = "False/True=0"
			await message.edit(ans)
			return
		if allargs == 'False^True':
			ans = "False^True=0"
			await message.edit(ans)
			return

		if allargs == 'False+False':
			ans = "False+False=0"
			await message.edit(ans)
			return
		if allargs == 'False-False':
			ans = "False-False=0"
			await message.edit(ans)
			return
		if allargs == 'False*False':
			ans = "False*False=0"
			await message.edit(ans)
			return
		if allargs == 'False/False':
			ans = "I can't count this math expression"
			await message.edit(ans)
			return
		if allargs == 'False^False':
			ans = "I can't count this math expression"
			await message.edit(ans)
			return

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
			await message.edit(ans)
			return
