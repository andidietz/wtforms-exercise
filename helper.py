def query_all(cls):
    """ Queries database and returns all items in table """

    return cls.query.all()

def query_by_id(cls, pet_id):
    """ Queries database and return item by id """
    
    return cls.query.get_or_404(pet_id)