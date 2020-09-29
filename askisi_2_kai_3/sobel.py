import argparse, sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

class image_data:
    def __init__(self, image_path, image, gray_image, sobel):
        self.image_path = image_path
        self.image = image
        self.gray_image = gray_image
        self.sobel = sobel
        
def convert_gray(imgData):
    imgData.image = Image.open(imgData.image_path)
    image = np.array(imgData.image)
    imgData.gray_image = image
    rows = image.shape[0]
    columns = image.shape[1]
    if (len(image.shape) == 3): #periptwsh opou den einai grayscale
        image2 = np.zeros((rows,columns))
        for i in range(rows):
            for j in range(columns):
                image2[i][j] = (int(image[i][j][0])
                                    +int(image[i][j][1])+int(image[i][j][2]))/3.0
        imgData.gray_image = image2
    plt.imshow(imgData.gray_image, cmap="gray")
    plt.show()

def sobel_tranform(imgData, threshold):
    x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    y = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
    Gx = convolve2d(imgData.gray_image, x, mode = 'same')
    Gy = convolve2d(imgData.gray_image, y, mode = 'same')
    G=np.sqrt(np.add(Gx*Gx, Gy*Gy))
    threshold = np.max(G) * threshold
    rows = G.shape[0]
    columns = G.shape[1]
    image2 = np.zeros((rows,columns))
    for i in range(rows):
        for j in range(columns):
            if (G[i][j] > threshold):
                image2[i][j] = 255
    imgData.sobel = image2
    plt.imshow(imgData.sobel, cmap="gray")
    plt.show()
        
        
def main(args):
    imgData = image_data(image_path = args.image_path, image = None, gray_image = None, sobel = None)
    convert_gray(imgData)
    sobel_tranform(imgData, args.threshold)
    
def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('image_path', type=str, 
        help='path of the input image')
    parser.add_argument('threshold', type=float, 
        help='for sobel\'s threshold. (float) range: 0 - 1.0')
    return parser.parse_args(argv)
    
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))