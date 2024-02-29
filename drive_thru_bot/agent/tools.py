from langchain_community.tools import tool
from typing import Any
from drive_thru_bot.agent.retriever import Retriever
from drive_thru_bot.pos.pos import POS
import ast
import chainlit as cl
import weaviate  # type: ignore
import weaviate.classes as wvc  # type: ignore

client = weaviate.connect_to_local()
retriever = Retriever(client=client, collection_name="Kfc_menu")


@tool
async def take_order(order_json_str: str) -> str:
    """
    Takes the order from the customer and repeats the customer's order, and ask if there is anything else you can help them with.
    """
    order = cl.user_session.get("order")

    # Convert string to list of dict
    list_of_items = ast.literal_eval(order_json_str.strip())
    for item in list_of_items:
        print(item)
        name = item["name"]
        meal_bool = item.get("meal", False)
        if meal_bool:
            filter = wvc.query.Filter.by_property("category").equal("Menus")
        else:
            filter = None

        res = (
            retriever.query(
                query=name,
                search_type="hybrid",
                query_properties=["name"],
                filters=filter,
                fusion_type=wvc.query.HybridFusion.RELATIVE_SCORE,
                alpha=0.1,
                limit=10,
                auto_limit=1,
            )
            .objects[0]
            .properties
        )

        info = {
            key: res.get(key, None)
            for key in res.keys()
            if key in ["name", "price", "available", "contents"]
        }
        info["quantity"] = item["quantity"]
        info["notes"] = item.get("notes", "None")
        order.append(info)
    order_summary = """Order:\n{}
          """.format(
        "\n".join(
            [
                "- "
                + f"{item['quantity']} x "
                + f"{item['name']}, Notes: {item['notes']}"
                for item in order
            ]
        )
    )

    cl.user_session.set("order", order)

    return order_summary


@tool
def confirm_order(any: Any) -> str:
    """
    Confirms the order to the customer, sends the order to the POS, and thank the customer and tell them to proceed to the next window.
    """
    order = cl.user_session.get("order")
    total_price = sum([item["price"] * item["quantity"] for item in order])
    pos_client = POS(endpoint="/order/3/orders/1")
    _ = pos_client.send_order_html(order)
    return f"Your order has been confirmed. Total price: {total_price} AED. Please move to the next window!"
