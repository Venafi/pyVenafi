from pytpp.attributes._helper import PropertyMeta, Attribute


class ProxyBaseAttributes(metaclass=PropertyMeta):
	bypass_proxy_on_local = Attribute('Bypass Proxy on Local')
	proxy_credential = Attribute('Proxy Credential')
	proxy_host = Attribute('Proxy Host')
	proxy_port = Attribute('Proxy Port')
	proxy_use_host_configuration = Attribute('Proxy Use Host Configuration')
