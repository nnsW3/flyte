# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.admin_annotations import AdminAnnotations  # noqa: F401,E501
from flyteadmin.models.admin_auth_role import AdminAuthRole  # noqa: F401,E501
from flyteadmin.models.admin_cluster_assignment import AdminClusterAssignment  # noqa: F401,E501
from flyteadmin.models.admin_execution_metadata import AdminExecutionMetadata  # noqa: F401,E501
from flyteadmin.models.admin_labels import AdminLabels  # noqa: F401,E501
from flyteadmin.models.admin_notification_list import AdminNotificationList  # noqa: F401,E501
from flyteadmin.models.admin_raw_output_data_config import AdminRawOutputDataConfig  # noqa: F401,E501
from flyteadmin.models.core_identifier import CoreIdentifier  # noqa: F401,E501
from flyteadmin.models.core_literal_map import CoreLiteralMap  # noqa: F401,E501
from flyteadmin.models.core_quality_of_service import CoreQualityOfService  # noqa: F401,E501
from flyteadmin.models.core_security_context import CoreSecurityContext  # noqa: F401,E501


class AdminExecutionSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'launch_plan': 'CoreIdentifier',
        'inputs': 'CoreLiteralMap',
        'metadata': 'AdminExecutionMetadata',
        'notifications': 'AdminNotificationList',
        'disable_all': 'bool',
        'labels': 'AdminLabels',
        'annotations': 'AdminAnnotations',
        'security_context': 'CoreSecurityContext',
        'auth_role': 'AdminAuthRole',
        'quality_of_service': 'CoreQualityOfService',
        'max_parallelism': 'int',
        'raw_output_data_config': 'AdminRawOutputDataConfig',
        'cluster_assignment': 'AdminClusterAssignment'
    }

    attribute_map = {
        'launch_plan': 'launch_plan',
        'inputs': 'inputs',
        'metadata': 'metadata',
        'notifications': 'notifications',
        'disable_all': 'disable_all',
        'labels': 'labels',
        'annotations': 'annotations',
        'security_context': 'security_context',
        'auth_role': 'auth_role',
        'quality_of_service': 'quality_of_service',
        'max_parallelism': 'max_parallelism',
        'raw_output_data_config': 'raw_output_data_config',
        'cluster_assignment': 'cluster_assignment'
    }

    def __init__(self, launch_plan=None, inputs=None, metadata=None, notifications=None, disable_all=None, labels=None, annotations=None, security_context=None, auth_role=None, quality_of_service=None, max_parallelism=None, raw_output_data_config=None, cluster_assignment=None):  # noqa: E501
        """AdminExecutionSpec - a model defined in Swagger"""  # noqa: E501

        self._launch_plan = None
        self._inputs = None
        self._metadata = None
        self._notifications = None
        self._disable_all = None
        self._labels = None
        self._annotations = None
        self._security_context = None
        self._auth_role = None
        self._quality_of_service = None
        self._max_parallelism = None
        self._raw_output_data_config = None
        self._cluster_assignment = None
        self.discriminator = None

        if launch_plan is not None:
            self.launch_plan = launch_plan
        if inputs is not None:
            self.inputs = inputs
        if metadata is not None:
            self.metadata = metadata
        if notifications is not None:
            self.notifications = notifications
        if disable_all is not None:
            self.disable_all = disable_all
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if security_context is not None:
            self.security_context = security_context
        if auth_role is not None:
            self.auth_role = auth_role
        if quality_of_service is not None:
            self.quality_of_service = quality_of_service
        if max_parallelism is not None:
            self.max_parallelism = max_parallelism
        if raw_output_data_config is not None:
            self.raw_output_data_config = raw_output_data_config
        if cluster_assignment is not None:
            self.cluster_assignment = cluster_assignment

    @property
    def launch_plan(self):
        """Gets the launch_plan of this AdminExecutionSpec.  # noqa: E501


        :return: The launch_plan of this AdminExecutionSpec.  # noqa: E501
        :rtype: CoreIdentifier
        """
        return self._launch_plan

    @launch_plan.setter
    def launch_plan(self, launch_plan):
        """Sets the launch_plan of this AdminExecutionSpec.


        :param launch_plan: The launch_plan of this AdminExecutionSpec.  # noqa: E501
        :type: CoreIdentifier
        """

        self._launch_plan = launch_plan

    @property
    def inputs(self):
        """Gets the inputs of this AdminExecutionSpec.  # noqa: E501


        :return: The inputs of this AdminExecutionSpec.  # noqa: E501
        :rtype: CoreLiteralMap
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this AdminExecutionSpec.


        :param inputs: The inputs of this AdminExecutionSpec.  # noqa: E501
        :type: CoreLiteralMap
        """

        self._inputs = inputs

    @property
    def metadata(self):
        """Gets the metadata of this AdminExecutionSpec.  # noqa: E501


        :return: The metadata of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminExecutionMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AdminExecutionSpec.


        :param metadata: The metadata of this AdminExecutionSpec.  # noqa: E501
        :type: AdminExecutionMetadata
        """

        self._metadata = metadata

    @property
    def notifications(self):
        """Gets the notifications of this AdminExecutionSpec.  # noqa: E501

        List of notifications based on Execution status transitions When this list is not empty it is used rather than any notifications defined in the referenced launch plan. When this list is empty, the notifications defined for the launch plan will be applied.  # noqa: E501

        :return: The notifications of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminNotificationList
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this AdminExecutionSpec.

        List of notifications based on Execution status transitions When this list is not empty it is used rather than any notifications defined in the referenced launch plan. When this list is empty, the notifications defined for the launch plan will be applied.  # noqa: E501

        :param notifications: The notifications of this AdminExecutionSpec.  # noqa: E501
        :type: AdminNotificationList
        """

        self._notifications = notifications

    @property
    def disable_all(self):
        """Gets the disable_all of this AdminExecutionSpec.  # noqa: E501

        This should be set to true if all notifications are intended to be disabled for this execution.  # noqa: E501

        :return: The disable_all of this AdminExecutionSpec.  # noqa: E501
        :rtype: bool
        """
        return self._disable_all

    @disable_all.setter
    def disable_all(self, disable_all):
        """Sets the disable_all of this AdminExecutionSpec.

        This should be set to true if all notifications are intended to be disabled for this execution.  # noqa: E501

        :param disable_all: The disable_all of this AdminExecutionSpec.  # noqa: E501
        :type: bool
        """

        self._disable_all = disable_all

    @property
    def labels(self):
        """Gets the labels of this AdminExecutionSpec.  # noqa: E501

        Labels to apply to the execution resource.  # noqa: E501

        :return: The labels of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminLabels
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AdminExecutionSpec.

        Labels to apply to the execution resource.  # noqa: E501

        :param labels: The labels of this AdminExecutionSpec.  # noqa: E501
        :type: AdminLabels
        """

        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this AdminExecutionSpec.  # noqa: E501

        Annotations to apply to the execution resource.  # noqa: E501

        :return: The annotations of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminAnnotations
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this AdminExecutionSpec.

        Annotations to apply to the execution resource.  # noqa: E501

        :param annotations: The annotations of this AdminExecutionSpec.  # noqa: E501
        :type: AdminAnnotations
        """

        self._annotations = annotations

    @property
    def security_context(self):
        """Gets the security_context of this AdminExecutionSpec.  # noqa: E501

        Optional: security context override to apply this execution.  # noqa: E501

        :return: The security_context of this AdminExecutionSpec.  # noqa: E501
        :rtype: CoreSecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this AdminExecutionSpec.

        Optional: security context override to apply this execution.  # noqa: E501

        :param security_context: The security_context of this AdminExecutionSpec.  # noqa: E501
        :type: CoreSecurityContext
        """

        self._security_context = security_context

    @property
    def auth_role(self):
        """Gets the auth_role of this AdminExecutionSpec.  # noqa: E501

        Optional: auth override to apply this execution.  # noqa: E501

        :return: The auth_role of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminAuthRole
        """
        return self._auth_role

    @auth_role.setter
    def auth_role(self, auth_role):
        """Sets the auth_role of this AdminExecutionSpec.

        Optional: auth override to apply this execution.  # noqa: E501

        :param auth_role: The auth_role of this AdminExecutionSpec.  # noqa: E501
        :type: AdminAuthRole
        """

        self._auth_role = auth_role

    @property
    def quality_of_service(self):
        """Gets the quality_of_service of this AdminExecutionSpec.  # noqa: E501

        Indicates the runtime priority of the execution.  # noqa: E501

        :return: The quality_of_service of this AdminExecutionSpec.  # noqa: E501
        :rtype: CoreQualityOfService
        """
        return self._quality_of_service

    @quality_of_service.setter
    def quality_of_service(self, quality_of_service):
        """Sets the quality_of_service of this AdminExecutionSpec.

        Indicates the runtime priority of the execution.  # noqa: E501

        :param quality_of_service: The quality_of_service of this AdminExecutionSpec.  # noqa: E501
        :type: CoreQualityOfService
        """

        self._quality_of_service = quality_of_service

    @property
    def max_parallelism(self):
        """Gets the max_parallelism of this AdminExecutionSpec.  # noqa: E501

        Controls the maximum number of task nodes that can be run in parallel for the entire workflow. This is useful to achieve fairness. Note: MapTasks are regarded as one unit, and parallelism/concurrency of MapTasks is independent from this.  # noqa: E501

        :return: The max_parallelism of this AdminExecutionSpec.  # noqa: E501
        :rtype: int
        """
        return self._max_parallelism

    @max_parallelism.setter
    def max_parallelism(self, max_parallelism):
        """Sets the max_parallelism of this AdminExecutionSpec.

        Controls the maximum number of task nodes that can be run in parallel for the entire workflow. This is useful to achieve fairness. Note: MapTasks are regarded as one unit, and parallelism/concurrency of MapTasks is independent from this.  # noqa: E501

        :param max_parallelism: The max_parallelism of this AdminExecutionSpec.  # noqa: E501
        :type: int
        """

        self._max_parallelism = max_parallelism

    @property
    def raw_output_data_config(self):
        """Gets the raw_output_data_config of this AdminExecutionSpec.  # noqa: E501


        :return: The raw_output_data_config of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminRawOutputDataConfig
        """
        return self._raw_output_data_config

    @raw_output_data_config.setter
    def raw_output_data_config(self, raw_output_data_config):
        """Sets the raw_output_data_config of this AdminExecutionSpec.


        :param raw_output_data_config: The raw_output_data_config of this AdminExecutionSpec.  # noqa: E501
        :type: AdminRawOutputDataConfig
        """

        self._raw_output_data_config = raw_output_data_config

    @property
    def cluster_assignment(self):
        """Gets the cluster_assignment of this AdminExecutionSpec.  # noqa: E501

        Controls how to select an available cluster on which this execution should run.  # noqa: E501

        :return: The cluster_assignment of this AdminExecutionSpec.  # noqa: E501
        :rtype: AdminClusterAssignment
        """
        return self._cluster_assignment

    @cluster_assignment.setter
    def cluster_assignment(self, cluster_assignment):
        """Sets the cluster_assignment of this AdminExecutionSpec.

        Controls how to select an available cluster on which this execution should run.  # noqa: E501

        :param cluster_assignment: The cluster_assignment of this AdminExecutionSpec.  # noqa: E501
        :type: AdminClusterAssignment
        """

        self._cluster_assignment = cluster_assignment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdminExecutionSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdminExecutionSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
