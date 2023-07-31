# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.post_create_retweet200_response import PostCreateRetweet200Response  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestPostCreateRetweet200Response(unittest.TestCase):
    """PostCreateRetweet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostCreateRetweet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateRetweet200Response`
        """
        model = twitter_openapi_python_generated.models.post_create_retweet200_response.PostCreateRetweet200Response()  # noqa: E501
        if include_optional :
            return PostCreateRetweet200Response(
                data = twitter_openapi_python_generated.models.create_retweet_response_data.CreateRetweetResponseData(
                    create_retweet = twitter_openapi_python_generated.models.create_retweet_response_result.CreateRetweetResponseResult(
                        retweet_results = twitter_openapi_python_generated.models.create_retweet.CreateRetweet(
                            result = twitter_openapi_python_generated.models.retweet.Retweet(
                                legacy = twitter_openapi_python_generated.models.retweet_legacy.Retweet_legacy(
                                    full_text = '', ), 
                                rest_id = '4', ), ), ), ), 
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ]
            )
        else :
            return PostCreateRetweet200Response(
                data = twitter_openapi_python_generated.models.create_retweet_response_data.CreateRetweetResponseData(
                    create_retweet = twitter_openapi_python_generated.models.create_retweet_response_result.CreateRetweetResponseResult(
                        retweet_results = twitter_openapi_python_generated.models.create_retweet.CreateRetweet(
                            result = twitter_openapi_python_generated.models.retweet.Retweet(
                                legacy = twitter_openapi_python_generated.models.retweet_legacy.Retweet_legacy(
                                    full_text = '', ), 
                                rest_id = '4', ), ), ), ),
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ],
        )
        """

    def testPostCreateRetweet200Response(self):
        """Test PostCreateRetweet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
