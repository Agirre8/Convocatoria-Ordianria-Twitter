from datetime import datetime


class UserAccount:
    def __init__(self, alias, email):
        #alias y email son tipo string
        self.alias = alias
        self.email = email

        #creo 3 listas para almacenar los objetos
        self.tweets = []
        self.followers = []
        self.timeline = []
    
    #metodo para añadir follower a la lista followers
    def add_follower(self, follower):

        self.followers.append(follower)
       
    #metodo para que el usuario actual se agregue como seguidor del usuario user2.       
    def follow (self, user2):

        user2.add_follower(self)

    #metodo para recivir un tweet y guardarlo en la lista del usuario
    def receive_tweet(self, tweet):

        self.timeline.append(tweet)

    #metodo para publicar un tweet, ademas implementando que en caso de que el user que ha publicado el tweet tenga seguidores, ellos tambien agregen el tweet a su lista de tweets
    def tweet(self, tweet1):
 
        self.tweets.append(tweet1)
        
        for follower in self.followers:
            follower.receive_tweet(tweet1)
            

