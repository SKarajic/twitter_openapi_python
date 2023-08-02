# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from twitter_openapi_python_generated.models.error_extensions import ErrorExtensions
from twitter_openapi_python_generated.models.location import Location
from twitter_openapi_python_generated.models.tracing import Tracing

class Error(BaseModel):
    """
    Error
    """
    code: StrictInt = Field(...)
    extensions: ErrorExtensions = Field(...)
    kind: StrictStr = Field(...)
    locations: conlist(Location) = Field(...)
    message: StrictStr = Field(...)
    name: StrictStr = Field(...)
    path: conlist(StrictStr) = Field(...)
    retry_after: StrictInt = Field(...)
    source: StrictStr = Field(...)
    tracing: Tracing = Field(...)
    __properties = ["code", "extensions", "kind", "locations", "message", "name", "path", "retry_after", "source", "tracing"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Error:
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of extensions
        if self.extensions:
            _dict['extensions'] = self.extensions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of tracing
        if self.tracing:
            _dict['tracing'] = self.tracing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Error:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Error.parse_obj(obj)

        _obj = Error.parse_obj({
            "code": obj.get("code"),
            "extensions": ErrorExtensions.from_dict(obj.get("extensions")) if obj.get("extensions") is not None else None,
            "kind": obj.get("kind"),
            "locations": [Location.from_dict(_item) for _item in obj.get("locations")] if obj.get("locations") is not None else None,
            "message": obj.get("message"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "retry_after": obj.get("retry_after"),
            "source": obj.get("source"),
            "tracing": Tracing.from_dict(obj.get("tracing")) if obj.get("tracing") is not None else None
        })
        return _obj

