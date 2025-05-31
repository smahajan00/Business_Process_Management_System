# bpms_core.py

#data structures for products and sales
products = [
    {"id": 1, "name": "Wireless Mouse",   "category": "Electronics", "price": 25.99, "stock": 120},
    {"id": 2, "name": "USB-C Cable",      "category": "Electronics", "price": 9.50,  "stock": 200},
    {"id": 3, "name": "Cotton T-Shirt",   "category": "Clothing",    "price": 15.00, "stock": 80},
    {"id": 4, "name": "Jeans",            "category": "Clothing",    "price": 45.00, "stock": 60},
    {"id": 5, "name": "Ceramic Mug",      "category": "Home",        "price": 12.75, "stock": 150},
    {"id": 6, "name": "Blender",          "category": "Home",        "price": 55.00, "stock": 30},
]

sales_records = [
    {"product_id": 1, "quantity": 10},
    {"product_id": 2, "quantity": 25},
    {"product_id": 3, "quantity": 5},
    {"product_id": 5, "quantity": 12},
    {"product_id": 1, "quantity": 7},
    {"product_id": 4, "quantity": 3},
]

def search_inventory(category_filter=None, min_price=None, max_price=None):
    """
    Search for products that match the given filters.
    Returns a list of matching products.
    """
    matching = []
    for prod in products:
        # Filter by category if provided
        if category_filter is not None:
            if prod["category"] != category_filter:
                continue

        # Filter by price range if provided
        if min_price is not None and prod["price"] < min_price:
            continue
        if max_price is not None and prod["price"] > max_price:
            continue

        matching.append(prod)
    return matching

def generate_sales_report():
    """
    Generate and print a summary report of total quantities sold per category.
    """
    # Initialize counters for each category
    report = {"Electronics": 0, "Clothing": 0, "Home": 0, "Other": 0}

    # Build a lookup from product ID to category
    id_to_cat = {prod["id"]: prod["category"] for prod in products}

    # Aggregate sales by category
    for record in sales_records:
        pid = record["product_id"]
        qty = record["quantity"]
        category = id_to_cat.get(pid, "Other")

        if category == "Electronics":
            report["Electronics"] += qty
        elif category == "Clothing":
            report["Clothing"] += qty
        elif category == "Home":
            report["Home"] += qty
        else:
            report["Other"] += qty

    # Print the summary
    print("Sales Report Summary:")
    for cat, total_qty in report.items():
        print(f"  {cat}: {total_qty} units sold")

# Example usage:
if __name__ == "__main__":
    # 1) Search for all Electronics between $10 and $30
    results = search_inventory(category_filter="Electronics", min_price=10, max_price=30)
    print("Search Results (Electronics, $10–$30):")
    for p in results:
        print(f"  • {p['name']} (ID: {p['id']}), Price: ${p['price']:.2f}, Stock: {p['stock']}")

    print("\n")

    # 2) Generate the overall sales report
    generate_sales_report()
