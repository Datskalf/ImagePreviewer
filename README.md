# ImagePreviewer
A python script that will scan a folder for images periodically, and show the most recent one in a number of pyplots.  
The script uses only default python libraries, and is written for Python3.


### Parameters
> ### interval
>> Type: int  
>> Default: 1000  
>> Sets how many milliseconds between each scan of the image folder  
>   
> ### start_on_init
>> Type: bool  
>> Default: True  
>> If True, the program will start the previewers as soon as they're initialized  
>> Else, it must be started with the "start" method  
>   
> ### path
>> Type: str  
>> Default: the current working directory  
>> Defines what folder to scan  
>   
> ### ext
>> Type: str  
>> Default: png  
>> Defines what type of image the previewer will scan for  
>> NOTE: case-sensitive  
>   
> ### previewer_count
>> Type: int  
>> Default: 1  
>> Defines how many windows will be ran  


### Example usage
> #### Basic usage
>     from ImagePreview import ImagePreviewer
>     ImagePreviewer()
> #### Specific folder and image type
>     from ImagePreview import ImagePreviewer
>     ImagePreviewer(path='C:/Users/User/Pictures/', ext='jpg')
> #### Multiple windows
>     from ImagePreview import ImagePreviewer
>     ImagePreviewer(previewer_count=2)
> #### Run the previewer at a later time
>     from ImagePreview import ImagePreviewer
>     impr = ImagePreviewer(write_on_creation=False)
>     
>     # Your code goes here...
>     
>     impr.start()
