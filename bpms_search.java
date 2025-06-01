List<Product> searchInventory(String categoryFilter, double minPrice, double maxPrice) {
    // 1: Create a list to store matching results
    List<Product> results = new ArrayList<>();

    // 2: Iterate over each product in the inventory
    for (Product p : allProducts) {
        // 3: Determine which category the product belongs to
        switch (p.getCategory()) {
            case "Electronics":
                // 4: Filter out Electronics products that do not meet price or stock criteria
                if (p.getPrice() < minPrice
                    || p.getPrice() > maxPrice
                    || p.getStock() == 0) {
                    // 5: If it fails, skip to the next product
                    break;
                }
                // 6: If it passes, add the Electronics product to the results
                results.add(p)
                break;

            case "Clothing":
                // 8: Filter out Clothing products that do not meet price or stock criteria
                if (p.getPrice() < minPrice
                    || p.getPrice() > maxPrice
                    || p.getStock() == 0) {
                    // 9: If it fails, skip to the next product
                    break;
                }
                // 10: If it passes, add the Clothing product to the results
                results.add(p);
                // 11: Exit this case and continue with the next product
                break;

            default:
                // 12: For any other category (e.g., "Home"), apply the same filters
                if (p.getPrice() < minPrice
                    || p.getPrice() > maxPrice
                    || p.getStock() == 0) {
                    // 13: If it fails, skip to the next product
                    break;
                }
                // 14: If it passes, add the “other” category product to the results
                results.add(p);
                // 15: Exit this case and continue with the next product
                break;
        }
    }

    // 16: Return the list of matching products
    return results;
}
