class Faculty:
    def __init__(self,name,f_id,year):
        self.name=name
        self.f_id=f_id
        self.year=year
        self.f_book={}
    def display(self):
        print(f"\t{self.name}\t{self.year}\t{self.f_id}\t{self.f_book}")
        
