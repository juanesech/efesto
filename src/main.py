import click
from cmd.gitlab_group_owners import get_group_owners
from cmd.gitlab_terraform_modules import get_terraform_modules


@click.group()
def cli():
    pass


@click.command()
@click.option('--gitlab-group-id',  help='GitLab group ID', required=True)
@click.option(
    '--confluence-page-id',
    help='Confluence page ID',
    required=True
)
def gitlab_group_owners(gitlab_group_id, confluence_page_id):
    """
    Retrieves the owners of a GitLab group and updating a Confluence page with the list of subgroups and their owners.

    Parameters:
        gitlab_group_id (str): The ID of the GitLab group.
        confluence_page_id (str): The ID of the Confluence page.

    Returns:
        None
    """  # noqa: E501
    get_group_owners(gitlab_group_id, confluence_page_id)


@click.command()
@click.option('--gitlab-group-id',  help='GitLab group ID', default="87762141")
@click.option(
    '--confluence-page-id',
    help='Confluence page ID',
    required=True
)
def terraform_modules_versions(gitlab_group_id, confluence_page_id):
    """
    Retrieves the Terraform modules from a GitLab group and updating a Confluence page with the list of modules and their latest versions.

    Parameters:
        gitlab_group_id (str): The ID of the GitLab group. Defaults to "87762141".
        confluence_page_id (str): The ID of the Confluence page.

    Returns:
        None
    """  # noqa: E501
    get_terraform_modules(gitlab_group_id, confluence_page_id)


cli.add_command(gitlab_group_owners)
cli.add_command(terraform_modules_versions)

if __name__ == '__main__':
    cli(obj={})
