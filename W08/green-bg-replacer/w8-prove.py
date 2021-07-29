from PIL import Image

green_image = Image.open(input("Path to target image: "))
background_image = Image.open(input("Path to background image: "))

width, height = background_image.size

green_pixels = green_image.load()
background_pixels = background_image.load()

for x in range(width):
    for y in range(height):
        r, g, b = green_pixels[x, y]
        if r < 110 and g > 108 and b < 100:
            green_pixels[x, y] = background_pixels[x, y]


print("Done!")
print("What do you want to do next?")

action = ""

while action != "exit":
    action = input("\nshow\nsave\nexit\n>> ").lower()
    if (action == "show"):
        green_image.show()
    if (action == "save"):
        green_image.save(input("Save as: (*.jpg|*.png) ") or "unamed-image.jpg")
        print("Image successfully save. \n") 
