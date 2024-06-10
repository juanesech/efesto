import os
import atlassian
from utils.logger import log


class ConfluenceDS:
    def __init__(self, url="https://confluence.com", token="", username=""):
        self.url = os.getenv("CONFLUENCE_URL") or url
        if self.url is None or self.url == "":
            raise ValueError("CONFLUENCE_URL is not set")
        self.token = os.getenv("CONFLUENCE_TOKEN") or token
        if self.token is None or self.token == "":
            raise ValueError("CONFLUENCE_TOKEN is not set")
        self.username = os.getenv("CONFLUENCE_USERNAME") or username
        if self.username is None or self.username == "":
            raise ValueError("CONFLUENCE_USERNAME is not set")
        self.confluence = atlassian.Confluence(
            username=self.username,
            url=self.url,
            password=self.token,
        )

    def get_page(self, page_id):
        """
        Retrieves a Confluence page by its ID.

        Args:
            page_id (int): The ID of the Confluence page.

        Returns:
            dict: A dictionary representing the Confluence page, including its body.

        Raises:
            atlassian.confluence.ApiError: If an error occurs while retrieving the page.
        """  # noqa: E501
        try:
            return self.confluence.get_page_by_id(page_id, expand="body")
        except atlassian.confluence.ApiError as e:
            raise e

    def update_page(self, page_id, title, content, labels=[]):
        """
        Updates a Confluence page with the given page ID, title, content, and labels.

        Args:
            page_id (int): The ID of the Confluence page to update.
            title (str): The new title for the page.
            content (str): The new content for the page.
            labels (List[str], optional): A list of labels to add to the page. Defaults to an empty list.

        Raises:
            atlassian.confluence.ApiError: If an error occurs while updating the page or retrieving the page labels.

        Returns:
            None
        """  # noqa: E501
        try:
            self.confluence.update_page(
                page_id=page_id,
                title=title,
                body=content,
                representation='storage',
            )
            curr_labels = self.confluence.get_page_labels(page_id)
            log.debug("CURRENT LABELS: {}".format(curr_labels))
            existing_label_names = [label['name']
                                    for label in curr_labels['results']]

            labels_to_add = [
                label for label in labels if label not in existing_label_names]

            for label in labels_to_add:
                self.confluence.set_page_label(page_id, label)
            else:
                log.info("No new labels to add")
        except atlassian.confluence.ApiError as e:
            raise e
