from Entity import Entity

class EntityRepository():
    entities_list = list() #TODO Verificar Performance de dicionarios
    #specimens_list = list() 
    @staticmethod
    def get_entities():
        return EntityRepository.entities_list
    #@staticmethod
    #def get_specimens():
    #    return EntityRepository.specimens_list
    @staticmethod
    def add_entitie(entity: Entity):
        EntityRepository.entities_list.append(entity)
    #    if Entity is Specimen:
    #        EntityRepository.specimens_list.append(entity)
    @staticmethod
    def remove_entitie(entity: Entity):
        EntityRepository.entities_list.remove(entity)
    #    if Entity is Specimen:
    #        EntityRepository.specimens_list.remove(entity)

class EntityCollider():
    pass