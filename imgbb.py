import requests
import base64
import json
import sys
from typing import Dict


class Imgbb:
    apikey = 'api key gir'
    uri = f'https://api.imgbb.com/1/upload?expiration=600&key={apikey}'

    @classmethod
    def upload(cmd, img_file) -> Dict[str, str]:
        with open(img_file, "rb") as f:
            image = f.read()
            r = requests.post(Imgbb.uri, data={
                'image': base64.b64encode(image)})

        image_url = json.loads(r.content)
        r = image_url['data']['url']

        return r


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f'Kullanım: {sys.argv[0]} resim.jpg')
        sys.exit(-1)

    imguri = Imgbb.upload(sys.argv[1])
    print(imguri)
