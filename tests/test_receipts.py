"""
Testing of Client.receipts endpoint functions

Tests:
* test_get_by_id: testing get_by_id function
* test_get_by_date: testing get_by_date function
"""

import pytest
from datetime import datetime
from loyverse import Client
from loyverse.utils.dates import add_timezone
from tests.utils import error_msg


endpoint = 'receipts'


@pytest.mark.vcr()
def test_get_by_id():
    """
    Test Client.receipts get_by_id endpoint function
    """

    # Excepted results
    receipt_id = '1-4076'

    client = Client()
    receipt = client.receipts.get_by_id(receipt_id)

    assert isinstance(receipt, dict), error_msg(endpoint, 'get_by_id return type not of type: dict')
    assert receipt['receipt_number'] == receipt_id, error_msg(endpoint, 'receipt ID should be in the response')


@pytest.mark.vcr()
def test_get_by_date():
    """
    Test Client.receipts get_by_date endpoint function
    """

    # Query arguments
    date = datetime(2020, 10, 12)
    date_tz = add_timezone(date, 'Europe/Zurich')

    # Expected results
    receipts_length = 40

    client = Client()
    receipts = client.receipts.get_by_date(date_tz)

    assert isinstance(receipts, dict), error_msg(endpoint, 'get_by_date return type not of type dict')
    assert len(receipts['receipts']) == receipts_length, error_msg(endpoint, 'get_by_date: incorrect number of '
                                                                             'receipts retrieved')
