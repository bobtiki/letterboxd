import logging

logging.getLogger(__name__)


class Lists(object):
    """
    /lists service for the Letterboxd API
    """

    def __init__(self, api):
        """

        :param api: API object
        """
        self._api = api

    def lists(self, lists_request={}):
        """
        /lists

        A cursored window over a list of lists.

        Use the ‘next’ cursor to move through the list.

        :param lists_request: dict - ListsRequest
        :return: dict - ListsResponse
        """
        response = self._api.api_call(path="lists", params=lists_request)
        lists_response = response.json()
        logging.debug(lists_response)
        return lists_response
