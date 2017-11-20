import numpy as np

import image_analyser

def test_analyse_image():
    expected = np.asarray([[
        0/33,
        1/33,
        2/33,
        3/33,
        4/33,
        5/33,
        6/33,
        7/33,
        8/33,
        9/33,
        10/33,
        11/33,
        12/33,
        13/33,
        14/33,
        15/33,
        16/33,
        17/33,
        18/33,
        19/33,
        20/33,
        21/33,
        22/33,
        23/33,
        24/33,
        25/33,
        26/33,
        27/33,
        28/33,
        29/33,
        30/33,
        31/33,
        32/33,
        33/33
    ]])

    result = image_analyser.analyse_image("testData/sample.png")

    assert((result==expected).all())
