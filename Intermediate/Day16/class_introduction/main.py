from user import User
from post import Post

app_user_one = User("rb@rb.com", "Richard B", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("cb@cb.com", "Chloe B", "supersecretmeatballs", "Financial Advisor")
app_user_two.get_user_info()

new_post = Post("On a secret mission today\n -", app_user_two.name)
new_post.get_post_info()