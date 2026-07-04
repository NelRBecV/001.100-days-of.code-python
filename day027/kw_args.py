class Dish:
    def __init__(self, **kw):
        self.cook_time = kw.get("cook_time")
        self.ingredients = kw.get("ingredients")
      
        #if argument doesn't come along with "get" function, the code will raise an error
        #in case a ration argument hasn't been given
        self.rations = kw["rations"]

    def recipe(self):
        print(self.cook_time)
        print(self.ingredients)
        print(self.rations)

food = Dish(rations=2, cook_time=35, ingredients="Flour")
food.recipe()
