class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # keep track of this owner's pets

    def pets(self):
        """Return all pets that belong to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Validate and add a Pet instance, link relationship both ways"""
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        self._pets.append(pet)
        pet.owner = self   # keep reverse link consistent

    def get_sorted_pets(self):
        """Return this owner's pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    # class-level attributes
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []  # stores all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # default to no owner yet
        Pet.all.append(self)

        if owner is not None:
            self.set_owner(owner)

    def set_owner(self, owner):
        """Assign this pet to an owner, ensuring relationship consistency"""
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")
        self.owner = owner
        if self not in owner.pets():
            owner.add_pet(self)
