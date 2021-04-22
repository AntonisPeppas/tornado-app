from pyroaring import BitMap


class UserTags:
    TAGS = {
        "tag1": 1,
        "tag2": 2,
        "tag3": 3,
        "tag4": 4,
        "tag5": 5,
        "tag6": 6,
        "tag7": 7,
        "tag8": 8,
        "tag9": 9,
        "tag10": 10
    }

    def __init__(self, user_tags):
        self.user_tags = user_tags
    
    def add(self, user_id, tag_id):
        if tag_id not in range(1, 11):
            return "Not a valid tag"
        try:
            self.user_tags[user_id].add(tag_id)
        except:
            self.user_tags[user_id] = BitMap([tag_id])
        print(self.user_tags)

    def get(self, user_id):
        try:
            return self.user_tags[user_id]
        except:
            return "No tags for this user"

    def delete(self, user_id, tag_id):
        try:
            self.user_tags[user_name].remove(tag_id)
            return "Tag removed"
        except:
            return "Tag does not exist"

    def get_users_for_tags(self):
        counter = 0
        tags = BitMap([1, 2])
        for user in self.user_tags:
            if tags.issubset(self.user_tags[user]):
                counter += 1
        return counter

    def get_users_with_tag1(self):
        tag1 = BitMap([1])
        users = []
        for user in self.user_tags:
            if tag1.issubset(self.user_tags[user]):
                users.append(user)
        return users
        