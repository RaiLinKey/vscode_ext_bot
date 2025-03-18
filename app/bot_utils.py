import aiohttp
import aiofiles
import os
import shutil

from aiogram.types import BotCommand, BotCommandScopeDefault

from bot import bot


async def set_commands():
    commands = [BotCommand(command='start', description='В начало')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def download_file(url: str, chat_id: int, file_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            os.makedirs(f'./tmp/{chat_id}', exist_ok=True)
            async with aiofiles.open(f'./tmp/{chat_id}/{file_name}', 'wb') as file:
                await file.write(await response.read())


def remove_tmp(chat_id: str):
    try:
        shutil.rmtree(f"./tmp/{chat_id}")
    except FileNotFoundError:
        pass
