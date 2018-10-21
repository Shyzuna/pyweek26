class Resource(object):
    def __init__(self, position, size, category, amount):
        """
        Init a resource
        :param position:
        :param size:
        :param category:
        :param amount:
        """
        self.position = position
        self.size = size
        self.category = category
        self.amount = amount