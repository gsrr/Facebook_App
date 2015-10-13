from facepy import GraphAPI

# Initialize the Graph API with a valid access token (optional,
# but will allow you to do all sorts of fun stuff).
oauth_access_token = "CAAMBhAmeu5oBAK9n7bhbwZBpjHwWIQZAQ9hPL8KzhKS2iqG8XZC2YoEiAM5cj7yzPITxA7RHZAEF0UkZBVruzYgzyh60BxQl0PhlgH0iY2oyrp0itwFjROavmgHkTiFZBwQapZB7vRv2I1OfsvJ84GWGbhvMPe3h6axNAKcEiVjYZC5SRvuZAmyV6XYBFjrDH8yLsMLWeaZBZCDBVSKfQj7e4tC"
graph = GraphAPI(oauth_access_token)

# Get my latest posts
graph.get('me/posts')

# Post a photo of a parrot
graph.post(
    path = '960793297302151/photos',
    source = open('parrot.jpg', 'rb'),
    message = "bbbbbbbbbbb"
)