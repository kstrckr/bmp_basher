import binascii

# file header

# bfType      2   The Characters 'BM'
# bfSize      4   the size of the file in bytes
# bfReserved1 2   0
# bfReserved2 2   0
# bfOffBits   4   offset to start pixel data (from beginning of file)

# image header

# biSize          4   header size - must be at least 40
# biWidth         4   image width in pixels
# biHeight        4  image height in pixels
# biPlanes        2   must = 1
# biBitCount      2   Bits per pixel - 1, 4, 8, 16, 24, or 32
# biCompression   4   compression type (0 = uncompressed)
# biSizeImage     4   Image size - may be zero for uncompressed images
# biXPelsPerMeter 4   preffered resolution in pixels per biXPelsPerMeter
# biYPelsPerMeter 4   preferred resolution in pixels per biXPelsPerMeter
# biClrUsed       4   Number color map entries biClrUsed
# biClrImportant  4   number of significant colors

with open('bmp.bmp', 'br') as raw_image:
    image_data = raw_image.read()
    
    # for value in image_data:
    #     print(value)

    
file_header_offset = [2, 4, 2, 2, 4]
image_header_offset = [4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4]

def split_headers(offset_array, start_index=0):
    current_index = start_index

    file_header = []
    for offset in offset_array:

        buffer = []
        value = image_data[current_index:offset+current_index]
        for byte in value:
            buffer.append(hex(byte))

        file_header.append(buffer)
        buffer = []
        current_index += offset
        
    for value in file_header:
        print(value)

split_headers(file_header_offset)
print('\n')
split_headers(image_header_offset, 14)