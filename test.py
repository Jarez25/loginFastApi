from controller.user import User

data = {
  "firstname" : "Jenebith",
  "lastname" : "Davila",
  "username" : "Juvel",
  "country" : "Nic",
  "password_user" : "31331",
}


user = User(data)
user.create_user()