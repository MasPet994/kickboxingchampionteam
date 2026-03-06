from PIL import Image

def convert_image():
    try:
        img = Image.open('logo.png').convert('RGBA')
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Replace white background with transparent
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                newData.append((255, 255, 255, 0))
            # Replace black parts with white for dark mode compatibility (while maintaining alpha)
            elif item[0] < 50 and item[1] < 50 and item[2] < 50 and item[3] > 0:
                newData.append((255, 255, 255, item[3]))
            else:
                newData.append(item)
                
        img.putdata(newData)
        img.save('logo.png', 'PNG')
        print('Success')
    except Exception as e:
        print('Error:', e)

convert_image()
