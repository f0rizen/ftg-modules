# ¯\_(ツ)_/¯
# by @f0rizen

from .. import loader, utils

import logging
import asyncio

logger = logging.getLogger(__name__)

@loader.tds
class SHRUGMod(loader.Module):
	"""Just shrug module"""
	strings = {"name": "Shrug"}

	def __init__(self):
		self.name = self.strings["name"]

	def config_complete(self):
		pass

	async def shrugcmd(self, message):
		"""This command returns: *message* + *shrug*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "¯\_(ツ)_/¯")
		else:
			if str(args[0])[len(str(args[0])) - 1] == " ":
				await utils.answer(message, str(args[0]) + "¯\_(ツ)_/¯")
			else:
				await utils.answer(message, str(args[0]) + " ¯\_(ツ)_/¯")

	async def shrugleftcmd(self, message):
		"""This command returns: *shrug* + *message*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "¯\_(ツ)_/¯")
		else:
			if str(args[0])[0] == " ":
				await utils.answer(message, "¯\_(ツ)_/¯" + str(args[0]))
			else:
				await utils.answer(message, "¯\_(ツ)_/¯ " + str(args[0]))

	async def shrugmancmd(self, message):
		"""This command returns: *message* + *man_shrugging emoji*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "🤷‍♂️")
		else:
			if str(args[0])[len(str(args[0])) - 1] == " ":
				await utils.answer(message, str(args[0]) + "🤷‍♂️")
			else:
				await utils.answer(message, str(args[0]) + " 🤷‍♂️")

	async def shrugwomancmd(self, message):
		"""This command returns: *message* + *woman_shrugging emoji*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "🤷")
		else:
			if str(args[0])[len(str(args[0])) - 1] == " ":
				await utils.answer(message, str(args[0]) + "🤷‍")
			else:
				await utils.answer(message, str(args[0]) + " 🤷‍")