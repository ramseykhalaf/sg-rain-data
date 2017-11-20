import imageio
import numpy as np

colourList = [
    [0, 0, 0, 0],
    [0, 255, 255, 255],
    [0, 239, 239, 255],
    [0, 209, 213, 255],
    [0, 186, 191, 255],
    [0, 151, 154, 255],
    [0, 131, 125, 255],
    [0, 128, 69, 255],
    [0, 137, 56, 255],
    [0, 162, 53, 255],
    [0, 183, 41, 255],
    [0, 202, 17, 255],
    [0, 218, 13, 255],
    [0, 245, 7, 255],
    [0, 255, 0, 255],
    [67, 255, 65, 255],
    [72, 255, 70, 255],
    [255, 255, 59, 255],
    [255, 255, 0, 255],
    [255, 240, 0, 255],
    [255, 220, 0, 255],
    [255, 198, 0, 255],
    [255, 178, 0, 255],
    [255, 165, 0, 255],
    [255, 138, 0, 255],
    [255, 114, 0, 255],
    [255, 73, 0, 255],
    [255, 31, 0, 255],
    [229, 0, 0, 255],
    [193, 0, 0, 255],
    [182, 0, 106, 255],
    [210, 0, 165, 255],
    [212, 0, 170, 255],
    [255, 0, 255, 255]
]

def analyse_image(file_name):
    arr = imageio.imread(file_name)
    intensity = np.zeros(arr.shape[:2])

    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            intensity[i,j] = colourList.index(arr[i,j].tolist())/(len(colourList)-1)

    return intensity

if __name__ == "__main__":
    intensity = analyse_image('data/2017-11-15/dpsri_240km_2017111519450000dBR.dpsri.png')
    print(intensity)
    # imageio.imwrite('sample.png', np.asarray([colourList]).astype(np.uint8))
