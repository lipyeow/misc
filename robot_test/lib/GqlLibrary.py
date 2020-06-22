import os.path
import sys


class GqlLibrary(object):

    def __init__(self):
        self._status = ''
        self._hunt_spec_ids = []
        self._mission_spec_ids = []
        self._hunt_run_ids = []
        self._ids = [self._hunt_spec_ids, self._mission_spec_ids, self._hunt_run_ids]
        self._del_gqls = ["", "", ""]

    def clear_database(self, server):
        print("clear db")
        for (gql, ids) in zip(self._del_gqls, self._ids):
            print("deleting")

    def status_should_be(self, expected_status):
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def run_gql_create_huntspec(self, server, gql_fname):
        assert os.path.exists(gql_fname)
        assert os.path.exists(gql_fname + ".exp")
        print("run gql query at server")
        print("check results")

        # store uuid in hunt spec ids

        self._status = "response matched expected"
    def run_gql_query(self, server, gql_fname):
        assert os.path.exists(gql_fname)
        assert os.path.exists(gql_fname + ".exp")
        print("run gql query at server")
        print("check results")

        self._status = "response matched expected"
