#!/usr/bin/env python
# encoding: utf-8

import sys
import os
if len(sys.argv) <= 1:
    print('missing parameter, use like:\t%s ../sample/3026472-128-42ba051cdf72bda1d93b9c506be44505.uc [output]' % __file__)
    exit(1)
if not os.path.isfile(sys.argv[1]):
    print('exist %s' % sys.argv[1])
    exit(2)

netmusic_code = {'\x00': '\xa3', '\x83': ' ', '\x04': '\xa7', '\x87': '$', '\x08': '\xab', '\x8b': '(', '\x0c': '\xaf', '\x8f': ',', \
        '\x10': '\xb3', '\x93': '0', '\x14': '\xb7', '\x97': '4', '\x18': '\xbb', '\x9b': '8', '\x1c': '\xbf', '\x9f': '<', \
        ' ': '\x83', '\xa3': '\x00', '$': '\x87', '\xa7': '\x04', '(': '\x8b', '\xab': '\x08', ',': '\x8f', '\xaf': '\x0c', \
        '0': '\x93', '\xb3': '\x10', '4': '\x97', '\xb7': '\x14', '8': '\x9b', '\xbb': '\x18', '<': '\x9f', '\xbf': '\x1c', \
        '@': '\xe3', '\xc3': '`', 'D': '\xe7', '\xc7': 'd', 'H': '\xeb', '\xcb': 'h', 'L': '\xef', '\xcf': 'l', 'P': '\xf3', \
        '\xd3': 'p', 'T': '\xf7', '\xd7': 't', 'X': '\xfb', '\xdb': 'x', '\\': '\xff', '\xdf': '|', '`': '\xc3', '\xe3': '@', \
        'd': '\xc7', '\xe7': 'D', 'h': '\xcb', '\xeb': 'H', 'l': '\xcf', '\xef': 'L', 'p': '\xd3', '\xf3': 'P', 't': '\xd7', \
        '\xf7': 'T', 'x': '\xdb', '\xfb': 'X', '|': '\xdf', '\xff': '\\', '\x80': '#', '\x03': '\xa0', '\x84': "'", '\x07': '\xa4', \
        '\x88': '+', '\x0b': '\xa8', '\x8c': '/', '\x0f': '\xac', '\x90': '3', '\x13': '\xb0', '\x94': '7', '\x17': '\xb4', \
        '\x98': ';', '\x1b': '\xb8', '\x9c': '?', '\x1f': '\xbc', '\xa0': '\x03', '#': '\x80', '\xa4': '\x07', "'": '\x84', \
        '\xa8': '\x0b', '+': '\x88', '\xac': '\x0f', '/': '\x8c', '\xb0': '\x13', '3': '\x90', '\xb4': '\x17', '7': '\x94', \
        '\xb8': '\x1b', ';': '\x98', '\xbc': '\x1f', '?': '\x9c', '\xc0': 'c', 'C': '\xe0', '\xc4': 'g', 'G': '\xe4', \
        '\xc8': 'k', 'K': '\xe8', '\xcc': 'o', 'O': '\xec', '\xd0': 's', 'S': '\xf0', '\xd4': 'w', 'W': '\xf4', '\xd8': '{', \
        '[': '\xf8', '\xdc': '\x7f', '_': '\xfc', '\xe0': 'C', 'c': '\xc0', '\xe4': 'G', 'g': '\xc4', '\xe8': 'K', 'k': '\xc8', \
        '\xec': 'O', 'o': '\xcc', '\xf0': 'S', 's': '\xd0', '\xf4': 'W', 'w': '\xd4', '\xf8': '[', '{': '\xd8', '\xfc': '_', \
        '\x7f': '\xdc', '\x81': '"', '\x02': '\xa1', '\x85': '&', '\x06': '\xa5', '\x89': '*', '\n': '\xa9', '\x8d': '.', \
        '\x0e': '\xad', '\x91': '2', '\x12': '\xb1', '\x95': '6', '\x16': '\xb5', '\x99': ':', '\x1a': '\xb9', '\x9d': '>', \
        '\x1e': '\xbd', '\xa1': '\x02', '"': '\x81', '\xa5': '\x06', '&': '\x85', '\xa9': '\n', '*': '\x89', '\xad': '\x0e', \
        '.': '\x8d', '\xb1': '\x12', '2': '\x91', '\xb5': '\x16', '6': '\x95', '\xb9': '\x1a', ':': '\x99', '\xbd': '\x1e', \
        '>': '\x9d', '\xc1': 'b', 'B': '\xe1', '\xc5': 'f', 'F': '\xe5', '\xc9': 'j', 'J': '\xe9', '\xcd': 'n', 'N': '\xed', \
        '\xd1': 'r', 'R': '\xf1', '\xd5': 'v', 'V': '\xf5', '\xd9': 'z', 'Z': '\xf9', '\xdd': '~', '^': '\xfd', '\xe1': 'B', \
        'b': '\xc1', '\xe5': 'F', 'f': '\xc5', '\xe9': 'J', 'j': '\xc9', '\xed': 'N', 'n': '\xcd', '\xf1': 'R', 'r': '\xd1', \
        '\xf5': 'V', 'v': '\xd5', '\xf9': 'Z', 'z': '\xd9', '\xfd': '^', '~': '\xdd', '\x01': '\xa2', '\x82': '!', '\x05': '\xa6', \
        '\x86': '%', '\t': '\xaa', '\x8a': ')', '\r': '\xae', '\x8e': '-', '\x11': '\xb2', '\x92': '1', '\x15': '\xb6', '\x96': '5', \
        '\x19': '\xba', '\x9a': '9', '\x1d': '\xbe', '\x9e': '=', '!': '\x82', '\xa2': '\x01', '%': '\x86', '\xa6': '\x05', ')': '\x8a', \
        '\xaa': '\t', '-': '\x8e', '\xae': '\r', '1': '\x92', '\xb2': '\x11', '5': '\x96', '\xb6': '\x15', '9': '\x9a', '\xba': '\x19', \
        '=': '\x9e', '\xbe': '\x1d', 'A': '\xe2', '\xc2': 'a', 'E': '\xe6', '\xc6': 'e', 'I': '\xea', '\xca': 'i', 'M': '\xee', \
        '\xce': 'm', 'Q': '\xf2', '\xd2': 'q', 'U': '\xf6', '\xd6': 'u', 'Y': '\xfa', '\xda': 'y', ']': '\xfe', '\xde': '}', \
        'a': '\xc2', '\xe2': 'A', 'e': '\xc6', '\xe6': 'E', 'i': '\xca', '\xea': 'I', 'm': '\xce', '\xee': 'M', 'q': '\xd2', \
        '\xf2': 'Q', 'u': '\xd6', '\xf6': 'U', 'y': '\xda', '\xfa': 'Y', '}': '\xde', '\xfe': ']'}

with open(sys.argv[1], 'rb') as f:
    k = f.read()

encode_path, encode_file = os.path.split(sys.argv[1])
if len(sys.argv) == 3:
    decode_file = sys.argv[2]
else:
    if encode_file.find('.') <= 0:
        decode_file = os.path.join(encode_path, encode_file + ".mp3")
    else:
        decode_file = os.path.join(encode_path, '.'.join(encode_file.split('.')[:-1]) + ".mp3") 

with open(decode_file, 'wb' ) as f:
    for i in range(len(k)):
        f.write(netmusic_code[k[i]])


