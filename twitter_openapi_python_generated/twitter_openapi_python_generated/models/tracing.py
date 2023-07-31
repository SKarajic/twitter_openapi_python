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



from pydantic import BaseModel, Field, constr, validator

class Tracing(BaseModel):
    """
    Tracing
    """
    trace_id: constr(strict=True) = Field(...)
    __properties = ["trace_id"]

    @validator('trace_id')
    def trace_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9a-f]{16}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{16}$/")
        return value

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
    def from_json(cls, json_str: str) -> Tracing:
        """Create an instance of Tracing from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Tracing:
        """Create an instance of Tracing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Tracing.parse_obj(obj)

        _obj = Tracing.parse_obj({
            "trace_id": obj.get("trace_id")
        })
        return _obj


