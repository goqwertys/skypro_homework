from src.masks import mask_account, mask_card
from src.widget import convert_iso_ddmmyyy, mask_card_or_acc_sring
from src.processing import filter_by_state, sort_by_date, sort_by_price_in_cat


def main() -> None:
    # MASK CARD
    card_mask = mask_card("7000792289606361")
    print(card_mask)

    # MASK ACCOUNT
    acc_mask = mask_account("73654108430135874305")
    print(acc_mask)

    strings_to_match = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Счет 736541084301358743",
    ]
    for line in strings_to_match:
        try:
            masked_data = mask_card_or_acc_sring(line)
            print(masked_data)
        except ValueError as e:
            print(f"An error occurred: {e}")

    dates = [
        "2024-03-16T08:00:00Z",
        "2024-01-17T08:00:00Z",
        "2025-12-18T08:00:00Z",
        "1999-11-21T08:00:00Z",
        "1998-09-24T08:00:00Z",
        "2023-01-14T08:00:00Z",
        "2022-02-24T08:00:00Z",
        "2022-02T08:00:00Z",
    ]
    for date in dates:
        try:
            converted_date = convert_iso_ddmmyyy(date)
            print(converted_date)
        except ValueError as e:
            print(f"An error occurred: {e}")

    # FILTER TEST
    filter_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    filtered_data = filter_by_state(filter_test)
    print("filter_by_state() test\nfiltered by DEFAULT:")
    for item in filtered_data:
        print(item)
    print("filter_by_state() test\nfiltered by CANCELED:")
    filtered_data = filter_by_state(filter_test, state="CANCELED")
    for item in filtered_data:
        print(item)

    # SORT TEST
    print("sort_by_date() test:")
    sort_test = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    sorted_data = sort_by_date(sort_test)
    for item in sorted_data:
        print(item)

    list_of_dicts = [
        {"name": "apple", "price": 3.0, "category": "fruit", "quantity": 5},
        {"name": "orange", "price": 4.0, "category": "fruit", "quantity": 10},
        {"name": "potato", "price": 1.2, "category": "vegetable", "quantity": 30},
        {"name": "mango", "price": 7.0, "category": "fruit", "quantity": 3},
    ]
    # TEST sort_by_price_in_cat() with no category
    sorted_in_category = sort_by_price_in_cat(list_of_dicts)
    for item in sorted_in_category:
        print(item)
    # TEST sort_by_price_in_cat() with specified category
    sorted_in_category = sort_by_price_in_cat(list_of_dicts, "fruit")
    for item in sorted_in_category:
        print(item)


if __name__ == "__main__":
    main()
