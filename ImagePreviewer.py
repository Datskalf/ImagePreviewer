import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.animation as animation
import os
import glob



###### Image writer ######
class ImageWriter:
	path = 'C:/Users/Datskalf/Pictures/Screenshots/'
	ext = 'png'
	figs = []
	axs = []

	def __init__(self, write_on_creation: bool = False, path: str = '', ext: str = '', previewer_count: int = 1):
		self.path = path if path else self.path
		self.ext = ext if ext else self.ext

		plt.interactive(True)

		for i in range(previewer_count):
			self.figs.append(plt.figure(i))
			self.axs.append(self.figs[i].add_subplot(111))
			self.axs[i].set_axis_off()
		self.plt_count = previewer_count

		self.latest_image = ''

		if write_on_creation:
			self.write_latest_image()

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

	def write_latest_image(self, *args) -> None:
		print('\n###############################')
		print('## Checking for new image... ##')
		if self._update_latest_image():
			print('## Writing to figure...      ##')

			for i in range(self.plt_count):
				self.axs[i].imshow(mpimg.imread(self.latest_image))
				self.figs[i].show()
			
			print('## Finished writing!         ##')
		print('###############################\n')
	
	def create_animators(self, interval: int = 1000):
		self.animators = []
		for i in range(self.plt_count):
			self.animators.append(animation.FuncAnimation(self.figs[i], self.write_latest_image, interval=interval))



###### Main entry point ######
if __name__ == '__main__':
	iw = ImageWriter(previewer_count=2) # Create an instance of the ImageWriter class

	iw.create_animators() # Create the animators

	print('Locks the image output when text is entered')
	print('Press Ctrl+C or type exit to exit')

	while True: # Needs a loop to keep the program running
		inp = input()
		if inp == 'exit':
			break