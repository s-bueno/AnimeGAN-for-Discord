import requests
from PIL import Image
import base64
from io import BytesIO

def pic2pic(x):
    
    # IP Address of the device hosting Gradio
    server_ip = 'YOUR.IP.ADDRESS'
    image_url = x

    response = requests.get(f'http://{server_ip}:5050/', params={'url': image_url})

    if response.status_code == 200:
        # Decode the base64-encoded image data
        response_data = response.content.decode('utf-8')
        image_data = base64.b64decode(response_data.split(",")[1])
    
        # Open the image using PIL
        image = Image.open(BytesIO(image_data))
    
        # Save the image locally
        image.save('generated_image.png')
    
        print("Image saved as 'generated_image.png'")
    else:
        print(f"Error: {response.status_code}")
