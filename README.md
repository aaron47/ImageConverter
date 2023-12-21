# idk got bored and wrote this script

- This script has 3 arguments 2 of which are optional:
  - --img_path: Path to your image
  - --new_ext: Your new desired extension, if not provided, the script assumes you're trying to convert from a JPG to a PNG
  - --delete_original: Whether to delete your original image, False by default

## Example Usage

### This first example shows usage without --delete-original or --new_ext, which will just convert this image to a PNG, while keeping the original

```bash
python .\ImageConverter.py --img_path="artworks-WHji2Yq7uowhxaS7-EnBh3w-t500x500.jpg"
```

### This second example shows usage with --delete-original and --new_ext, which will just convert this image to a back to JPG, and delete the original which is a PNG in this case

```bash
python .\ImageConverter.py --img_path="artworks-WHji2Yq7uowhxaS7-EnBh3w-t500x500.png" --new_ext=jpg --delete-original
```

### Final example converting a JPG to a PNG and deleting the original

```bash
python .\ImageConverter.py --img_path="artworks-WHji2Yq7uowhxaS7-EnBh3w-t500x500.jpg" --delete-original
```
