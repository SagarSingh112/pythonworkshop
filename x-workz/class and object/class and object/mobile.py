class mobile:

    def callings(self):
        print("iNVOKING CALLING FUNCTION")

    def sms(self):
        print("invoking sms method")

    def games(self):
        print("invoking games")

class One_plus(mobile):

    def cam(self):
        print("invoking cam method")

    def music(self):
        print("invoking music method")

    def video_call(self):
        print("invoking video call method")


Oneplus=One_plus()
Oneplus.video_call()

mobile=mobile()
mobile.games()
