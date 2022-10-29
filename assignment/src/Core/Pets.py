from assignment.src.Utilities.genericUtilities import *
import random



class Pets(object):

    def __init__(self, **kwargs):

        self.id = None
        self.cateogry = {'id': random.randint(1, 1000),
                         'name': category_pets() if 'name' not in kwargs else kwargs['name']}
        self.name = generate_first_names()
        self.photoUrls = ["randomurls.com"]
        self.tags = []
        self.id = random.randint(1, 1000)
        self.name = generate_last_names()
        dict ={
            'id': self.id,
            'name': self.name
        }
        self.tags.append(dict)
        self.status = "available"


