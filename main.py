#imports
from WaterMark import merge_images, Add_WaterMark
from glob import glob, iglob
from os import mkdir,path
import re
#----------------------------------------------------------------
def get_files(format):
    #data 
    data = []
    #image files
    for file in iglob(f"*.{format}"):
        data.append(file)
    #change data values
    new_data = list(zip(data[::2], data[1::2]))
    #out
    return new_data
#----------------------------------------------------------------
def create_new_name(name1, name2):
    #extract number from name 1
    num1 = re.search("\D*(\d+)\D*\.",name1).group(1)
    #extract number from name 2
    num2 = re.search("\D*(\d+)\D*\.",name2).group(1)
    #extract format from name 1
    format = re.search(".*\.(.+)",name1).group(1)
    #out
    new_name = f"{num1}-{num2}.{format}"
    return new_name
#----------------------------------------------------------------
def main():
    #get watermark file
    watermark = input("Enter the name of watermark file : ")
    #check exists watermark file:
    if not path.exists(watermark):
        print(f"\"{watermark}\" does not exists, try again !")
        main()
        return
    
    #get files format
    format = input("Enter files format (jpg,png,...) : ")
    format = format.replace(".","")

    # get opacity of watermark
    opacity = float(input("Enter the opacity of watermark (0-1) : "))
    if not (0 <= opacity <= 1):
        print(f"Invalid input (enter a number between 0 to 1), try again !")
        main()
        return
    opacity = int(opacity * 255) #0-255

    # get watermark ratio of image
    watermark_ratio = float(input("Enter watermark ratio of image (0-1) : "))  
    if not (0 <= watermark_ratio <= 1):
        print(f"Invalid input (enter a number between 0 to 1), try again !")
        main()
        return

    #create output folder
    output_filder = "Output"
    if not path.exists(output_filder):
        mkdir(output_filder)

    #get data
    data = get_files(format)
    for item in data:
        try:
            # merge images
            merge_image = merge_images(item[0], item[1])
            # add water mark to new image
            output_image = Add_WaterMark(merge_image, watermark, opacity,watermark_ratio=watermark_ratio)

            #save
            new_name = create_new_name(item[0], item[1])
            output_image.save(f"{output_filder}/"+new_name)
        except Exception as e:
            #continue
            print(e)


if __name__ == '__main__':
    main()
    input("Press Any key to quit !")
    #Programmer : https://github.com/AmirAref

