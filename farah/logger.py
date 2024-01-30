import csv
import os
from datetime import datetime

from farah.utils import create_csv

log_dir = "log"
header_row = ["date", "product_id", "type", "attr", "from", "to"]


def create_log_file(filename):
    create_csv(filename, log_dir, header_row)


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


def log_reactivated_product(product, end_date):
    today = datetime.today().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"{today}.csv")
    create_log_file(log_file)

    rows = []
    rows.append([today, product.id, "reactivated", "end_date", end_date, ""])
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


# source is where it was run from
def log_workflow_run(source):
    today = datetime.today().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, "workflow.csv")
    create_csv(log_file, log_dir, ["run_date", "source"])

    rows = []
    rows.append([today, source])
    append_rows(rows, log_file)
