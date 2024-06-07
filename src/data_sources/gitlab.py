import gitlab
import os


gitlab_url = os.getenv("GITLAB_URL") or "https://gitlab.com"
gitlab_token = os.getenv("GITLAB_TOKEN")
if gitlab_token is None:
    raise ValueError("GITLAB_TOKEN is not set")


glab = gitlab.Gitlab(gitlab_url, gitlab_token)


def get_subgroups(group_id):
    """
    Retrieves all subgroups of a given GitLab group.

    Args:
        group_id (int): The ID of the GitLab group.

    Returns:
        list: A list of GitLab subgroup objects.

    Raises:
        gitlab.GitlabListError: If an error occurs while retrieving subgroups.If an error occurs while retrieving the subgroups.

    """  # noqa: E501
    try:
        return glab.groups.get(group_id).subgroups.list(
            get_all=True, include_subgroups=True)
    except gitlab.GitlabListError as e:
        raise e


def get_group_owners(group_id):
    """
    Retrieves the owners of a GitLab group.

    Args:
        group_id (int): The ID of the GitLab group.

    Returns:
        list: A list of GitLab member objects representing the owners of the group.

    """  # noqa: E501
    owners = []
    group_members = glab.groups.get(group_id).members.list()
    for member in group_members:
        if member.access_level == 50:
            owners.append(member)
    return owners


def get_projects_by_group(group_id):
    """
    Retrieves the owners of a GitLab group.

    Args:
        group_id (int): The ID of the GitLab group.

    Returns:
        list: A list of GitLab member objects representing the owners of the group.

    """  # noqa: E501
    projects = []
    try:
        subgroup_projects = glab.groups.get(
            group_id).projects.list(get_all=True)
        for project in subgroup_projects:
            projects.append(glab.projects.get(project.id))
    except gitlab.GitlabListError as e:
        raise e
    return projects
