class Predicates(object):
    def getReverseDictionary(self):
        dict = {}
        dict['hasCollectionMember'] = 'isMemberOfCollection'
        dict['isMemberOfCollection'] = 'hasCollectionMember'
        dict['isMemberOf'] = 'hasMember'
        dict['hasMember'] = 'isMemberOf'
        dict['isDerivationOf'] = 'hasDerivation'
        dict['hasDerivation'] = 'isDerivationOf'
        dict['isPartOf'] = 'hasPart'
        dict['hasPart'] = 'isPartOf'
        return dict
