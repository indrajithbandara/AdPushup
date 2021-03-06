import numpy as np

class EpsilonGreedy(object):
    
    def __init__(self, n_ads, epsilon_decay=.999, epsilon=0.1):
        self.hits = [1] * n_ads # example: total number of hits
        self.views = [1.] * n_ads # example: total number of views
        self.values = [1.] * n_ads # example: hits / views
        self.decay = epsilon_decay
        self.epsilon = epsilon
        self.n = n_ads
    
    def set_views(self, views):
        self.views = views
    
    def set_values(self, values):
        self.values = values
    
    def set_hits(self, hits):
        self.hits = hits
    
    def get_views(self):
        return self.views
    
    def get_values(self):
        return self.values
    
    def get_hits(self):
        return self.hits
    
    def recommend_ad(self):
        """Recommends ads"""
        epsilon = self.epsilon

        if np.random.random() > epsilon:
            # Exploit best ad
            index_ad = np.argmax(self.values)

        else:
            # Explore ( test other ads )
            index_ad = np.random.randint(self.n - 1)
        
        self.update(index_ad, 1)
        
        return index_ad
            
        
    def update(self, ad, reward):
        """Update an ad with some reward""" # Example: click = 1; no click = 0
        
        # update hit stats
        if reward == 1:
            self.hits[ad] = self.hits[ad] + 1
        hit = self.hits[ad]
        
        # update views stat
        self.views[ad] = self.views[ad] + 1
        view = self.views[ad]
        
        # recalculate hit / views ratio
        new_value = (hit) / float(view)
        
        # after each view decrease the value of epsilon by using epsilon = epsilon * decay
        self.epsilon = self.epsilon * ( self.decay )
        
        self.values[ad] = new_value