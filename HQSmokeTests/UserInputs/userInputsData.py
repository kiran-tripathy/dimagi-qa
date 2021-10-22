import os
from pathlib import Path


class UserInputsData:
    application = "Village Health"
    domain = "qa-automation"
    if os.environ.get("CI") == "true":
        download_path = Path("/home/runner/work/dimagi-qa/dimagi-qa")
    else:
        download_path = Path('~/Downloads').expanduser()
    # Report names
    Screenshots = download_path = Path("/home/runner/work/dimagi-qa/dimagi-qa/Screenshots")
    form_export_name = "CCHQ Smoke Tests Form Export DSE"
    case_export_name = "CCHQ Smoke Tests Case Export DSE"
    dashboard_feed_form = "CCHQ Smoke Tests Dashboard Form feed"
    dashboard_feed_case = "CCHQ Smoke Tests Dashboard Case feed"
    odata_feed_form = "CCHQ Smoke Tests Odata Form feed"
    odata_feed_case = "CCHQ Smoke Tests Odata Case feed"
