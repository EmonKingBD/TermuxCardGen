from PIL import Image, ImageDraw, ImageFont

def generate_nid(name, address, dob):
    img = Image.new("RGB", (700, 400), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw.text((50, 50), f"Name: {name}", fill="black", font=font)
    draw.text((50, 100), f"Address: {address}", fill="black", font=font)
    draw.text((50, 150), f"Date of Birth: {dob}", fill="black", font=font)
    draw.text((50, 200), f"NID: {random_nid()}", fill="black", font=font)

    path = f"/mnt/data/nid_{name}.png"
    img.save(path)
    return path

def random_nid():
    from random import randint
    return str(randint(1990000000000, 2000000000000))
