import paad
from paad.ext import commands
from ext.context import CustomContext
from ext.formatter import EmbedHelp
from collections import defaultdict
from ext import embedtobox
import asyncio
import aiohttp
import datetime
import psutil
import time
import json
import sys
import os
import re
import textwrap
from PIL import Image
import io

class paadbot(commands.Bot):
    '''
    Custom Client for paadu.py - Made by padoda
    '''
    _mentions_transforms = {
        '@everyone': '@\upaaddeveryone',
        '@here': '@\upaad2'
    }

    _mention_pattern = re.compile('|'.join(_mentions_transforms.keys()))

    def __init__(self, **attrs):
        super().__init__(command_prefix=self.get_pre, self_bot=True)
        self.formatter = EmbedHelp()
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.process = psutil.Process()
        self.prefix = None
        self._extensions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.last_message = None
        self.messages_sent = 0
        self.commands_used = defaultdict(int)
        self.remove_command('help')
        self.add_command(self.ping)
        self.load_extensions()
        self.add_command(self.load)
        self.add_command(self.reloadcog)
        self.load_community_extensions()
