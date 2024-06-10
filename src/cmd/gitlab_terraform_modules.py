from data_sources import gitlab
from data_sources import confluence
from utils.objects import create_html_table
from utils.logger import log


def get_terraform_modules(gitlab_group_id, confluence_page_id):
    """
    Retrieves the Terraform modules from a GitLab group and updates the content of a Confluence page with the list of modules and their latest versions.

    Args:
        gitlab_group_id (int): The ID of the GitLab group.
        confluence_page_id (int): The ID of the Confluence page.

    Returns:
        None

    Raises:
        None

    Steps:
        1. Retrieves the Confluence page using the provided `confluence_page_id`.
        2. Retrieves the GitLab projects belonging to the group specified by `gitlab_group_id`.
        3. For each project, retrieves its tags and appends a list with the project name and the latest tag name to `table_data`.
        4. Sorts `table_data` by the project name.
        5. Creates an HTML table with the headers "Module" and "Latest version" using the sorted `table_data`.
        6. Updates the content of the Confluence page with the new table markup.

    """  # noqa: E501
    glab = gitlab.Gitlab()
    page = confluence.get_page(confluence_page_id)
    gitlab_projects = glab.get_projects_by_group(gitlab_group_id)
    table_data = []
    log.info("Retrieving group {} projects".format(gitlab_group_id))
    for project in gitlab_projects:
        log.debug("PROJECT PATH: {}".format(project.path_with_namespace))
        tags = project.tags.list(get_all=True)
        if len(tags) < 1:
            log.debug("Project {} has no tags".format(
                project.path_with_namespace))
            continue
        log.debug("Project tags: {}".format(tags))
        log.debug("Project latest tag: {}".format(tags[0].name))
        table_data.append([
            f"<a href=\"{project.web_url}\">{project.name}</a>",
            f"{tags[0].name}"])

    sorted_table_data = sorted(table_data, key=lambda x: x[0])
    table_markup = create_html_table(
        ["Module", "Latest version"], sorted_table_data)
    log.debug(table_markup)
    updated_content = table_markup
    log.info("Updating confluence page content")
    confluence.update_page(
        confluence_page_id, page['title'], updated_content)
