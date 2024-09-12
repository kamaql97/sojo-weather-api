import unittest

from pydantic import ValidationError

from src.models import OriginalApiRealTimeSchema

from src.helpers import (
    validate_original_api_response,
    transform_validated_original_response,
)
from tests.data import (
    VALID_ORIGINAL_RESPONSE,
    INVALID_ORIGINAL_RESPONSE,
    EXPECTED_TRANSFORMED_DATA,
)


class TestValidateOriginalApiResponse(unittest.TestCase):
    def test_validate_original_api_response__valid_schema(self):
        validated_data = validate_original_api_response(VALID_ORIGINAL_RESPONSE)
        self.assertIsInstance(validated_data, OriginalApiRealTimeSchema)

    def test_validate_original_api_response__validation_error(self):
        with self.assertRaises(ValidationError):
            validate_original_api_response(INVALID_ORIGINAL_RESPONSE)


class TestTransformValidatedOriginalResponse(unittest.TestCase):
    def test_transform_validated_original_response__valid_schema(self):
        original_data = OriginalApiRealTimeSchema(**VALID_ORIGINAL_RESPONSE)
        real_transformed_data = transform_validated_original_response(original_data)
        self.assertEqual(real_transformed_data, EXPECTED_TRANSFORMED_DATA)
