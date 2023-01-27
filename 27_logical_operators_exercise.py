is_magician = True  # tells about user profile
is_expert = True  # is the user expert?

# 1.check if magician and expert: "you are a master magician"

# 2.check if magician but not expert: "at least you're getting there"

# 3.if you're not a magician: "you need magic powers"

# 1.
if is_magician and is_expert:
    print("you are a master magician")

# 2.
elif is_magician and not is_expert:
    print("at least you are getting there")

# 3.
elif not is_magician:
    print("you need magic powers")
