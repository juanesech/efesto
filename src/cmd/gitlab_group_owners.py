from data_sources import gitlab
from data_sources import confluence
import utils
from utils.logger import log


def get_group_owners(gitlab_group_id, confluence_page_id):
    """
    Retrieves the owners of all subgroups within a given GitLab group and updates the content of a Confluence page with the list of subgroups and their owners.

    Args:
        gitlab_group_id (int): The ID of the GitLab group.
        confluence_page_id (int): The ID of the Confluence page.

    Returns:
        None

    Raises:
        None

    Steps:
        1. Retrieves the Confluence page using the provided `confluence_page_id`.
        2. Retrieves all subgroups of the GitLab group specified by `gitlab_group_id`.
        3. For each subgroup, retrieves its owners and appends a list with the subgroup path and the owner names to `table_data`.
        4. Creates an HTML table with the headers "Group name" and "Owner" using the `table_data`.
        5. Updates the content of the Confluence page with the new table markup.

    """  # noqa: E501
    glab = gitlab.GitlabDS()
    confl = confluence.ConfluenceDS()
    page = confl.get_page(confluence_page_id)
    gitlab_groups = glab.get_subgroups(gitlab_group_id)
    table_data = []
    log.info("Retrieving group {} owners".format(gitlab_group_id))
    for group in gitlab_groups:
        if len(glab.get_subgroups(group.id)) > 0:
            for subgroup in glab.get_subgroups(group.id):
                log.debug("SUBGROUP PATH: {}".format(subgroup.path))
                gr_owners = glab.get_group_owners(subgroup.id)
                table_data.append([subgroup.full_path, ', '.join(
                    [gowner.name for gowner in gr_owners])])
        else:
            gr_owners = glab.get_group_owners(group.id)
            log.debug(group.full_path, gr_owners)
            log.debug("SUBGROUP PATH: {}".format(group.path))
            table_data.append([group.path, ', '.join(
                [gowner.name for gowner in gr_owners])])

    table_markup = utils.html.create_table(["Group name", "Owner"], table_data)
    log.debug(table_markup)
    updated_content = table_markup
    log.info("Updating confluence page content")
    confl.update_page(confluence_page_id, page['title'], updated_content)
