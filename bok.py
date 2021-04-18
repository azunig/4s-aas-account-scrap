from boxsdk import OAuth2, Client

auth = OAuth2(
    client_id='46lbyt5j6n1xse3wzq3yzim8cacyvqnm',
    client_secret='XkYcpvjaMpDF7GUCg0vUq9znYb2N0qxU',
    access_token='vzpsJOJXeicchBehucQObdAr6Z8UcF7W',
)
client = Client(auth)

user = client.user().get()
print('The current user ID is {0}'.format(user.id))
