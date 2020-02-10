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

from flyteadmin.models.admin_cluster_resource_attributes import AdminClusterResourceAttributes  # noqa: F401,E501
from flyteadmin.models.admin_execution_cluster_label import AdminExecutionClusterLabel  # noqa: F401,E501
from flyteadmin.models.admin_execution_queue_attributes import AdminExecutionQueueAttributes  # noqa: F401,E501
from flyteadmin.models.admin_task_resource_attributes import AdminTaskResourceAttributes  # noqa: F401,E501


class AdminMatchingAttributes(object):
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
        'task_resource_attributes': 'AdminTaskResourceAttributes',
        'cluster_resource_attributes': 'AdminClusterResourceAttributes',
        'execution_queue_attributes': 'AdminExecutionQueueAttributes',
        'execution_cluster_label': 'AdminExecutionClusterLabel'
    }

    attribute_map = {
        'task_resource_attributes': 'task_resource_attributes',
        'cluster_resource_attributes': 'cluster_resource_attributes',
        'execution_queue_attributes': 'execution_queue_attributes',
        'execution_cluster_label': 'execution_cluster_label'
    }

    def __init__(self, task_resource_attributes=None, cluster_resource_attributes=None, execution_queue_attributes=None, execution_cluster_label=None):  # noqa: E501
        """AdminMatchingAttributes - a model defined in Swagger"""  # noqa: E501

        self._task_resource_attributes = None
        self._cluster_resource_attributes = None
        self._execution_queue_attributes = None
        self._execution_cluster_label = None
        self.discriminator = None

        if task_resource_attributes is not None:
            self.task_resource_attributes = task_resource_attributes
        if cluster_resource_attributes is not None:
            self.cluster_resource_attributes = cluster_resource_attributes
        if execution_queue_attributes is not None:
            self.execution_queue_attributes = execution_queue_attributes
        if execution_cluster_label is not None:
            self.execution_cluster_label = execution_cluster_label

    @property
    def task_resource_attributes(self):
        """Gets the task_resource_attributes of this AdminMatchingAttributes.  # noqa: E501


        :return: The task_resource_attributes of this AdminMatchingAttributes.  # noqa: E501
        :rtype: AdminTaskResourceAttributes
        """
        return self._task_resource_attributes

    @task_resource_attributes.setter
    def task_resource_attributes(self, task_resource_attributes):
        """Sets the task_resource_attributes of this AdminMatchingAttributes.


        :param task_resource_attributes: The task_resource_attributes of this AdminMatchingAttributes.  # noqa: E501
        :type: AdminTaskResourceAttributes
        """

        self._task_resource_attributes = task_resource_attributes

    @property
    def cluster_resource_attributes(self):
        """Gets the cluster_resource_attributes of this AdminMatchingAttributes.  # noqa: E501


        :return: The cluster_resource_attributes of this AdminMatchingAttributes.  # noqa: E501
        :rtype: AdminClusterResourceAttributes
        """
        return self._cluster_resource_attributes

    @cluster_resource_attributes.setter
    def cluster_resource_attributes(self, cluster_resource_attributes):
        """Sets the cluster_resource_attributes of this AdminMatchingAttributes.


        :param cluster_resource_attributes: The cluster_resource_attributes of this AdminMatchingAttributes.  # noqa: E501
        :type: AdminClusterResourceAttributes
        """

        self._cluster_resource_attributes = cluster_resource_attributes

    @property
    def execution_queue_attributes(self):
        """Gets the execution_queue_attributes of this AdminMatchingAttributes.  # noqa: E501


        :return: The execution_queue_attributes of this AdminMatchingAttributes.  # noqa: E501
        :rtype: AdminExecutionQueueAttributes
        """
        return self._execution_queue_attributes

    @execution_queue_attributes.setter
    def execution_queue_attributes(self, execution_queue_attributes):
        """Sets the execution_queue_attributes of this AdminMatchingAttributes.


        :param execution_queue_attributes: The execution_queue_attributes of this AdminMatchingAttributes.  # noqa: E501
        :type: AdminExecutionQueueAttributes
        """

        self._execution_queue_attributes = execution_queue_attributes

    @property
    def execution_cluster_label(self):
        """Gets the execution_cluster_label of this AdminMatchingAttributes.  # noqa: E501


        :return: The execution_cluster_label of this AdminMatchingAttributes.  # noqa: E501
        :rtype: AdminExecutionClusterLabel
        """
        return self._execution_cluster_label

    @execution_cluster_label.setter
    def execution_cluster_label(self, execution_cluster_label):
        """Sets the execution_cluster_label of this AdminMatchingAttributes.


        :param execution_cluster_label: The execution_cluster_label of this AdminMatchingAttributes.  # noqa: E501
        :type: AdminExecutionClusterLabel
        """

        self._execution_cluster_label = execution_cluster_label

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
        if issubclass(AdminMatchingAttributes, dict):
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
        if not isinstance(other, AdminMatchingAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
