import os
import sys
from pdf2image import convert_from_path

def convert(filepath: str):

    name = os.path.splitext(filepath)[0]

    # Store Pdf with convert_from_path function
    images = convert_from_path(name + '.pdf')
    
    for i in range(len(images)):
    
        # Save pages as images in the pdf
        images[i].save(name + '-'+ str(i) +'.png', 'PNG')


if __name__ == '__main__':

    if len(sys.argv) <= 1:
        print('USAGE:', sys.argv[0], '<pdf file path>')
    else:
        print('Converting', sys.argv[1])
        convert(sys.argv[1])
