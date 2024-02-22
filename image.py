from PIL import Image

def convert_png_to_webp(png_path, webp_path):
    # Open PNG image
    png_image = Image.open(png_path)
    
    # Convert to WebP format and save
    png_image.save(webp_path, 'WEBP')

# Example usage
convert_png_to_webp("/home/insabhi/Downloads/202204181053.png", "/home/insabhi/Downloads/output.webp")
