from PIL import Image

def create_Spritesheet(file):
    frames = []

    if file.endswith(".gif"):
        with Image.open(file) as im:
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

def create_GIF(file, frameSize, filename):
    with Image.open(file) as im:
        width, height = frameSize
        left, upper, right, lower = 0, 0, width, height

        frameNumber = im.width // width
        frames = []

        for i in range(frameNumber):
            frame = im.crop((left, upper, right, lower))
            frames.append(frame)

            left  += width
            upper += 0
            right += width
            lower += 0
        
        frames[0].save(filename + '.gif', format='GIF', 
                        append_images=frames[1:], 
                        save_all=True, 
                        duration=150, 
                        loop=0)

# create_Spritesheet(file)
# create_GIF('3x spritesheet.png', (112, 112), 'export')

# Todo
    # Get file from sysarg
    # Define number of rows and cols
    # Spritesheet to gif
    # apply naming conventions