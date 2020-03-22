from PIL import Image, ImageDraw, ImageFont

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def getFactors(n):
    list = []
    c = 40
    x = 2
    for prime in filter(is_prime, range(2, 100)):
        y = 0
        while n % prime == 0:
            n /= prime
            y = y + 1

        if y > 0:
            list.append([x*c, y*c, x*c + c, y*c + c])
        x = x + 1

    return list


for x in range(2, 100):
    im = Image.new("RGB", (1024, 1024), "#FFFFFF")
    draw = ImageDraw.Draw(im)
    for array in getFactors(x):
        draw.rectangle(array, fill ="#ffff33", outline ="red")
    im.save("c:\\tmp\\pil\\"+str(x)+".png")
