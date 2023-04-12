import argparse
import rsa


def generate_keys():
    (pubkey, privkey) = rsa.newkeys(2048)
    with open('keys/public.pem', mode='wb') as public_file:
        public_file.write(pubkey.save_pkcs1())
    with open('keys/private.pem', mode='wb') as private_file:
        private_file.write(privkey.save_pkcs1())
    print("Keys generated successfully!")


def sign_file(filename):
    with open('keys/private.pem', mode='rb') as private_file:
        keydata = private_file.read()
        privkey = rsa.PrivateKey.load_pkcs1(keydata)
    with open(filename, mode='rb') as file:
        filedata = file.read()
        signature = rsa.sign(filedata, privkey, 'SHA-256')
    with open(filename + '.sig', mode='wb') as sig_file:
        sig_file.write(signature)
    print("File signed successfully!")


def verify_file(filename):
    with open('keys/public.pem', mode='rb') as public_file:
        keydata = public_file.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
    with open(filename, mode='rb') as file:
        filedata = file.read()
    with open(filename + '.sig', mode='rb') as sig_file:
        sigdata = sig_file.read()
        try:
            rsa.verify(filedata, sigdata, pubkey)
            print("Signature is valid")
        except rsa.VerificationError:
            print("Signature is not valid")


def main():
    parser = argparse.ArgumentParser(description='Digital signature implementation')
    parser.add_argument('--generate-keys', '-g', action='store_true', help='Generate public and private keys')
    parser.add_argument('--sign', '-s', type=str, help='Sign the given file')
    parser.add_argument('--verify', '-v', type=str, help='Verify the given file')

    args = parser.parse_args()

    if args.generate_keys:
        generate_keys()
    elif args.sign:
        sign_file(args.sign)
    elif args.verify:
        verify_file(args.verify)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
