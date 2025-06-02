import numpy as np
from PIL import Image
import cv2

import base64
from Crypto.Cipher import AES
import config
import concurrent.futures

ENABLE_ENCRYPTION = getattr(config, 'enable_encryption', False)
KEY = getattr(config, 'encryption_key', 'DefaultEncryptionKey').encode("ascii")[:16]


def quotient_remainder(divident, divsor):
    return divident // divsor, divident % divsor


def color_value(x):
    return x*255


def normal(x):
    return x/255


def encrypt_data_aes(data: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return base64.urlsafe_b64encode(cipher.nonce + tag + ciphertext)


def decrypt_data_aes(data: bytes, key: bytes) -> bytes:
    raw = base64.urlsafe_b64decode(data)
    nonce, tag, ciphertext = raw[:16], raw[16:32], raw[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    clear_data = cipher.decrypt_and_verify(ciphertext, tag)
    return clear_data


def prepare_frame(args):
    frame_bytes, num_rows_per_frame, num_cols_per_frame, color_value, size = args
    frame_bits = np.unpackbits(frame_bytes)
    frame = color_value(frame_bits).reshape(num_rows_per_frame, num_cols_per_frame, 3).astype(np.uint8)
    newimg = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    return newimg


def encode(infile_path, outvideo_path, encrypt=ENABLE_ENCRYPTION, key=KEY,
           fps=20, num_cols_per_frame=64, num_rows_per_frame=36):
    with open(infile_path, 'rb') as fd:
        raw_data_bytes = fd.read()
    if encrypt:
        raw_data_bytes = encrypt_data_aes(raw_data_bytes, key)
    data_bytes = np.frombuffer(raw_data_bytes, dtype=np.uint8)
    len_of_data = len(data_bytes)
    num_bytes_per_row = int(num_cols_per_frame * 3 / 8)
    num_bytes_per_frame = num_bytes_per_row * num_rows_per_frame

    # Avoid unnecessary np.array conversion
    len_bytes = np.frombuffer(len_of_data.to_bytes(4, byteorder='big'), dtype=np.uint8)
    total_data = [len_bytes, data_bytes]

    (num_frames, num_leftover_bytes) = quotient_remainder(4 + len_of_data, num_bytes_per_frame)

    if num_leftover_bytes > 0:
        num_bytes_last_frame_padding = num_bytes_per_frame - num_leftover_bytes
        # Use np.zeros instead of np.full for zero padding
        padding_bytes = np.zeros(num_bytes_last_frame_padding, dtype=np.uint8)
        total_data.append(padding_bytes)
        num_frames += 1

    # Concatenate only once
    data_bytes = np.concatenate(total_data)

    size = (num_cols_per_frame * 20, num_rows_per_frame * 20)
    video = cv2.VideoWriter(outvideo_path, cv2.VideoWriter_fourcc(
        *'mp4v'), fps, size)

    args_list = [
        (
            data_bytes[i * num_bytes_per_frame: (i + 1) * num_bytes_per_frame],
            num_rows_per_frame,
            num_cols_per_frame,
            color_value,
            size
        )
        for i in range(num_frames)
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for newimg in executor.map(prepare_frame, args_list):
            video.write(newimg)


def decode(invideo_path, outfile_path, decrypt=ENABLE_ENCRYPTION, key=KEY):
    step = 20
    cap = cv2.VideoCapture(invideo_path)
    data_bits_list = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Vectorized block extraction
        blocks = frame.reshape(frame.shape[0]//step, step, frame.shape[1]//step, step, 3)
        blocks = blocks.transpose(0,2,1,3,4).reshape(-1, step*step, 3)
        means = normal(blocks.mean(axis=1)).round().astype(np.uint8)
        data_bits_list.append(means)
    cap.release()
    data_bits = np.concatenate(data_bits_list).reshape(-1, 1)
    data_bytes = np.packbits(data_bits)
    len_of_data = int.from_bytes(data_bytes[:4], byteorder='big')
    data_bytes_retrieved = data_bytes[4:len_of_data+4].tobytes()
    if decrypt:
        data_bytes_retrieved = decrypt_data_aes(data_bytes_retrieved, key)
    with open(outfile_path, 'wb') as fd:
        fd.write(data_bytes_retrieved)


if __name__ == '__main__':
    # encode("../examples/painting.jpg", "../examples/upload.mp4")
    # decode("../examples/upload.mp4", "../examples/painting-retrieved2.jpg")
    pass