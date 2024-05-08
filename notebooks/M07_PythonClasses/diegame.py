import pandas as pd

class DieGame():
    """
    Just another Python class.
    """
    n_rolls = 10
    weights = [1,1,1,1,1,1]
    
    def __init__(self):
        return None
        
    def create_die(self):
        self.n_sides = len(self.weights)
        self.my_probs = [i/sum(self.weights) for i in self.weights]
        self.die = pd.DataFrame({
            'side': range(1, self.n_sides + 1),
            'weights': self.my_probs
        })
    
    def roll_die(self):
        results = []
        for i in range(self.n_rolls):
            result = self.die.side.sample(weights=self.die.weights).values[0]
            results.append(result)
        self.results = pd.Series(results)        
        
    def plot_results(self):
        prob_model = pd.Series({i+1:round(p, 2) for i, p in enumerate(self.my_probs)})
        print("Sides:", self.n_sides)
        print("Model:")
        print(prob_model)
        print("Rolls:", self.n_rolls)
        self.results.value_counts().sort_index().plot.bar(rot=0);
        
    # We add another method because it's so easy :-)
    def plot_probs(self):
        pd.Series(self.my_probs).plot.pie(title="Die Model")
        
    def do_it_all(self):
        self.create_die()
        self.roll_die()
        self.plot_results()

if __name__ == '__main__':
    
    # Run demo code of the file is called by itself
    game_1 = DieGame()
    game_1.n_rolls = 100
    game_1.do_it_all()