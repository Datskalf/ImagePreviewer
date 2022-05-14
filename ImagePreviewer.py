import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import os
import glob



###### Image writer ######
class ImagePreviewer:
    ### Default values ###
    path = os.getcwd()
    ext = 'png'
    latest_image = ''
    figs = []
    axs = []



    def __init__(self, interval: int = 1000, start_on_init: bool = True, path: str = '', ext: str = '', previewer_count: int = 1):
        self.path = path if path else self.path
        self.ext = ext if ext else self.ext
        self.interval = interval

        plt.interactive(True)

        for i in range(previewer_count):
            self.figs.append(plt.figure(i))
            self.axs.append(self.figs[i].add_subplot(111))
            self.axs[i].set_axis_off()
        self.plt_count = previewer_count

        if start_on_init:
            self.start()
    


    # Gets and Sets
    def set_path(self, path: str) -> None:
        self.path = path
    
    def set_ext(self, ext: str) -> None:
        self.ext = ext

    def set_interval(self, interval: int) -> None:
        self.interval = interval

    def set_plt_count(self, plt_count: int) -> None:
        self.plt_count = plt_count

    def get_plt_count(self) -> int:
        return self.plt_count

    def get_path(self) -> str:
        return self.path

    def get_ext(self) -> str:
        return self.ext




    def _update_latest_image(self) -> bool:
        files = glob.glob(self.path + '*.' + self.ext)
        latest_file = max(files, key=os.path.getctime)

        if self.latest_image == latest_file:
            print('## No new image found.       ##')
            return False
        else:
            print('## New image found!          ##')
            self.latest_image = latest_file
            return True

    def _write_latest_image(self, *args) -> None:
        print('\n###############################')
        print('## Checking for new image... ##')
        if self._update_latest_image():
            print('## Writing to figure...      ##')

            for i in range(self.plt_count):
                self.axs[i].imshow(mpimg.imread(self.latest_image))
                self.figs[i].show()
            
            print('## Finished writing!         ##')
        print('###############################\n')
    


    # Starts the image previewer
    def start(self) -> None:
        self.animators = []
        for i in range(self.plt_count):
            self.animators.append(animation.FuncAnimation(self.figs[i], self.write_latest_image, interval=self.interval))
        
        print('Locks the image output when text is entered')
        print('Press Ctrl+C or type exit to exit')

        while True:  # Needs a loop to keep the program running
            inp = input()
            if inp == 'exit':
                break



###### Main entry point ######
if __name__ == '__main__':
    ImagePreviewer(previewer_count=1) # Create an instance of the ImageWriter class