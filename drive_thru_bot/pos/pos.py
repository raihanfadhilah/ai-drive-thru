# from request_body import TEMPLATE as template #type: ignore
from dotenv import load_dotenv
from typing import List, Dict, Any, Union
from drive_thru_bot.pos.request_body import TEMPLATE as template  # type: ignore
import os
import requests  # type: ignore
import subprocess


class POS:
    """
    Point of Sale (POS) class for handling order processing and API communication.
    """

    def __init__(self, endpoint: str):
        """
        Initializes the class with the provided endpoint.

        Args:
            endpoint (str): The endpoint URL for the API.
        """
        self.endpoint = endpoint
        self.API_GATEWAY = os.getenv("API_GATEWAY")

    @property
    def headers(self) -> Dict[str, str | None]:
        """
        Returns the headers for the API request.

        Returns:
            Dict[str, str]: The headers for the API request.
        """
        load_dotenv(override=True)
        return {
            "nep-organization": os.getenv("BSP_ORGANIZATION"),
            "nep-enterprise-unit": os.getenv("BSP_SITE_ID"),
            "Authorization": os.getenv("BSP_ACCESS_KEY"),
            "Date": os.getenv("DATE"),
            "Content-Type": "application/json",
        }

    def format_http_body(self, list_of_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Formats the HTTP body for the API request based on the given list of items.

        Args:
            list_of_items (List[Dict[str, Any]]): A list of items, where each item is a dictionary containing the following keys:
                - 'name': The name of the item.
                - 'quantity': The quantity of the item.
                - 'price': The price of the item.
                - 'notes' (optional): Additional notes for the item.
                - 'Meal' (optional): A boolean indicating if the item is a meal.

        Returns:
            Dict[str, Any]: The formatted HTTP body as a dictionary.
        """
        order_lines: List[Dict[str, Any]] = []
        for item in list_of_items:
            product_id = {"type": "UPC", "value": item["name"]}
            quantity = {"unitOfMeasureLabel": "PCS", "value": item["quantity"]}
            unit_price = item["price"]
            extended_amount = item["quantity"] * item["price"]
            notes = [
                {"type": "Preferences", "value": item.get("notes", "None")},
                {
                    "type": "Other",
                    "typeLabel": "meal",
                    "value": item.get("meal", False),
                },
            ]

            order_lines.append(
                {
                    "productId": product_id,
                    "quantity": quantity,
                    "extendedAmount": extended_amount,
                    "notes": notes,
                    "unitPrice": unit_price,
                }
            )

        template["orderLines"] = order_lines

        return template

    def send_order_html(
        self, list_of_items: List[Dict[str, Any]]
    ) -> Union[dict[str, Any], None]:
        """
        Sends an order in HTML format to the API Gateway.

        Args:
            list_of_items (List[Dict[str, Any]]): A list of items in the order.

        Returns:
            Union[dict[str, Any], None]: The response from the API Gateway if the order was sent successfully,
            otherwise None.

        Raises:
            requests.exceptions.HTTPError: If there is an HTTP error while sending the order.
        """
        try:
            subprocess.run(["node", "prerequest.js"])  # Run the pre-request script
            response = requests.post(
                str(self.API_GATEWAY) + self.endpoint,
                headers=self.headers,
                json=template,
            )
            print("HTTP OK 200. Order sent successfully!")
            return response.json()

        except requests.exceptions.HTTPError as err:
            print(err)
            return None


if __name__ == "__main__":
    pos = POS(endpoint="/order/3/orders/1")
    order = [
        {
            "name": "Cheeseburger",
            "quantity": 3,
            "price": 20.8,
            "notes": "Lightly salted",
        },
        {"name": "Cola", "quantity": 1, "price": 5.5},
    ]
    pos.send_order_html(order)
