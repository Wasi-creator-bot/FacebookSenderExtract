
from facebook import GraphAPI

# Replace with your own token
ACCESS_TOKEN = "EAAC…ZDZD"

# Initialize the Graph API client
graph = GraphAPI(access_token=ACCESS_TOKEN, version="12.0")

def get_profile(user_id):
    """
    Fetches a user profile object.
    Fields can be adjusted as needed.
    """
    fields = ["id", "name", "link", "picture.width(200).height(200)", "about", "location"]
    profile = graph.get_object(id=user_id, fields=",".join(fields))
    return profile

if __name__ == "__main__":
    user_ids = ["4", "zuck"]  # e.g. numeric ID or username
    for uid in user_ids:
        profile = get_profile(uid)
        print(profile)
