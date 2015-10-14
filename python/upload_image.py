from facepy import GraphAPI

# Initialize the Graph API with a valid access token (optional,
# but will allow you to do all sorts of fun stuff).
oauth_access_token = "CAACEdEose0cBALwZBiv5QymZB3XO3UwyTHv55lYNItEnkpB0ZALRsZCkPNPMs9hqf8jaL8AsQOnEnDljKFThmD3BHyvJcN4B1uqZAZA46KS2occPPMTHNkZCGxTpiuhVZChvJuT9rsmJ9P2R1yc5aIFxHO7DSnGvHRbP9x0JA0GlifnmwAY6Yh29jVExma5K2XOZAD9jjDOZApJAZDZD"
graph = GraphAPI(oauth_access_token)

# Get my latest posts
graph.get('me/posts')

# Post a photo of a parrot
graph.post(
    path = '960793297302151/photos',
    source = open('parrot.jpg', 'rb'),
    message = "bbbbbbbbbbb"
)
