import os

from PIL import Image


def scale_and_copy_icon(icon_path, output_folder, icon_size):
    # Open the image
    image = Image.open(icon_path)

    # Scale the image without interpolation
    scaled_image = image.resize(icon_size, Image.NEAREST)

    # Create the target directory if it does not exist
    os.makedirs(output_folder, exist_ok=True)

    # Save the scaled image in the target directory
    output_path = os.path.join(output_folder, "ic_launcher.png")
    scaled_image.save(output_path)

    print(f"Icon saved in {output_folder}.")


# Source path to the original image
source_path = "assets/icon.png"

# Target folder for Android icons
android_output_folder = "android"

# Target folder for iOS icons
ios_output_folder = "ios"

# Target sizes for different density folders for Android
android_sizes = {
    "mipmap-mdpi": (48, 48),
    "mipmap-hdpi": (72, 72),
    "mipmap-xhdpi": (96, 96),
    "mipmap-xxhdpi": (144, 144),
    "mipmap-xxxhdpi": (192, 192),
}

# Target sizes for different iOS icon resolutions
ios_sizes = {
    "29x29": (29, 29),
    "40x40": (40, 40),
    "60x60": (60, 60),
    "76x76": (76, 76),
    "83.5x83.5": (83, 83),
    "120x120": (120, 120),
    "152x152": (152, 152),
    "167x167": (167, 167),
    "180x180": (180, 180),
}

# Scale and copy for Android
for density, size in android_sizes.items():
    scale_and_copy_icon(source_path, os.path.join(android_output_folder, density), size)

# Scale and copy for iOS
for name, size in ios_sizes.items():
    scale_and_copy_icon(source_path, os.path.join(ios_output_folder, f"{name}.png"), size)
