from datetime import datetime

class UserAccount:
    def __init__(self, alias, email):
        #alias y email son tipo string
        self.alias = alias
        self.email = email

        #creo 3 listas para almacenar los objetos
        self.tweets = []
        self.followers = []
        #lista que almacena los tweets de las cuentas que sigue el usuario
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
        if isinstance(tweet1, Tweet):
            self.tweets.append(tweet1)
        elif isinstance(tweet1, Retweet):
            self.tweets.append(tweet1.to_tweet())
        else:
            raise ValueError("El objeto no es un tweet válido.")
        
        for follower in self.followers:
            follower.receive_tweet(tweet1)
    
class Tweet:

    max_characters = 140
    def __init__(self, message, sender):
        #en caso de que el tweet contenga mas de 140 caracteres saltara una excepcion
        if len(message) > self.max_characters:
            raise ValueError("El mensaje excede el límite de caracteres permitidos.")
        self.message = message
        self.sender = sender
        self.time = datetime.now()

    def __str__(self):
        return f"El Tweet lo manda:{self.sender} \nFecha del Tweet: {self.time} \nEl tweet es: {self.message}"


class Retweet(Tweet):

    def __init__(self, message, sender, original_tweet):
        super().__init__(message, sender)
        self.original_tweet = original_tweet

    
    def to_tweet(self):
        return Tweet(self.message, self.sender)

    def __str__(self):
        return f"El Tweet lo manda:{self.sender} \nFecha del Tweet: {self.time} \nEl tweet es: {self.message} \n El tweet original: {self.original_tweet}"


class DirectMessage(Tweet):

    def __init__(self, message, sender, receiver):
        super().__init__(message, sender)
        self.receiver = receiver

    def __str__(self):
        return f"El Tweet lo manda:{self.sender} \nEl receptor es: {self.receiver}\nFecha del Tweet: {self.time} \nEl tweet es: {self.message}"


"""¿Deberá modificar los atributos timeline y tweets de la clase UserAccount
(definida en el ejercicio 1) para que contenga elementos de la clase hija
Retweet? Justifique su razonamiento y, si cree que hay que modificarlos, explique
también cómo lo haría.

RESPUESTA:
Como listas listas timeline y tweets son distintas separado, para permitir que contengan tanto 
objetos de la clase Tweet como objetos de la clase Retweet. Por lo que al recivir un Retweet
tengo que  convertirlo en un objeto de la clase Tweet antes de agregarlo a las listas. Para eso creo un metodo 
to_tweet en la clase Retweet para llamarlo despues en la clase UserAccount
        """