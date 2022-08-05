from pytpp.properties.response_objects.dataclasses._base import PayloadModel, PayloadField


class Self(PayloadModel):
    href: str = PayloadField(alias='Href')


class Link(PayloadModel):
    self: Self = PayloadField(alias='Self')


class Engine(PayloadModel):
    links: Link = PayloadField(alias='_links')
    engine_dn: str = PayloadField(alias='EngineDn')
    engine_guid: str = PayloadField(alias='EngineGuid')
    engine_name: str = PayloadField(alias='EngineName')


class Folder(PayloadModel):
    folder_dn: str = PayloadField(alias='FolderDN')
    folder_guid: str = PayloadField(alias='FolderGuid')
    folder_name: str = PayloadField(alias='FolderName')
