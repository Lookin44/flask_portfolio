from blog.models import User, Post


def get_all_posts():
    return Post.query.order_by(Post.date_posted.desc()).all()
