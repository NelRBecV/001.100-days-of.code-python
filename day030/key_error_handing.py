#eval() function create a list of dictionary using that looks like this (see data in line 5)
facebook_posts = eval(input())

# data introduced to build the list
# {"Likes": 21, "Coments":2}, {"Likes": 13, "Coments":2, "Shares": 2}, {"Likes": 33, "Coments":8, "Shares": 2}, {"Coments":2, "Shares": 2}, {"Coments":2, "Shares": 1}, {"Likes": 19, "Coments":3}

total_likes: int = 0
likes: int = 0

#TODO: Catch th error exception
print(type(facebook_posts))
print(facebook_posts)

for post in facebook_posts:
    try:
        likes = post['Likes']
    except KeyError:
        total_likes +=0
    else:
        total_likes = total_likes + likes

print(total_likes)
