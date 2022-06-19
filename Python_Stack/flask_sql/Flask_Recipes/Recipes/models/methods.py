from Recipes.models.users import User

class Method:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.isUnderThirty = data['underThirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = data['user']

