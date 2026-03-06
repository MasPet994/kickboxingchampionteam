from PIL import Image
import os

def process_sponsors():
    for i in range(1, 7):
        filename = f'sponsor{i}.png'
        filepath = os.path.join('images', filename)
        if not os.path.exists(filepath):
            print(f'File {filename} not found, skipping.')
            continue
            
        try:
            img = Image.open(filepath).convert('RGBA')
            datas = img.getdata()
            
            newData = []
            for item in datas:
                # If it's white or very light, make it transparent
                if item[0] > 220 and item[1] > 220 and item[2] > 220:
                    newData.append((255, 255, 255, 0))
                # If it's black or very dark, make it white
                elif item[0] < 60 and item[1] < 60 and item[2] < 60:
                    newData.append((255, 255, 255, 255))
                else:
                    newData.append(item)
            
            img.putdata(newData)
            img.save(filepath, 'PNG')
            print(f'Processed {filename}')
        except Exception as e:
            print(f'Error processing {filename}: {e}')

if __name__ == '__main__':
    process_sponsors()
