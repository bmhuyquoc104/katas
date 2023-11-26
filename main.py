class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.published = False

    def publish(self):
        self._publish_success() if not self.published else self._publish_failure()

    def _publish_success(self):
        print(f"Publishing: {self.title}")
        self.published = True

    def _should_published(self) -> bool:
        return not self.published

    def _publish_failure(self):
        print(f"{self.title} is already published")

    def display_published_post(self):
        if self.published:
            print(f"{self.title}")


class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def display(self) -> None:
        print(f"Comment by {self.author}: {self.text}")


class ContentManagementSystem:
    def __init__(self):
        self.posts = list()
        self.comments = list()

    def add_post(self, post: Post):
        self.posts.append(post)

    def add_comment(self, comment: Comment):
        self.comments.append(comment)

    def display_posts(self):
        [post.display_published_post() for post in self.posts]

    def display_comments(self) -> None:
        [comment.display() for comment in self.comments]
