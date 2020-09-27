from Class import squareImage

configDict = {
    'imageFolder'     : 'img',
    'saveImageFolder' : 'saveImg',
    'imageName'       : 'Lenna.jpg',
    'squareSize'      : 190,
    'quality'         : 95,
    'backgroundColor' : (255,255,255)
    }

pil = squareImage.ImageClass(configDict)

saveImageName = pil.ImageSquare(configDict) # Size Quality BackgroundColor

pil.ImageSquareBorderAdd(configDict, saveImageName, borderColor=(0,0,0), Thickness=2)
