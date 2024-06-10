from typing import List


def create_table(header: List[str], data: List[List[str]]):
    """
    Creates an HTML table from a header and data.

    Args:
        header (List[str]): The header of the table.
        data (List[List[str]]): The data to populate the table with.

    Returns:
        str: The HTML table as a string.

    Example:
       >>> create_table(["Name", "Age"], [["John", "25"], ["Jane", "30"]])
        '<table><tr><th>Name</th><th>Age</th></tr><tr><td>John</td><td>25</td></tr><tr><td>Jane</td><td>30</td></tr></table>'
    """
    html_table = "<table>"
    for cell in header:
        html_table += f"<th>{cell}</th>"
    for row in data:
        html_table += "<tr>"
        for cell in row:
            html_table += f"<td>{cell}</td>"
        html_table += "</tr>"
    html_table += "</table>"
    return html_table
