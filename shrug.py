# ¯\_(ツ)_/¯

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

	async def shrug(self, message):
		"""This comand return: *message*, shrug"""
		await utils.answer(message, "¯\_(ツ)_/¯")
