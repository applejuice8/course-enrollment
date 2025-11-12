# Validate fields to be included in query parameters

# Request body (Client -> API) (Create, Update)
# Response body (API -> Client) (Update)

# By default, only return dictionaries
# If want to allow return both dictionaries and ORM objects, need to include this
'''
class Config:
    orm_mode = True
'''

# Update doesn't need id because id in path parameters
