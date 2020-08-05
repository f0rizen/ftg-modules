# by @f0rizen

from .. import loader, utils

import logging
import asyncio
import time

logger = logging.getLogger(__name__)

@loader.tds
class HACKMod(loader.Module):
	"""Hack your ass"""
	strings = {"name": "Hack"}
	def __init__(self):
		self.name = self.strings["name"]
	def config_complete(self):
		pass
	async def hackcmd(self, message):
		"""Hack your ass"""
		i = 0
		while i <= 99:
			await message.edit("<strong>Ass hacked for " + str(i) + "%</strong>")
			i += 1
			time.sleep(0.3)
		time.sleep(0.3)
		await message.edit("<strong>Ass successfully hacked</strong>")
		return

