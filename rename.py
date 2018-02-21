import os
path = '/Users/Lanbig/Desktop/images3'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'image_ce_mark_3_' + str(i)+'.jpg'))
    i = i+1
