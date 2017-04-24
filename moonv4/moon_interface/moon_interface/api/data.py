# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.
"""
Data are elements used to create rules

"""

from flask import request
from flask_restful import Resource
from oslo_config import cfg
from oslo_log import log as logging
from moon_interface.tools import call
from moon_interface.tools import check_auth

__version__ = "0.2.0"

LOG = logging.getLogger(__name__)
CONF = cfg.CONF


class SubjectData(Resource):
    """
    Endpoint for subject data requests
    """

    __urls__ = (
        "/policies/<string:uuid>/subject_data",
        "/policies/<string:uuid>/subject_data/",
        "/policies/<string:uuid>/subject_data/<string:category_id>",
        "/policies/<string:uuid>/subject_data/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all subject categories or a specific one if sid is given for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the subject category
        :param data_id: uuid of the subject data
        :param user_id: user ID who do the request
        :return: [{
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "subject_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }]
        :internal_api: get_subject_data
        """
        return call(ctx={"id": uuid, "method": "get_subject_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Create or update a subject.

        :param uuid: uuid of the policy
        :param category_id: uuid of the subject category
        :param data_id: uuid of the subject data
        :param user_id: user ID who do the request
        :request body: {
            "name": "name of the data",
            "description": "description of the data"
        }
        :return: {
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "subject_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }
        :internal_api: add_subject_data
        """
        return call(ctx={"id": uuid, "method": "add_subject_data", "category_id": category_id, "user_id": user_id},
                    args=request.json)

    @check_auth
    def delete(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Delete a subject for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the subject category
        :param data_id: uuid of the subject data
        :param user_id: user ID who do the request
        :return: [{
            "result": "True or False",
            "message": "optional message"
        }]
        :internal_api: delete_subject_data
        """
        return call(ctx={"id": uuid, "method": "delete_subject_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})


class ObjectData(Resource):
    """
    Endpoint for object data requests
    """

    __urls__ = (
        "/policies/<string:uuid>/object_data",
        "/policies/<string:uuid>/object_data/",
        "/policies/<string:uuid>/object_data/<string:category_id>",
        "/policies/<string:uuid>/object_data/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all object categories or a specific one if sid is given for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the object category
        :param data_id: uuid of the object data
        :param user_id: user ID who do the request
        :return: [{
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "object_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }]
        :internal_api: get_object_data
        """
        return call(ctx={"id": uuid, "method": "get_object_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Create or update a object.

        :param uuid: uuid of the policy
        :param category_id: uuid of the object category
        :param data_id: uuid of the object data
        :param user_id: user ID who do the request
        :request body: {
            "name": "name of the data",
            "description": "description of the data"
        }
        :return: {
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "object_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }
        :internal_api: add_object_data
        """
        return call(ctx={"id": uuid, "method": "add_object_data", "category_id": category_id, "user_id": user_id}, args=request.json)

    @check_auth
    def delete(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Delete a object for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the object category
        :param data_id: uuid of the object data
        :param user_id: user ID who do the request
        :return: {
            "result": "True or False",
            "message": "optional message"
        }
        :internal_api: delete_object_data
        """
        return call(ctx={"id": uuid, "method": "delete_object_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})


class ActionData(Resource):
    """
    Endpoint for action data requests
    """

    __urls__ = (
        "/policies/<string:uuid>/action_data",
        "/policies/<string:uuid>/action_data/",
        "/policies/<string:uuid>/action_data/<string:category_id>",
        "/policies/<string:uuid>/action_data/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all action categories or a specific one if sid is given for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the action category
        :param data_id: uuid of the action data
        :param user_id: user ID who do the request
        :return: [{
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "action_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }]
        :internal_api: get_action_data
        """
        return call(ctx={"id": uuid, "method": "get_action_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Create or update a action.

        :param uuid: uuid of the policy
        :param category_id: uuid of the action category
        :param data_id: uuid of the action data
        :param user_id: user ID who do the request
        :request body: {
            "name": "name of the data",
            "description": "description of the data"
        }
        :return: {
            "policy_id": "policy_id1",
            "category_id": "category_id1",
            "data": {
                "action_data_id": {
                    "name": "name of the data",
                    "description": "description of the data"
                }
            }
        }
        :internal_api: add_action_data
        """
        return call(ctx={"id": uuid, "method": "add_action_data", "category_id": category_id, "user_id": user_id},
                    args=request.json)

    @check_auth
    def delete(self, uuid=None, category_id=None, data_id=None, user_id=None):
        """Delete a action for a given policy

        :param uuid: uuid of the policy
        :param category_id: uuid of the action category
        :param data_id: uuid of the action data
        :param user_id: user ID who do the request
        :return: {
            "result": "True or False",
            "message": "optional message"
        }
        :internal_api: delete_action_data
        """
        return call(ctx={"id": uuid, "method": "delete_action_data", "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

