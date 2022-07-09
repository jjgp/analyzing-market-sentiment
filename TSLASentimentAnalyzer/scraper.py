import praw
from config import settings
from loguru import logger
from praw.models import MoreComments


class RedditScraper:
    def __init__(self, subreddit: str = "TSLA"):
        reddit = praw.Reddit(
            client_id=settings.reddit_api_client_id,
            client_secret=settings.reddit_api_client_secret,
            user_agent=settings.reddit_api_user_agent,
        )
        self.subreddit = reddit.subreddit(subreddit)

    def get_hot(self, posts: int = 10):
        return self.subreddit.hot(limit=posts)

    def get_new(self, posts: int = 10):
        return self.subreddit.new(limit=posts)

    def get_rising(self, posts: int = 10):
        return self.subreddit.rising(limit=posts)

    def get_top(self, posts: int = 10):
        return self.subreddit.top(limit=posts)

    def get_top_comments(self, submission, threshold: int = 5):
        return [
            comment.body
            for comment in submission.comments
            if comment.score >= threshold
        ]

    def get_comment_forest(self, comment_forest, all_comments=[]):
        all_comments = []
        if isinstance(comment_forest, MoreComments):
            comments_list = comment_forest.comments()
        else:
            comments_list = comment_forest.list()
        logger.debug(str(comment_forest), len(comments_list))
        for comment in comments_list:
            if isinstance(comment, MoreComments):
                logger.info("more comments")
                logger.debug(self.get_comment_forest(comment))
                continue
            item = {}
            item["comment"] = comment.body
            item["title"] = comment.submission.title
            item["id"] = comment.id
            item["created_at"] = int(comment.created_utc)
            item["score"] = comment.score
            all_comments.append(item)
        return all_comments
        if comment_forest.list():
            for reply in comment_forest:
                all_comments.append(reply)
            return self.get_comment_forest(reply.replies, all_comments)
        return all_comments
