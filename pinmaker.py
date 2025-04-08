from PIL import Image, ImageDraw, ImageFont
import os

# Config
pin_image_path = "pin_small.png"
font_path = "Inter_18pt-SemiBold.ttf"
font_size = 12
font_color="white"
number_of_pins = 10
pin_name = "marker_greenborder"
# End config

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

# Load the pin image
try:
    pin_image = Image.open(pin_image_path).convert("RGBA")
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find the image at {pin_image_path}")

# Load the font
try:
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    front = ImageFont.load_default()
    print(f"Could not load the font at {font_path}, using default font instead")
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find the font at {font_path}")

# Generate the pin images
for i in range(1, number_of_pins + 1):
    # Create the output image
    img = pin_image.copy()
    draw = ImageDraw.Draw(img)
    text = str(i)

    # Calculate the position of the text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    image_width, image_height = img.size
    x = (image_width - text_width) / 2
    y = 4

    # Draw the text
    draw.text((x, y), text, font=font, fill=font_color)

    # Save the image
    output_filename = os.path.join(output_folder, f"{pin_name}{i}.png")
    img.save(output_filename)
    print(f"Saved {output_filename}")

print("Pin images generated successfully!")