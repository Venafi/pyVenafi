class Identity:
    def __init__(self, identity_dict, api_type):
        """
        :type identity_dict: dict
        :type api_type: str
        """
        if api_type.lower() == 'websdk':
            self.FullName = identity_dict.get('FullName')
            self.IsContainer = identity_dict.get('IsContainer')
            self.IsGroup = identity_dict.get('IsGroup')
            self.Name = identity_dict.get('Name')
            self.Prefix = identity_dict.get('Prefix')
            self.PrefixedName = identity_dict.get('PrefixedName')
            self.PrefixedUniversal = identity_dict.get('PrefixedUniversal')
            self.Universal = identity_dict.get('Universal')

        elif api_type.lower() == 'aperture':
            # Not implemented yet.
            pass
