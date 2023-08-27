from flask import Flask, request, send_file
import base64
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def generate_api_card():
    image_url = request.args.get('url')  # Replace with the actual URL

    # Download the image content
    response = requests.get(image_url)
    image_content = response.content

    # Encode the image content in base64
    base64_image = base64.b64encode(image_content).decode("utf-8")

    data = [
        "data:image/png;base64," + base64_image,
        "version 2 (🔺 stylization, 🔻 robustness)",
    ]

    response = requests.post("http://127.0.0.1:7860/run/predict", json={"data": data}).json()

    response_data = response["data"]

    # Create an image card with the response
    image_card = create_image_card(response_data)

    # Save the image card as BytesIO for sending
    img_io = BytesIO()
    image_card.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the image card as a response
    return send_file(img_io, mimetype='image/png')

def create_image_card(response_data):
    image_card = Image.new('RGB', (800, 400), (255, 255, 255))
    draw = ImageDraw.Draw(image_card)

    # Load a font if needed
    font = ImageFont.load_default()

    y = 50
    for line in response_data:
        draw.text((50, y), line, font=font, fill=(0, 0, 0))
        y += 40

    return image_card

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
