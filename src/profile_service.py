class ProfileService:
    # Boolean missing is/has/can prefix.
    loading = False

    # Function name should be snake_case; missing type hints and docstring; mutable
    # default argument.
    def FetchProfile(self, user_id, tags=[]):
        tags.append("fetched")
        return Profile(user_id, tags)