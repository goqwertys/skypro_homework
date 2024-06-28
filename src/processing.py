from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(
    input_list: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """Returns filtered list of dicts if 'state' item contains state"""
    return [
        item
        for item in input_list
        if isinstance(item.get("state"), str) and item.get("state") == state
    ]


def sort_by_date(
    input_list: List[Dict[str, Any]], rev: bool = False
) -> List[Dict[str, Any]]:
    """Returns list of dicts sorted by 'date'"""
    return sorted(
        input_list,
        key=lambda x: (
            datetime.fromisoformat(x["date"])
            if "date" in x and isinstance(x["date"], str)
            else datetime.min
        ),
        reverse=rev,
    )


def sort_by_price_in_cat(input_list: List[dict], cat: str | None = None) -> List[dict]:
    """Returns sorted list of dicts in specified category"""
    categories = [x.get("category", None) for x in input_list]
    if cat is None:
        list_for_sort = input_list
    elif cat in categories:
        list_for_sort = [x for x in input_list if x.get("category") == cat]
    else:
        raise ValueError("Invalid category")
    return sorted(list_for_sort, key=lambda x: x.get("price", float("inf")))


def orders_info(orders: List[Dict]) -> Dict[str, Dict[str, float]]:
    """Returns dict of average order value and number of orders for each month"""
    monthly_data: Dict[str, Dict[str, float]] = {}
    result_data: Dict[str, Dict[str, float]] = {}
    for order in orders:
        # Get year and month of order
        year_month = datetime.fromisoformat(order["date"]).strftime("%Y-%m")
        # If the dictionary does not yet have an entry for the current month, create an empty dictionary
        if year_month not in monthly_data:
            monthly_data[year_month] = {"total_price": 0, "order_count": 0}
        # Calculate the total cost of the order
        total_order_price = sum(
            item["price"] * item["quantity"] for item in order["items"]
        )
        # Updating price and count
        monthly_data[year_month]["total_price"] += total_order_price
        monthly_data[year_month]["order_count"] += 1
    # Calculate the average order value for each month
    for month, stats in monthly_data.items():
        average_order_value = (
            stats["total_price"] / stats["order_count"]
            if stats["order_count"] > 0
            else 0
        )
        stats["average_order_value"] = average_order_value
    for key, value in monthly_data.items():
        result_data[key] = {
            "average_order_value": value["average_order_value"],
            "order_count": value["order_count"],
        }
    return result_data
