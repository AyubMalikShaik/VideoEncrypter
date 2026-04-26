import numpy as np

def xor_encrypt(frame, key):
    key_array = np.frombuffer(key, dtype=np.uint8)

    # Repeat key to match total pixel count
    repeated_key = np.resize(key_array, frame.size)

    flat_frame = frame.flatten()

    encrypted = np.bitwise_xor(flat_frame, repeated_key)

    return encrypted.reshape(frame.shape)


def process_frame(frame, key):
    return xor_encrypt(frame, key)