import inspect
import uuid


def tag(guid: str, owner: str = None, features: list = None):
    def decorate(cls_or_meth):
        if inspect.ismethod(cls_or_meth) or inspect.isfunction(cls_or_meth):
            setattr(cls_or_meth, 'guid', guid)
        setattr(cls_or_meth, 'owner', owner)
        setattr(cls_or_meth, 'features', features)
        return cls_or_meth
    return decorate


class Owner:
    spi = 0


class Features:
    class Certificates:
        certificate_renewal = 0

    class Interface:
        websdk = 100
        aperture = 101

    class Applications:
        apache = 200
        pkcs11 = 201
        association = 202
        one_to_many = 203


# @tag(guid='q1w34q234',
#      owner=Owner.spi,
#      features=[
#          Features.Certificates.certificate_renewal,
#          Features.Interface.websdk,
#          Features.Applications.apache
#      ])
# def test():
#     pass
