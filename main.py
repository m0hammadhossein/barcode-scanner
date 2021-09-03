from pyzbar.pyzbar import decode
from PIL import Image
from argparse import ArgumentParser


def barcode_decode(path: str):
    try:
        res = decode(Image.open(path))
        if res:
            cn = len(res)
            txt = f'Found {cn} barcode:\n==================\n'
            for barcode in res:
                txt += f'Type : {barcode.type}\nResult : {barcode.data.decode("utf-8")}\n==================\n'
            return txt
        else:
            return 'Not found barcode'
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    parser = ArgumentParser(description='Barcode Decoder')
    parser.add_argument('-i', dest='image', help='path image', type=str, required=True)
    args = parser.parse_args()
    print(barcode_decode(args.image))
