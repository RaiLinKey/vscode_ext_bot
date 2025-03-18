from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile

from bot_utils import download_file, remove_tmp


bot_router = Router()


VERSION = 'latest'
START_MSG = '''Бот для получения VSIX\\-файлов расширений для Visual Studio Code\\.

Бот принимает ссылки в формате:\n`https://marketplace\\.visualstudio\\.com/items?itemName=publisher\\.extension`

То есть достаточно найти интересующее расширение в [Marketplace](https://marketplace.visualstudio.com), скопировать ссылку из адресной строки браузера и отправить её боту\\.

Ограничения:
1\\. Ссылки стоит отправлять строго по одной\\. На каждую ссылку бот вернёт файл в формата VSIX\\.
2\\. Не поддерживаются наборы расширений \\(Extension Packs\\)\\.
3\\. Скачивается только последняя версия расширения\\.'''


@bot_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(START_MSG, parse_mode="MarkdownV2")
    

@bot_router.message(F.text)
async def cmd_download(message: Message):
    if message.text.startswith("https://marketplace.visualstudio.com/items?itemName="):
        bot_msg = await message.answer("Подождите, идёт загрузка файла...")
        ext_data = message.text[message.text.find('items?itemName=') + len('items?itemName='):] 
        publisher, ext_name = ext_data.split('.')

        download_link = f'https://{publisher}.gallery.vsassets.io/_apis/public/gallery/publisher/{publisher}/extension/{ext_name}/{VERSION}/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage'
        
        file_name = f'{publisher}.{ext_name}.vsix'
        await download_file(download_link, message.chat.id, file_name)
        
        await message.answer_document(FSInputFile(f'./tmp/{message.chat.id}/{file_name}', filename=file_name))
        await bot_msg.delete()
        remove_tmp(message.chat.id)
        


