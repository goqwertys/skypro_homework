from src.masks import mask_account, mask_card
from src.widget import convert_iso_ddmmyyy, mask_card_or_acc_sring


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


if __name__ == "__main__":
    main()
