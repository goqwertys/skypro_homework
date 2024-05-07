from src.masks import mask_account, mask_card
from src.widget import get_masked_card_from_str


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
    ]
    for line in strings_to_match:
        print(get_masked_card_from_str(line))


if __name__ == "__main__":
    main()
