import sys

def patch_11e(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = bytearray(f.read())
    
    # The VSS/NVRAM area starts where your grep found 'VSS'
    # We are zeroing the common NVRAM password variable offsets for 11e
    # Target range: 0x770000 to 0x800000 (The top 512KB-1MB)
    start_offset = 0x770000
    end_offset = 0x7FFFFF
    
    print(f"Patching NVRAM range {hex(start_offset)} to {hex(end_offset)}...")
    for i in range(start_offset, end_offset + 1):
        data[i] = 0xFF # FF is the 'empty' state for SPI Flash
        
    with open(output_file, 'wb') as f:
        f.write(data)
    print(f"Success: {output_file} created.")

if __name__ == "__main__":
    patch_11e('backup1.bin', 'patched_11e.bin')
