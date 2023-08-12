# Signature Transparency Utility

A utility to extract signatures from images, make them transparent and overlay them with a color of choice.

## Features

- Upload your signature image.
- View the image and decide if cropping is required.
- Define custom cropping coordinates.
- Convert the cropped signature to a transparent PNG with a color overlay.
- Save the transparent signature as a PNG to retain transparency.

## Prerequisites

- Python
- OpenCV (`cv2`)
- NumPy (`numpy`)
- Matplotlib (`matplotlib`)
- PIL (`PIL`)

## Usage

1. Set the `image_path` variable to the path of your signature image.
2. Configure `threshold` and `color` based on your requirements:
   - `threshold`: Threshold value for binarization of the signature.
   - `color`: RGB value for the color overlay.
3. Run the script. The signature image will be displayed.
4. Decide if cropping is required and provide the cropping coordinates if needed.
5. The script will generate a transparent signature image named `extracted.png`.

## Customization

You can modify the `threshold` and `color` variables to suit your needs:

- `threshold`: Adjust this to capture varying levels of signature details. A higher threshold might miss out on finer details, whereas a lower threshold might include more noise.
- `color`: This sets the color overlay for the signature. It defaults to blue (`(255, 0, 0)`), but can be changed to any RGB value.

## Contributing

Contributions are welcome. Please fork the repository and submit pull requests for any enhancements or feature additions.

## License

This utility is open-source and available under the MIT License.
