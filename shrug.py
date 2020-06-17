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
			return
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + str(args[i]) + " "
		await utils.answer(message, allargs + "¯\_(ツ)_/¯")
		return

	async def shrugleftcmd(self, message):
		"""This command returns: *shrug* + *message*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "¯\_(ツ)_/¯")
			return
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + args[i] + " "
		if allargs[0] == " ":
			await utils.answer(message, "¯\_(ツ)_/¯" + allargs)
		else:
			await utils.answer(message, "¯\_(ツ)_/¯ " + allargs)

	async def shrugmancmd(self, message):
		"""This command returns: *message* + *man_shrugging emoji*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "🤷‍♂️")
			return
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + args[i] + " "
		await utils.answer(message, allargs + "🤷‍♂️")

	async def shrugwomancmd(self, message):
		"""This command returns: *message* + *woman_shrugging emoji*"""
		args = utils.get_args(message)
		if not args:
			await utils.answer(message, "🤷")
			return
		allargs = ""
		for i in range(0, len(args)):
			allargs = allargs + args[i] + " "
		await utils.answer(message, allargs + "🤷‍")