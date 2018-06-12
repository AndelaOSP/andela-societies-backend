"""Test suite for Point Redemption Module."""
import json
import uuid
from .base_test import BaseTestCase


class PointRedemptionBaseTestCase(BaseTestCase):
    """Test class for Society point redemption including endpoint."""

    def setUp(self):
        """Set up all needed variables."""
        BaseTestCase.setUp(self)
        self.president_role.save()
        self.v_president_role.save()
        self.successops_role.save()
        self.invictus.save()
        self.istelle.save()
        self.sparks.save()
        self.phoenix.save()
        self.redemp_req.save()

    def test_create_redemption_request(self):
        """Test creation of Redemption Request through endpoint."""
        new_request = dict(
            name="T-shirt Funds Request",
            value=2500,
            user_id=self.test_user.uuid
            )

        response = self.client.post("api/v1/societies/redeem",
                                    data=json.dumps(new_request),
                                    headers=self.society_president,
                                    content_type='application/json')

        message = "created"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 201)

    def test_create_redemption_request_no_payload(self):
        """Test RedemptionRequest creation without payload fails."""
        response = self.client.post("api/v1/societies/redeem",
                                    headers=self.society_president,
                                    content_type='application/json')

        message = "must have data"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 400)

    def test_create_redemption_request_invalid_fields(self):
        """Test RedemptionRequest creation without payload fails."""
        invalid_request = dict(
            descriptor="T-shirt Funds Request",
            amount=2500,
            user_id=self.test_user.uuid
            )

        response = self.client.post("api/v1/societies/redeem",
                                    data=json.dumps(invalid_request),
                                    headers=self.society_president,
                                    content_type='application/json')

        message = "required"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 400)

    def test_get_all_redemption_requests(self):
        """Test retrieval of Redemption Requests."""
        response = self.client.get("api/v1/societies/redeem",
                                   headers=self.society_president,
                                   content_type='application/json')

        message = "fetched successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_get_existing_redemption_requests_by_id(self):
        """Test retrieval of Redemption Requests."""
        response = self.client.get(
                        f"api/v1/societies/redeem/{self.redemp_req.uuid}",
                        headers=self.society_president,
                        content_type='application/json')

        message = "fetched successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_get_existing_redemption_requests_by_name(self):
        """Test retrieval of Redemption Requests."""
        response = self.client.get(
                    f"api/v1/societies/redeem?name={self.redemp_req.name}",
                    headers=self.society_president,
                    content_type='application/json')

        message = "fetched successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_get_existing_redemption_requests_by_society(self):
        """Test retrieval of Redemption Requests."""
        response = self.client.get(
                    f"api/v1/societies/redeem?society={self.redemp_req.name}",
                    headers=self.society_president,
                    content_type='application/json')

        message = "fetched successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_get_existing_redemption_requests_by_status(self):
        """Test retrieval of Redemption Requests."""
        response = self.client.get(
                    f"api/v1/societies/redeem?status={self.redemp_req.name}",
                    headers=self.society_president,
                    content_type='application/json')

        message = "fetched successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_edit_redemption_request(self):
        """Test edit of Redemption Request through endpoint."""
        edit_request = dict(
            name="T-shirt Funds Request",
            value=2500
            )

        response = self.client.put(
                        f"api/v1/societies/redeem/{self.redemp_req.uuid}",
                        data=json.dumps(edit_request),
                        headers=self.society_president,
                        content_type='application/json')

        message = "edited successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_edit_nonexistent_redemption_request(self):
        """Test editing nonexistent Redemption Request fails."""
        edit_request = dict(
            name="T-shirt Funds Request",
            value=2500
            )

        response = self.client.put(
                        f"api/v1/societies/redeem/{str(uuid.uuid4())}",
                        data=json.dumps(edit_request),
                        headers=self.society_president,
                        content_type='application/json')

        message = "does not exist"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 404)

    def test_edit_redemption_request_no_id(self):
        """Test editing request without ID fails."""
        edit_request = dict(
            name="T-shirt Funds Request",
            value=2500
            )

        response = self.client.put("api/v1/societies/redeem",
                                   data=json.dumps(edit_request),
                                   headers=self.society_president,
                                   content_type='application/json')

        message = "Redemption Request to be edited must be provided"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 400)

    def test_edit_redemption_request_no_payload(self):
        """Test editing request without payload fails."""
        response = self.client.put(f"api/v1/societies/{self.sparks.uuid}",
                                   headers=self.society_president,
                                   content_type='application/json')

        message = "Data for editing must be provided"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 400)

    def test_delete_redemption_request(self):
        """Test deletion of Redemption Request is successful."""
        response = self.client.delete(
                        f"api/v1/societies/redeem/{self.redemp_req.uuid}",
                        headers=self.success_ops,
                        content_type='application/json'
                        )

        message = "deleted successfully"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)

    def test_delete_nonexistent_redemption_request(self):
        """Test deletion of non-existent Redemption Request fails."""
        response = self.client.delete(
                        "api/v1/societies/redeem/801029-203191-023032",
                        headers=self.success_ops,
                        content_type='application/json')

        message = "does not exist"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 404)

    def test_delete_redemption_request_no_id(self):
        """Test deletion request rejected with no ID provided."""
        response = self.client.delete("api/v1/societies/redeem",
                                      headers=self.success_ops,
                                      content_type='application/json')

        message = "RedemptionRequest id must be provided"
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 400)


class PointRedemptionApprovalTestCase(BaseTestCase):
    """Test class for Society point redemption approval/rejection."""

    def setUp(self):
        """Set up all needed variables."""
        BaseTestCase.setUp(self)
        self.president_role.save()
        self.v_president_role.save()
        self.successops_role.save()
        self.invictus.save()
        self.istelle.save()
        self.sparks.save()
        self.phoenix.save()
        self.redemp_req.save()

    def test_point_redemption_approval_successful(self):
        """Test approval of redemption request.

        When approved the value of the redemption request should reflect on the
        society._total_points.
        """
        approval_payload = dict(status="approved")

        response = self.client.put(
                    f"api/v1/societies/redeem/verify/{self.redemp_req.uuid}",
                    data=json.dumps(approval_payload),
                    headers=self.success_ops,
                    content_type='application/json'
        )

        message = "status changed to {}".format(approval_payload["status"])
        response_details = json.loads(response.data)

        self.assertIn(message, response_details["message"])
        self.assertEqual(response.status_code, 200)