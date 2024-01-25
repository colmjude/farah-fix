import csv
import os
from datetime import datetime

log_dir = "log"
header_row = ["date", "product_id", "type", "attr", "from", "to"]


def create_log_file(filename):
    # make sure the directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    if not os.path.exists(filename):
        # Create the file and write the header row
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header_row)


def append_rows(rows, filename):
    # Append new rows to the CSV file
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def log_new_product(log):
    log_file = os.path.join(log_dir, f"{log['date']}.csv")
    create_log_file(log_file)

    rows = []
    for change in log["log"]:
        rows.append(
            [log["date"], log["product"], "new", change["attr"], change["from"], ""]
        )

    append_rows(rows, log_file)


def log_product_changes(log):
    log_file = os.path.join(log_dir, f"{log['date']}.csv")
    create_log_file(log_file)

    rows = []
    for change in log["log"]:
        rows.append(
            [
                log["date"],
                log["product"],
                "change",
                change["attr"],
                change["from"],
                change["to"],
            ]
        )

    append_rows(rows, log_file)


def log_price_change(product):
    today = datetime.today().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"{today}.csv")
    create_log_file(log_file)

    rows = []
    previous_price = "" if len(product.prices) == 1 else product.prices[-2].price
    latest_price = product.prices[-1].price
    rows.append([today, product.id, "new-price", "price", previous_price, latest_price])

    append_rows(rows, log_file)
