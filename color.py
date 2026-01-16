import sys

def write(bb:bytes):
    sys.stdout.buffer.write(bb)

def u8(i:int):
    write(i.to_bytes(1,'little'))

def u16(i:int):
    write(i.to_bytes(2,'little'))

def u32(i:int):
    write(i.to_bytes(4,'little'))

def rgb(red,green,blue:int):
    u8(blue)
    u8(green)
    u8(red)

    width=100
    height=100
    
    #file header BMP
    write(b'BM')
    u32(14+40 + width*height*3)
    u32(0)
    u32(0)
    u32(14+40)

    # DIB header
    u32(40)
    u32(width)
    u32(height)
    u16(1)
    u16(24)
    u32(0)
    u32(0)
    u32(0) 
    u32(0)
    u32(0)
    u32(0)

    for py in range(height):
        for px in range(width):
            rgb(255,180,0)
