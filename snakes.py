class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    
    def bite(self, other):
        venom = 'super poison'
        print(venom)
        """Deliver a dose of venom."""
        pass

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        pass

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    pass
