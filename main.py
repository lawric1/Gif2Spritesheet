from PIL import Image

file = '3x.gif'

def create_Spritesheet(file):
    frames = []

    if file.endswith(".gif"):
        with Image.open('3x.gif') as im:
            print(im)
            for i in range(im.n_frames):
                im.seek(i)
                frames.append(im.convert('RGB'))
    else:
        print('Wrong file type')

    spriteSheet_width = sum([frame.width for frame in frames])
    spriteSheet = Image.new('RGBA', (spriteSheet_width, frames[0].height))

    width, height = 0, 0

    for frame in frames:
        spriteSheet.paste(frame, (width, height))
        width += frame.width

    spriteSheet.save(file[:-4] + ' spritesheet.png')

create_Spritesheet(file)