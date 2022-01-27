from cryptography import x509
from cryptography.x509.oid import ExtensionOID

target = b'-----BEGIN CERTIFICATE-----\nMIICujCCAkCgAwIBAgIUAIhXdZ2EeJv1iw/cb7+jZ6sI1QQwCgYIKoZIzj0EAwMw\nKjEVMBMGA1UEChMMc2lnc3RvcmUuZGV2MREwDwYDVQQDEwhzaWdzdG9yZTAeFw0y\nMTEwMjcxNjUxNDRaFw0yMTEwMjcxNzExNDNaMAAwWTATBgcqhkjOPQIBBggqhkjO\nPQMBBwNCAAS0CPMDckvwLCuCUkdDc7L1ojKEMdpUfwDPTO5803Q5MF7A60dXYfiq\nJ0pW9d7ifp/4RJh+1t2ngk0lix0I2TGCo4IBbDCCAWgwDgYDVR0PAQH/BAQDAgeA\nMBMGA1UdJQQMMAoGCCsGAQUFBwMDMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFJFH\nsX99GGgejd20Do773tJaMjl+MB8GA1UdIwQYMBaAFMjFHQBBmiQpMlEk6w2uSu1K\nBtPsMIGNBggrBgEFBQcBAQSBgDB+MHwGCCsGAQUFBzAChnBodHRwOi8vcHJpdmF0\nZWNhLWNvbnRlbnQtNjAzZmU3ZTctMDAwMC0yMjI3LWJmNzUtZjRmNWU4MGQyOTU0\nLnN0b3JhZ2UuZ29vZ2xlYXBpcy5jb20vY2EzNmExZTk2MjQyYjlmY2IxNDYvY2Eu\nY3J0MDgGA1UdEQEB/wQuMCyBKmtleWxlc3NAZGlzdHJvbGVzcy5pYW0uZ3NlcnZp\nY2VhY2NvdW50LmNvbTApBgorBgEEAYO/MAEBBBtodHRwczovL2FjY291bnRzLmdv\nb2dsZS5jb20wCgYIKoZIzj0EAwMDaAAwZQIxAOr4Zm779AqybxokbAh76ImxySWT\nAyeatiUNpKxhDvw3VcIYemw4zShmIwKmXAG6BgIwI8exlz9FURYVRjenIPekwqRF\nHisnC8AGqh+NR8ZFLAHSL7COEjZH+moBMXIFpz+I\n-----END CERTIFICATE-----\n'

cert = x509.load_pem_x509_certificate(target)
email = cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value.get_values_for_type(x509.RFC822Name)[0]
print(len(cert.extensions.get_extension_for_oid(ExtensionOID.SUBJECT_ALTERNATIVE_NAME).value))
provider_oid = x509.ObjectIdentifier("1.3.6.1.4.1.57264.1.1")
oicd = cert.extensions.get_extension_for_oid(provider_oid).value.value.decode("utf-8")
print("{} via {}".format(email, oicd))