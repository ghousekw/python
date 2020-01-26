import graphene
import json
from datetime import datetime

# creating a user class
class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

class Query(graphene.ObjectType):
    # creating a list to display all users
    # we can also set limit to display number of users like graphene.List(User, limit=graphene.int())
    users = graphene.List(User, limit=graphene.int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"
    
    def resolve_is_admin(sef, info):
        return True

    # define a function for users
    def resolve_users(self, info, limit):
        return [
            # creating users with current datetime stamp
            User(id="1", username="Fred", created_at=datetime.now()),
            User(id="2", username="Douglas", created_at=datetime.now()),
        ][:limit]
schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        # we've to use dictionary to display all fields otherwise attribute error
        # will rise
        users(limit: 1) {
            id
            username
            createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))