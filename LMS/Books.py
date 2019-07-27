class Books:
    def __init__(self,name,publication,isbn,year,copies):
        self.name=name
        self.publication=publication
        self.isbn=isbn
        self.year=year
        self.copies=copies
    def display(self):
        print(f"\t{self.name}\t{self.publication}\t{self.year}\t{self.isbn}\t{self.copies}")
        
