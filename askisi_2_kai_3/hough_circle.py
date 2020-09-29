import sobel
import argparse, sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from math import cos, sin, pi
from collections import defaultdict

def main(args):
    
    def dimension(x):
        return x[1]
    
    r_min = 10
    r_max = 20
    
    imgData = sobel.image_data(image_path = args.image_path, image = None, gray_image = None, sobel = None)
    sobel.convert_gray(imgData)
    sobel.sobel_tranform(imgData, args.sobel_threshold)
    
    output_image = Image.new("RGB", imgData.image.size)
    output_image.paste(imgData.image)
    for_circle = ImageDraw.Draw(output_image)

    points = []
    for r in range(r_min, r_max + 1):
        for t in range(100):
            points.append((r, int(r * cos(2 * pi * t / 100)),  #dx
                            int(r * sin(2 * pi * t / 100))))   #dy
    
    white_pix = []
    for x in range(len(imgData.sobel)):
        for y in range(len(imgData.sobel[x])):
            if imgData.sobel[x][y] == 255:
                white_pix.append((x,y))
                
    votes = defaultdict(int)
    for x, y in white_pix:
        for r, dx, dy in points:
            a = x - dx
            b = y - dy
            votes[(a, b, r)] += 1

    circles = []
    asc_list= sorted(votes.items(), reverse=True, key=dimension)        # kanei sort ws pros ton auksonta psifo
    for k, v in asc_list:
        y, x, r = k         #grb
        cond = True
        for xc, yc, rc in circles:
            if pow((x - xc), 2) + pow((y - yc), 2) <= pow(rc, 2):
                cond = False
                break
        if v / 100 >= args.hough_threshold and cond:
            circles.append((x, y, r))
            print('confidence: ' + str(v / 100))
            print('radius: '+ str(r))
            print('\n')

    for x, y, r in circles: for_circle.ellipse((x-r, y-r, x+r, y+r), outline=(0,255,0))
    plt.imshow(np.array(output_image))
    plt.show()

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    
    parser.add_argument('image_path', type=str, 
        help='path of the input image')
    parser.add_argument('sobel_threshold', type=float, 
        help='for sobel\'s threshold. (float) range: 0 - 1.0')
    parser.add_argument('--hough_threshold', type=float, 
        help='for hough\'s threshold. (float) range: 0 - 1.0', default=0.6)
    
    return parser.parse_args(argv)
    
if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))