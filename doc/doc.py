
yolofaces_doc = '''### Description
**Faces** component detects and anonymizes human faces from images basing on YOLO.

### Configuration

- **threshold** sets the minimum score to detect a face.
- **blur** allows to save the blurred results.
- **file_path** sets the directory where to save the blurred results.

### Input
The component accepts an image file in input.

### Output
The output is the list of bounding boxes associated with scores of the detected faces:

```
{
    "label": "face",
    "score": 0.9896213412284851,
    "bbox": [795,95,78,84]
}
```
If you've selected the **blur** parameter, you'll find the blurred images into the **file_path** folder. 

'''