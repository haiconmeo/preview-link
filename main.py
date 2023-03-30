from io import BytesIO
from linkpreview import link_preview
import requests as ulreq
from PIL import Image
from fastapi import FastAPI

app = FastAPI()
def getsizes(uri):
    file = ulreq.get(uri)
    stream = BytesIO(file.content)

    image = Image.open(stream).convert("RGBA")
    stream.close()
    return image.size

def get_preview_link(link):
    preview = link_preview(link)
    width = preview.width
    height = preview.height
    if ((preview.width and preview.height) or preview.image ):

        width,height =getsizes(preview.image)

    return {
        'title': preview.title,
        'description': preview.description,
        'image': preview.image,
        'force_title': preview.force_title,
        'absolute_image': preview.absolute_image,
        'site_name':preview.site_name,
        'width': width,
        'height': height
    }

@app.get("/")
async def read_item(url: str):
    return get_preview_link(url)