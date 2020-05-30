import OpenSSL
from OpenSSL._util import lib as _lib, ffi as _ffi
from OpenSSL.crypto import _new_mem_buf, _bio_to_string

bio_pub = _new_mem_buf()  # Memory buffers to write to
bio_priv = _new_mem_buf()

helper = OpenSSL.crypto._PassphraseHelper(OpenSSL.crypto.FILETYPE_PEM, None)

pk = OpenSSL.crypto.PKey()
pk.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

# Convert from EVP_PKEY type to RSA type
rsa_pkey = _lib.EVP_PKEY_get1_RSA(pk._pkey)

result_code = _lib.PEM_write_bio_RSAPublicKey(bio_pub, rsa_pkey)
result_code = _lib.PEM_write_bio_RSAPrivateKey(
    bio_priv, rsa_pkey, _ffi.NULL, _ffi.NULL, 0,
    helper.callback, helper.callback_args)
