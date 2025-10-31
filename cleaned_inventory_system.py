import json
import logging
from datetime import datetime

# Configure logging once
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

stock_data = {}

def add_item(item: str, qty: int = 0, logs=None):
    """Add quantity of a specific item to the stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid item or quantity type for add_item: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)

def remove_item(item: str, qty: int):
    """Remove quantity of an item from stock safely."""
    try:
        if item not in stock_data:
            logging.warning("Attempted to remove non-existing item: %s", item)
            return

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed all stock of %s", item)
        else:
            logging.info("Removed %d of %s", qty, item)
    except KeyError as e:
        logging.error("Item not found: %s", e)
    except TypeError as e:
        logging.error("Invalid quantity type: %s", e)

def get_qty(item: str):
    """Return quantity of given item if it exists."""
    return stock_data.get(item, 0)

def load_data(file_path: str = "inventory.json"):
    """Load inventory data from file."""
    global stock_data
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        logging.info("Loaded inventory from %s", file_path)
    except FileNotFoundError:
        logging.warning("File not found: %s", file_path)
    except json.JSONDecodeError as e:
        logging.error("JSON decode error: %s", e)

def save_data(file_path: str = "inventory.json"):
    """Save inventory data to file."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        logging.info("Saved inventory to %s", file_path)
    except OSError as e:
        logging.error("Failed to save file: %s", e)

def print_data():
    """Print current stock report."""
    print("Items Report:")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold: int = 5):
    """Return list of items below threshold quantity."""
    return [item for item, qty in stock_data.items() if qty < threshold]

def main():
    """Demonstration of inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()

if __name__ == "__main__":
    main()
