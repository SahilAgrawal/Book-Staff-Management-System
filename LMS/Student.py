class Student:
    def __init__(self,name,branch,adm_year,s_id,adm_id):
        self.name=name
        self.branch=branch
        self.adm_year=adm_year
        self.adm_id=adm_id
        self.s_id=s_id
        self.book={}    
    def display(self):
        print(f"\t{self.name}\t{self.branch}\t{self.s_id}\t{self.adm_year}\t{self.book}")
        
    
