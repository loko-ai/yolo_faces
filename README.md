<html><p><a href="https://loko-ai.com/" target="_blank" rel="noopener"> <img style="vertical-align: middle;" src="https://user-images.githubusercontent.com/30443495/196493267-c328669c-10af-4670-bbfa-e3029e7fb874.png" width="8%" align="left" /> </a></p>
<h1>YOLO Faces</h1><br></html>

**YOLO Faces** extension detects and anonymizes human faces from images.

The "Faces Detection" dashboard allows you to upload images and visualize the detected results:
<p align="center">
<img src="https://user-images.githubusercontent.com/30443495/223385026-3be3f789-099a-488a-9e51-13983b15563b.png" width="80%" />
</p>

Basing on <a href="https://github.com/sthanhng/yoloface">yoloface</a> model, it detects faces bounding boxes associated with scores.

You can use the **Faces** component directly into you flow:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/221590067-74a1ffed-d732-4990-a641-6ccf8cec67f4.png" width="80%" /></p>

In the block's configuration, you can set the minimum score **threshold** to detect a face and a folder where to save 
the anonymized images (you have to tick **blur** first):

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/221591157-b3091f7d-6464-40cf-9b06-c8f48feb6467.png" width="80%" /></p>


If you open your previous selected folder, you'll find the blurred images:

<p align="center"><img src="https://user-images.githubusercontent.com/30443495/223385686-5b477d3e-9b25-45fe-bcaf-6ba64b40b2dc.png" width="80%" /></p>

## Configuration

In the file *config.json* you can choose where to mount the volume containing the *yoloface* model:

```
{
  "main": {
    "volumes": [
       "/var/opt/loko/yolo_faces/.yoloface:/plugin/services/.yoloface"
       ],
    "gui": {
      "name": "Faces Detection"
    }
  }
}
```