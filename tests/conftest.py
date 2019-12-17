import pytest
from faker import Faker
from starlette.testclient import TestClient

from main import app

fake = Faker()


@pytest.fixture
def client():
    return TestClient(app)


def make_person():
    return {
        "login": fake.name(),
        "id": fake.pyint(max_value=9999999),
        "node_id": fake.sha1(),
        "avatar_url": fake.uri(),
        "gravatar_id": fake.sha1(),
        "url": fake.uri(),
        "html_url": fake.uri(),
        "followers_url": fake.uri(),
        "following_url": fake.uri(),
        "gists_url": fake.uri(),
        "starred_url": fake.uri(),
        "subscriptions_url": fake.uri(),
        "organizations_url": fake.uri(),
        "repos_url": fake.uri(),
        "events_url": fake.uri(),
        "received_events_url": fake.uri(),
        "type": "User",
        "site_admin": fake.pybool()
    }


@pytest.fixture
def release_body():
    return {
        "action": "edited",
        "changes": {
            "body": {
                "from": fake.text(max_nb_chars=255)
            }
        },
        "release": {
            "url": fake.uri(),
            "assets_url": fake.uri(),
            "upload_url": fake.uri(),
            "html_url": fake.uri(),
            "id": fake.pyint(max_value=9999999),
            "node_id": fake.sha1(),
            "tag_name": fake.word(),
            "target_commitish": fake.word(),
            "name": fake.sentence(),
            "draft": fake.pybool(),
            "author": make_person(),
            "prerelease": fake.pybool(),
            "created_at": fake.iso8601(),
            "published_at": fake.iso8601(),
            "assets": [],
            "tarball_url": fake.uri(),
            "zipball_url": fake.uri(),
            "body": fake.text(max_nb_chars=255)
        },
        "repository": {
            "id": fake.pyint(max_value=9999999),
            "node_id": fake.sha1(),
            "name": fake.sentence(),
            "full_name": fake.sentence(),
            "private": fake.pybool(),
            "owner": make_person(),
            "html_url": fake.uri(),
            "description": fake.text(max_nb_chars=255),
            "fork": fake.pybool(),
            "url": fake.uri(),
            "forks_url": fake.uri(),
            "keys_url": fake.uri(),
            "collaborators_url": fake.uri(),
            "teams_url": fake.uri(),
            "hooks_url": fake.uri(),
            "issue_events_url": fake.uri(),
            "events_url": fake.uri(),
            "assignees_url": fake.uri(),
            "branches_url": fake.uri(),
            "tags_url": fake.uri(),
            "blobs_url": fake.uri(),
            "git_tags_url": fake.uri(),
            "git_refs_url": fake.uri(),
            "trees_url": fake.uri(),
            "statuses_url": fake.uri(),
            "languages_url": fake.uri(),
            "stargazers_url": fake.uri(),
            "contributors_url": fake.uri(),
            "subscribers_url": fake.uri(),
            "subscription_url": fake.uri(),
            "commits_url": fake.uri(),
            "git_commits_url": fake.uri(),
            "comments_url": fake.uri(),
            "issue_comment_url": fake.uri(),
            "contents_url": fake.uri(),
            "compare_url": fake.uri(),
            "merges_url": fake.uri(),
            "archive_url": fake.uri(),
            "downloads_url": fake.uri(),
            "issues_url": fake.uri(),
            "pulls_url": fake.uri(),
            "milestones_url": fake.uri(),
            "notifications_url": fake.uri(),
            "labels_url": fake.uri(),
            "releases_url": fake.uri(),
            "deployments_url": fake.uri(),
            "created_at": fake.iso8601(),
            "updated_at": fake.iso8601(),
            "pushed_at": fake.iso8601(),
            "git_url": fake.uri(),
            "ssh_url": fake.uri(),
            "clone_url": fake.uri(),
            "svn_url": fake.uri(),
            "homepage": fake.uri(),
            "size": 0,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "None",
            "has_issues": fake.pybool(),
            "has_projects": fake.pybool(),
            "has_downloads": fake.pybool(),
            "has_wiki": fake.pybool(),
            "has_pages": fake.pybool(),
            "forks_count": 0,
            "mirror_url": fake.uri(),
            "archived": fake.pybool(),
            "disabled": fake.pybool(),
            "open_issues_count": 0,
            "license": "None",
            "forks": 0,
            "open_issues": 0,
            "watchers": 0,
            "default_branch": "master"
        },
        "sender": make_person()
    }


@pytest.fixture
def deploy_body():
    return {
        'project_name': fake.sentence(),
        'tag': fake.word()
    }
