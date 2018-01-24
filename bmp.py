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

with open('100x100.bmp', 'br') as raw_image:
    image_data = raw_image.read()
    
    # for value in image_data:
    #     print(value)

    
file_header_offset = [2, 4, 2, 2, 4]
image_header_offset = [4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4]

def split_headers(offset_array, start_index=0):
    current_index = start_index

    header = []
    for offset in offset_array:

        buffer = []
        value = image_data[current_index:offset+current_index]
        for byte in value:
            buffer.append(int(hex(byte), 16))

        header.append(buffer)
        buffer = []
        current_index += offset
        
    return header

    #print(len(image_data[current_index:]))

def print_pixel_values(start_index=54):
    pixel_data = []
    buffer = []

    for value in image_data[start_index:]:
        buffer.append(value)

        if len(buffer) == 4:
            pixel_data.append(buffer)
            buffer = []
    return pixel_data

def eight_bit_color_table():
    table_line = []
    color_table = []
    current_index = 0

    for value in image_data[54:118]:
        table_line.append(value)
        current_index += 1

        if current_index == 4:
            current_index = 0
            color_table.append(table_line)
            table_line = []

    for row in color_table:
        print(row)



file_header = split_headers(file_header_offset)

for row in file_header:
    print(hex(row[1]))
# file_header[2][0] = 100
# file_header[3][0] = 100

image_header = split_headers(image_header_offset, 14)
print('\n')
pixel_data = print_pixel_values()

new_pixel_data = []
single_pixel = [255, 0, 0]

for i in range(10000):
    if i % 2 == 0:
        new_pixel_data.append(single_pixel)
    else:
        new_pixel_data.append(single_pixel[::-1])
#eight_bit_color_table()

# print(new_pixel_data)

#print('{}\n{}\n{}'.format(file_header, image_header, new_pixel_data))
# for byte in image_data[117:218]:
#     print(byte)

def unify_values_for_bmp(file_header, image_header, new_pixel_data):

    data_list = [file_header, image_header, new_pixel_data]
    final_output = []

    for file_section in data_list:
        for field in file_section:
            for value in field:
                final_output.append(value)

    return final_output

new_bmp_hex = unify_values_for_bmp(file_header, image_header, new_pixel_data)

print(len(bytes(new_bmp_hex)))


with open('new.bmp', 'wb') as new_image:
        new_image.write(bytes(new_bmp_hex))