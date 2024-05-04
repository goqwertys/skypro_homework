from src.masks import mask_account, mask_card


def main() -> None:
    # MASK CARD
    card_mask = mask_card("7000792289606361")
    print(card_mask)

    # MASK ACCOUNT
    acc_mask = mask_account("73654108430135874305")
    print(acc_mask)


if __name__ == "__main__":
    main()
