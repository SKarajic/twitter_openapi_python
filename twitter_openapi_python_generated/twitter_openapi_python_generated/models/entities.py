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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conlist
from twitter_openapi_python_generated.models.media import Media
from twitter_openapi_python_generated.models.url import Url

class Entities(BaseModel):
    """
    Entities
    """
    hashtags: conlist(Dict[str, Any]) = Field(...)
    media: Optional[conlist(Media)] = None
    symbols: conlist(Dict[str, Any]) = Field(...)
    urls: conlist(Url) = Field(...)
    user_mentions: conlist(Dict[str, Any]) = Field(...)
    __properties = ["hashtags", "media", "symbols", "urls", "user_mentions"]

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
    def from_json(cls, json_str: str) -> Entities:
        """Create an instance of Entities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item in self.media:
                if _item:
                    _items.append(_item.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in urls (list)
        _items = []
        if self.urls:
            for _item in self.urls:
                if _item:
                    _items.append(_item.to_dict())
            _dict['urls'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Entities:
        """Create an instance of Entities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Entities.parse_obj(obj)

        _obj = Entities.parse_obj({
            "hashtags": obj.get("hashtags"),
            "media": [Media.from_dict(_item) for _item in obj.get("media")] if obj.get("media") is not None else None,
            "symbols": obj.get("symbols"),
            "urls": [Url.from_dict(_item) for _item in obj.get("urls")] if obj.get("urls") is not None else None,
            "user_mentions": obj.get("user_mentions")
        })
        return _obj


