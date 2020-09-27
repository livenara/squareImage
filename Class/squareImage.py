from PIL import Image, ImageDraw

class ImageClass():
    
    def __init__(self,configDict):
        self.configDict = configDict


    def ImageSquare(self, configDict):

        saveImageName = self.configDict['saveImageFolder'] + '\\' + self.configDict['imageName'].split('.')[0] + '.jpg'
        imagePath = Image.open(self.configDict['imageFolder'] + '\\' + self.configDict['imageName'])
        width, height = imagePath.size

        if width == height:
            imagePath.save(saveImageName, quality=self.configDict['quality'])
        elif width > height:
            result = Image.new(imagePath.mode, (width, width), self.configDict['backgroundColor'])
            result.paste(imagePath, (0, (width - height) // 2))
            result = result.resize((self.configDict['squareSize'], self.configDict['squareSize']))
            result.save(saveImageName, quality=configDict['quality'])
        else:
            result = Image.new(imagePath.mode, (height, height), self.configDict['backgroundColor'])
            result.paste(imagePath, ((height - width) // 2, 0))
            result = result.resize((self.configDict['squareSize'], self.configDict['squareSize']))
            result.save(saveImageName, quality=self.configDict['quality'])
        return saveImageName


    def ImageSquareBorderAdd(self, configDict, saveImageName, borderColor, Thickness):

        self.configDict['borderColor'] = borderColor
        canvus = Image.open(saveImageName)
        canvus = canvus.resize((self.configDict['squareSize'], self.configDict['squareSize']))
        draw = ImageDraw.Draw(canvus)
        draw.rectangle([(0, 0), (self.configDict['squareSize'] - 1, self.configDict['squareSize'] - 1)], outline=self.configDict['borderColor'], width=Thickness)
        canvus.save(saveImageName, quality=configDict['quality'])
        return saveImageName


if __name__ == "__main__":

    configDict = {
        'imageFolder'     : 'img',
        'saveImageFolder' : 'saveImg',
        'imageName'       : 'Lenna.jpg',
        'squareSize'      : 190,
        'quality'         : 95,
        'backgroundColor' : (255,255,255)
    }

    pil = ImageClass(configDict)
    saveImageName = pil.ImageSquare(configDict)
    pil.ImageSquareBorderAdd(configDict, saveImageName, borderColor=(0,0,0), Thickness=2)

