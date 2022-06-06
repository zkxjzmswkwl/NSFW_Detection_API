from config import MAX_IMAGE_SIZE
from random import randint
import aiohttp
import aiofiles
from PIL import Image

MAX_IMAGE_SIZE = MAX_IMAGE_SIZE * 1000000


async def download_image(url):
    file_name = f"{randint(6969, 6999)}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return False

            if int(resp.headers['Content-Length']) > MAX_IMAGE_SIZE:
                return False
            f = await aiofiles.open(file_name, mode='wb')
            await f.write(await resp.read())
            await f.close()
            img = Image.open(file_name)
            img.thumbnail((224, 224), Image.ANTIALIAS)
            img.save(file_name)

    return file_name
