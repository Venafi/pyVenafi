class SecretStoreVaultTypes:
    vault_types = {
          0: 'None',
          1: 'Private Key (obsolete, use Vault Type 256, PKCS#8)',
          2: 'Certificate',
          4: 'PKCS#12',
          8: 'Symmetric Key',
         16: 'State (Obsolete)',
         32: 'Password',
         64: 'CSR (obsolete, use Vault Type 512, PKCS#10)',
        128: 'Blob',
        256: 'PKCS#8',
        512: 'PKCS#10',
        1024: 'File',
        2048: 'RSA Public Key (obsolete, use Vault Type 4096, Public Key)',
        4096: 'Public Key',
        1073741826: 'Archived Certificate',
        1073741828: 'Archived PKCS#12',
        1073741832: 'Archived Symmetric Key',
        1073741840: 'Archived State (Obsolete)',
        1073741856: 'Archived Password',
        1073741952: 'Archived Blob',
        1073742080: 'Archived PKCS#8',
        1073742336: 'Archived PKCS#10',
        1073742848: 'Archived File',
        1073743872: 'Archived RSA Public Key (obsolete, use Vault Type 1073745920, Archived Public Key)',
        1073745920: 'Archived Public Key'
    }


class Namespaces:
    config = 'config'
