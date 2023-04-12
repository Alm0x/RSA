# Digital Signature Implementation using RSA Algorithm

This project provides a Python implementation of digital signature using RSA algorithm.

## Usage

### Generate keys

To generate public and private keys, run the following command:

`python main.py --generate-keys`


This will generate two files `public_key.pem` and `private_key.pem` in the `keys` directory.

### Sign a file

To sign a file using private key, run the following command:

`python main.py --sign <filename>`


This will generate a new file with `.sig` extension, which contains the digital signature.

### Verify signature

To verify the signature of a file using public key, run the following command:

`python main.py --verify <filename>`

This will verify the signature of the file and print whether the signature is valid or not.
