class ProgrammingLanguage:


    def __int__(self,name="",Typing="", Year=0):
        self.name=name
        self.Typing=Typing
        self.Year=Year



    def __str__(self):
        return("{},{} Typing,First appeared in {}".format(self.name, str(self.Typing), str(self.Year)))