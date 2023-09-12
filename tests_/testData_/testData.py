
class UserCredentials():
    def __init__(self, login, password, name):
        self.login = login
        self.password = password
        self.name = name



validClientUser = UserCredentials("test_armenia_99@mail.ru", "anunazganun321", "Fname")
invalidClientUser = UserCredentials("john@gmail.com", "MyNameIsJohn", "John")



#URLS

homePageURL = "https://www.amazon.com"
signInURL = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Fhomepage.html%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
