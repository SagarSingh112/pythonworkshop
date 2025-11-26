class adhar:
    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print({self.name},{self.aadhar_number},{self.dob},{self._finger_print},{self.__retina})


vars=adhar("sagar",00000000,"01-jan-2025","scanned","jyjyghfhfg")
vars.display_userData()
retena_vars=vars.getretena()
print(retena_vars)




