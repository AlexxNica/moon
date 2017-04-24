# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.
"""
Assignments allow to connect data with elements of perimeter

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


class SubjectAssignments(Resource):
    """
    Endpoint for subject assignment requests
    """

    __urls__ = (
        "/policies/<string:uuid>/subject_assignments",
        "/policies/<string:uuid>/subject_assignments/",
        "/policies/<string:uuid>/subject_assignments/<string:perimeter_id>",
        "/policies/<string:uuid>/subject_assignments/<string:perimeter_id>/<string:category_id>",
        "/policies/<string:uuid>/subject_assignments/<string:perimeter_id>/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all subject assignments or a specific one for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the subject
        :param category_id: uuid of the subject category
        :param data_id: uuid of the subject scope
        :param user_id: user ID who do the request
        :return: {
            "subject_data_id": {
                "policy_id": "ID of the policy",
                "subject_id": "ID of the subject",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: get_subject_assignments
        """
        return call(ctx={"id": uuid, "method": "get_subject_assignments", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Create a subject assignment.

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the subject (not used here)
        :param category_id: uuid of the subject category (not used here)
        :param data_id: uuid of the subject scope (not used here)
        :param user_id: user ID who do the request
        :request body: {
            "id": "UUID of the subject",
            "category_id": "UUID of the category"
            "data_id": "UUID of the scope"
        }
        :return: {
            "subject_data_id": {
                "policy_id": "ID of the policy",
                "subject_id": "ID of the subject",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: update_subject_assignment
        """
        return call(ctx={"id": uuid, "method": "update_subject_assignment", "user_id": user_id}, args=request.json)

    @check_auth
    def delete(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Delete a subject assignment for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the subject
        :param category_id: uuid of the subject category
        :param data_id: uuid of the subject scope
        :param user_id: user ID who do the request
        :return: {
            "result": "True or False",
            "message": "optional message"
        }
        :internal_api: delete_subject_assignment
        """
        return call(ctx={"id": uuid, "method": "delete_subject_assignment", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})


class ObjectAssignments(Resource):
    """
    Endpoint for object assignment requests
    """

    __urls__ = (
        "/policies/<string:uuid>/object_assignments",
        "/policies/<string:uuid>/object_assignments/",
        "/policies/<string:uuid>/object_assignments/<string:perimeter_id>",
        "/policies/<string:uuid>/object_assignments/<string:perimeter_id>/<string:category_id>",
        "/policies/<string:uuid>/object_assignments/<string:perimeter_id>/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all object assignment or a specific one for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the object
        :param category_id: uuid of the object category
        :param data_id: uuid of the object scope
        :param user_id: user ID who do the request
        :return: {
            "object_data_id": {
                "policy_id": "ID of the policy",
                "object_id": "ID of the object",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: get_object_assignments
        """
        return call(ctx={"id": uuid, "method": "get_object_assignments", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Create an object assignment.

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the object (not used here)
        :param category_id: uuid of the object category (not used here)
        :param data_id: uuid of the object scope (not used here)
        :param user_id: user ID who do the request
        :request body: {
            "id": "UUID of the action",
            "category_id": "UUID of the category"
            "data_id": "UUID of the scope"
        }
        :return: {
            "object_data_id": {
                "policy_id": "ID of the policy",
                "object_id": "ID of the object",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: update_object_assignment
        """
        return call(ctx={"id": uuid, "method": "update_object_assignment", "user_id": user_id}, args=request.json)

    @check_auth
    def delete(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Delete a object assignment for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the object
        :param category_id: uuid of the object category
        :param data_id: uuid of the object scope
        :param user_id: user ID who do the request
        :return: {
            "result": "True or False",
            "message": "optional message"
        }
        :internal_api: delete_object_assignment
        """
        return call(ctx={"id": uuid, "method": "delete_object_assignment", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})


class ActionAssignments(Resource):
    """
    Endpoint for action assignment requests
    """

    __urls__ = (
        "/policies/<string:uuid>/action_assignments",
        "/policies/<string:uuid>/action_assignments/",
        "/policies/<string:uuid>/action_assignments/<string:perimeter_id>",
        "/policies/<string:uuid>/action_assignments/<string:perimeter_id>/<string:category_id>",
        "/policies/<string:uuid>/action_assignments/<string:perimeter_id>/<string:category_id>/<string:data_id>",
    )

    @check_auth
    def get(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Retrieve all action assignment or a specific one for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the action
        :param category_id: uuid of the action category
        :param data_id: uuid of the action scope
        :param user_id: user ID who do the request
        :return: {
            "action_data_id": {
                "policy_id": "ID of the policy",
                "object_id": "ID of the action",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: get_action_assignments
        """
        return call(ctx={"id": uuid, "method": "get_action_assignments", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})

    @check_auth
    def post(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Create an action assignment.

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the action (not used here)
        :param category_id: uuid of the action category (not used here)
        :param data_id: uuid of the action scope (not used here)
        :param user_id: user ID who do the request
        :request body: {
            "id": "UUID of the action",
            "category_id": "UUID of the category",
            "data_id": "UUID of the scope"
        }
        :return: {
            "action_data_id": {
                "policy_id": "ID of the policy",
                "object_id": "ID of the action",
                "category_id": "ID of the category",
                "assignments": "Assignments list (list of data_id)",
            }
        }
        :internal_api: update_action_assignment
        """
        return call(ctx={"id": uuid, "method": "update_action_assignment", "user_id": user_id},
                    args=request.json)

    @check_auth
    def delete(self, uuid=None, perimeter_id=None, category_id=None, data_id=None, user_id=None):
        """Delete a action assignment for a given policy

        :param uuid: uuid of the policy
        :param perimeter_id: uuid of the action
        :param category_id: uuid of the action category
        :param data_id: uuid of the action scope
        :param user_id: user ID who do the request
        :return: {
            "result": "True or False",
            "message": "optional message"
        }
        :internal_api: delete_action_assignment
        """
        return call(ctx={"id": uuid, "method": "delete_action_assignment", "perimeter_id": perimeter_id, "category_id": category_id, "user_id": user_id},
                    args={"data_id": data_id})