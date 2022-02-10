import os
from pathlib import Path


class UserData:

    """Path Settings"""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    if os.environ.get("CI") == "true":
        DOWNLOAD_PATH = Path("/home/runner/work/dimagi-qa/dimagi-qa")
    else:
        DOWNLOAD_PATH = Path('~/Downloads').expanduser()

    """User Test Data"""

    # Pre-setup application names
    village_application = "Village Health"

    # Export report names
    form_export_name = "Form Export DSE"
    case_export_name = "Case Export DSE"
    dashboard_feed_form = "Dashboard Form feed"
    dashboard_feed_case = "Dashboard Case feed"
    odata_feed_form = "Odata Form feed"
    odata_feed_case = "Odata Case feed"

    # Date Filter
    date_having_submissions = "2022-01-18 to 2022-02-18"
