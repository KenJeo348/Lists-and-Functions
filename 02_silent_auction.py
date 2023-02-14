def main():
    auction_item = input("What is the auction for:")
    reserve_price = int(input(f"What is the reserve price for {auction_item}:"))
    print()
    auction(auction_item, reserve_price)


def auction(_auction_item, _reserve_price):
    bid = 0
    highest_bid = 0
    print(f"The auction for the {_auction_item} has started!\n"
          f"Bid a price of -1 to stop the bid.\n")

    while bid != -1:
        if bid >= highest_bid:
            highest_bid = bid
        else:
            print("*******************************\n"
                  "Please bid with a higher price:\n"
                  "*******************************\n")

        print(f"The highest bid so far is ${highest_bid}")
        bid = int(input("What is your bid:"))
        print()

    if highest_bid >= _reserve_price:
        print(f"The auction for the {_auction_item} has finished with a highest "
              f"bid of ${highest_bid}")
    elif highest_bid == _reserve_price:
        print(f"The auction for the {_auction_item} has finished with a highest "
              f"bid of ${highest_bid}")
    else:
        print("The object was not sold as the reserve price was not met.")


# Main Routine
main()
