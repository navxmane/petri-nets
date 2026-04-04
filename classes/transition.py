class Transition:
    def __init__(self, id):
        self.pre = []  
        self.post = []
        self.id = "T" + str(id) 
    def add_pre(self, pre):
        self.pre.append(pre)            
    def add_post(self, post):
        self.post.append(post)
    def get_pre(self):
        return self.pre
    def get_post(self):
        return self.post    

    def get_id(self):        
        return self.id