import struct

# pack与unpack
# '>'代表big-endian编码
# 'I'代表4个字节的整数
# 'H'代表2字节无符号整数
print(struct.pack('>I', 1050624))  # b'\x00\x10\x08\x00'
print(struct.pack('>I', 10240064))  # b'\x00\x9c@@'
print(struct.unpack('>IH', b'\x00\x9c\x40\x40\x7c\x80'))  # (10240064, 31872)

with open('sample.bmp','rb') as f:
    header = struct.unpack('<2c6I2H',f.read(30))
    print(header)
    print('图片大小',header[2])
    print('实际图片偏移量', header[4])
    print('header字节数', header[5])
    print('宽度', header[6])
    print('高度', header[7])
    print('颜色数', header[9])
'''
(b'\xff', b'\xd8', 268493055, 1179207242, 16843008, 1207977984, 3690921984, 50348800, 514, 515)
图片大小 268493055
实际图片偏移量 16843008
header字节数 1207977984
宽度 3690921984
高度 50348800
颜色数 515
'''