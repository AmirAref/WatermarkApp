# libraries
from PIL import Image

#----------------------------------------------------------------

def merge_images(image1, image2, save=False):
    # image 1 and image 2 are string of paths

    # open image 1
    image1 = Image.open(image1)
    # open image 1
    image2 = Image.open(image2)

    # get size of images
    image1_size = image1.size
    image2_size = image2.size

    #optimazinf size of images
    if image1_size != image2_size :
        if image1_size > image2_size :
            image2 = image2.resize(image1_size)
        else:
            image1 = image1.resize(image2_size) 
    
    # get size of images
    image1_size = image1.size
    image2_size = image2.size

    # new image
    # width
    _width_new_image = image1_size[0] + image2_size[0]
    # height
    _height_new_image = image1_size[1] if image1_size[1] > image2_size[1] else image2_size[1]
    # create
    new_image = Image.new(
        "RGB", (_width_new_image, _height_new_image), (250, 250, 250))
    # paste image 1
    new_image.paste(image1, (0, 0))
    # paste image 2
    new_image.paste(image2, (image1_size[0], 0))
    # save output
    if save:
        new_image.save(save)
    #
    return new_image

#----------------------------------------------------------------

def Add_WaterMark(image : Image,watermark : str, opacity=255, save=False, watermark_ratio = 0.8):
    # image is a Image object
    # watermark is a string of path

    # open watermark
    watermark = Image.open(watermark)

    #size of watermark and image
    watermark_size = watermark.size
    image_size = image.size

    #set ratio watermark of image
    _new_w = int(watermark_ratio * image_size[0])
    _new_h = int(watermark_ratio * image_size[1])
    watermark = watermark.resize((_new_w, _new_h))

    #size of watermark and image
    watermark_size = watermark.size
    image_size = image.size

    #set watermark location
    loc = None
    #center
    _w = (image_size[0] - watermark_size[0]) // 2
    _h = (image_size[1] - watermark_size[1]) // 2
    loc = (_w, _h)

    # set opacity of watermark
    watermark.putalpha(opacity)

    # paste watermark
    image.paste(watermark, loc, watermark)

    # save output
    if save:
        image.save(save)
    #
    return image

#----------------------------------------------------------------
#Programmer : https://github.com/AmirAref
