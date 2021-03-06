"""Communication with storage."""
import json
import os

import env


def check_storage(form_data):
    """Check if result file is available in storage."""
    filepath = env.analysis(form_data['id'])['resultfile']

    if not os.path.isfile(filepath):
        return None

    print('[STORAGE] return analysis result of {} ...'.format(form_data['id']))
    with open(filepath) as f:
        json_data = json.load(f)
        # TODO: check if analysis result up to date, if not trigger reprocessing
        return json_data
