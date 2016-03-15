# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from pprint import pformat
from six import iteritems


class BuildConfigSetRecord(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BuildConfigSetRecord - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'build_configuration_set': 'BuildConfigurationSet',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'user': 'User',
            'status': 'str',
            'build_records': 'list[BuildRecord]',
            'product_version': 'ProductVersion',
            'field_handler': 'FieldHandler'
        }

        self.attribute_map = {
            'id': 'id',
            'build_configuration_set': 'buildConfigurationSet',
            'start_time': 'startTime',
            'end_time': 'endTime',
            'user': 'user',
            'status': 'status',
            'build_records': 'buildRecords',
            'product_version': 'productVersion',
            'field_handler': 'fieldHandler'
        }

        self._id = None
        self._build_configuration_set = None
        self._start_time = None
        self._end_time = None
        self._user = None
        self._status = None
        self._build_records = None
        self._product_version = None
        self._field_handler = None

    @property
    def id(self):
        """
        Gets the id of this BuildConfigSetRecord.


        :return: The id of this BuildConfigSetRecord.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BuildConfigSetRecord.


        :param id: The id of this BuildConfigSetRecord.
        :type: int
        """
        self._id = id

    @property
    def build_configuration_set(self):
        """
        Gets the build_configuration_set of this BuildConfigSetRecord.


        :return: The build_configuration_set of this BuildConfigSetRecord.
        :rtype: BuildConfigurationSet
        """
        return self._build_configuration_set

    @build_configuration_set.setter
    def build_configuration_set(self, build_configuration_set):
        """
        Sets the build_configuration_set of this BuildConfigSetRecord.


        :param build_configuration_set: The build_configuration_set of this BuildConfigSetRecord.
        :type: BuildConfigurationSet
        """
        self._build_configuration_set = build_configuration_set

    @property
    def start_time(self):
        """
        Gets the start_time of this BuildConfigSetRecord.


        :return: The start_time of this BuildConfigSetRecord.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this BuildConfigSetRecord.


        :param start_time: The start_time of this BuildConfigSetRecord.
        :type: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this BuildConfigSetRecord.


        :return: The end_time of this BuildConfigSetRecord.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this BuildConfigSetRecord.


        :param end_time: The end_time of this BuildConfigSetRecord.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def user(self):
        """
        Gets the user of this BuildConfigSetRecord.


        :return: The user of this BuildConfigSetRecord.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this BuildConfigSetRecord.


        :param user: The user of this BuildConfigSetRecord.
        :type: User
        """
        self._user = user

    @property
    def status(self):
        """
        Gets the status of this BuildConfigSetRecord.


        :return: The status of this BuildConfigSetRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BuildConfigSetRecord.


        :param status: The status of this BuildConfigSetRecord.
        :type: str
        """
        allowed_values = ["SUCCESS", "FAILED", "UNSTABLE", "BUILDING", "REJECTED", "CANCELLED", "SYSTEM_ERROR", "UNKNOWN"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status`, must be one of {0}"
                .format(allowed_values)
            )
        self._status = status

    @property
    def build_records(self):
        """
        Gets the build_records of this BuildConfigSetRecord.


        :return: The build_records of this BuildConfigSetRecord.
        :rtype: list[BuildRecord]
        """
        return self._build_records

    @build_records.setter
    def build_records(self, build_records):
        """
        Sets the build_records of this BuildConfigSetRecord.


        :param build_records: The build_records of this BuildConfigSetRecord.
        :type: list[BuildRecord]
        """
        self._build_records = build_records

    @property
    def product_version(self):
        """
        Gets the product_version of this BuildConfigSetRecord.


        :return: The product_version of this BuildConfigSetRecord.
        :rtype: ProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """
        Sets the product_version of this BuildConfigSetRecord.


        :param product_version: The product_version of this BuildConfigSetRecord.
        :type: ProductVersion
        """
        self._product_version = product_version

    @property
    def field_handler(self):
        """
        Gets the field_handler of this BuildConfigSetRecord.


        :return: The field_handler of this BuildConfigSetRecord.
        :rtype: FieldHandler
        """
        return self._field_handler

    @field_handler.setter
    def field_handler(self, field_handler):
        """
        Sets the field_handler of this BuildConfigSetRecord.


        :param field_handler: The field_handler of this BuildConfigSetRecord.
        :type: FieldHandler
        """
        self._field_handler = field_handler

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
	    elif isinstance(value, datetime):
		result[attr] = str(value.date())
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
