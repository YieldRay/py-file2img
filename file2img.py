from math import sqrt
from PIL import Image


def crack(integer):
    """
    将整数分解为二元组
    """
    is_integer = lambda n:int(n) == n
    
    start = int(sqrt(integer))
    factor = integer / start
    while not is_integer(factor):
        start += 1
        factor = integer / start
    return int(factor), start
 

def file_to_bytes(file_path):
    """
    文件转换为字节数组
    """
    with open(file_path, 'rb') as file:
        bytes_obj = file.read()
    return bytes_obj


def bytes_to_image(binary):
    """
    字节数组转换为图片（Image实例）
    """
    length = len(binary)
    width,height = crack(length)
    img = Image.new("L", (width,height), color=0)
    i = 0 # index the bytes array
    for y in range(height):
        for x in range(width):
            color = binary[i]
            i+=1
            img.putpixel((x,y),color)
    return img

def bytes_to_image_file(binary,path):
    """
    字节数组保存为图像文件
    """
    img = bytes_to_image(binary)
    img.save(path)
    img.close()


def image_to_bytes(image_path):
    """
    图像文件转换为字节数组
    """
    image = Image.open(image_path).convert("L")
    # width, height = image.size
    pixels = list(image.getdata())
    binary = bytes(pixels)
    image.close()
    return binary

def encode_file_to_image(file_path, image_path):
    """
    编码任意文件到图像
    """
    binary = file_to_bytes(file_path)
    bytes_to_image_file(binary,image_path)


def decode_image_to_file(image_path,file_path):
    """
    图像还原为文件
    """
    binary = image_to_bytes(image_path)
    with open(file_path,"wb") as f:
        f.write(binary)



def cli():
    from sys import argv,stderr
    from os.path import basename

    eprint = lambda s:print(s,file=stderr)

    def show_help():
        name = basename(argv[0])
        eprint(f"Usage: ")
        eprint(f"./{name} encode <file_path> <image_path>")
        eprint(f"./{name} decode <image_path> <file_path>")
        exit(-1)

    def encode():
        try:
            encode_file_to_image(argv[2],argv[3])
        except FileNotFoundError as e:
            eprint(e)
            exit(e.errno)

    def decode():
        try:
            decode_image_to_file(argv[2],argv[3])
        except FileNotFoundError as e:
            eprint(e)
            exit(e.errno)

    if len(argv) <4:
        show_help()

    match argv[1]:
        case "encode":
            encode()
        case "decode":
            decode()
        case _:
            show_help()
    

if __name__ == "__main__":
    cli()