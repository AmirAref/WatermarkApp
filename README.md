
# WatermarkApp
A console program to set the watermark on images and merge them


## how it works ?
This program has two parts that you can remove or add as needed
To run, you need to move the file to the folder where your photos are located
The program takes the extension of the photos from you so that it can find them
It also asks you for the watermark image address

#### Part One :
The program selects all the files in the desired folder with the format you entered and merges them in pairs. 2 to 1

#### Part Two :
It then transfers the new image to the add watermark function
In this section, the program asks you to enter the watermark transparency as well as its ratio to the original image numerically between 0 and 1.
It then saves the newly created images on which the watermark is installed in the Out folder and you can use it.
Note: Converting Names The program is defined so that the names of image files are numbered
Personalize for yourself if needed

### Attributes :
- Find all the images of the current folder, according to the selected format
- Combine both photos together and place a watermark on the new image
- Match the size of two photos to combine automatically
- Adjust the watermark transparency on the image
- Adjust the watermark to image ratio
- Automatic placement of the watermark in the middle of the image

### Install Requirement :
```
pip install -r requirements.txt
```

### Run :
```
python main.py
```

## Test Display :
[WaterMark App](https://user-images.githubusercontent.com/81515807/130963412-1cd31375-ffda-418e-ad76-580d353adafe.mp4)

<br></br>
**Author** : Amir Aref <br />
**Telegram** : [@Amir_720](https://t.me/Amir_720)<br />
**Github** : [@AmirAref](https://github.com/AmirAref)<br />
