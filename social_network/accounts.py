
class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []
    

    def add_post(self, post):
        post.set_user(self) #self = Anders
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for user in self.following:
            #timeline.append(user.post)
            timeline += user.posts
        return sorted(timeline, key=lambda timeline: timeline.timestamp)
            

#return '{class}: post{num}'.format(class=self.__class__.__name__, post=)
        
    def follow(self, other):
        self.following.append(other) #anders is user, appending instance of michael to following list

    
#"john.follow(paul)
#print(john.following)
#>>> [<User: "Paul McCartney">]"
