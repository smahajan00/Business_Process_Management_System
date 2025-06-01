import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

public class SalesReport {
    public static void main(String[] args) {
        String category = "Clothing";
        String start = "2025-05-01";
        String end = "2025-05-31";

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
        LocalDate startDate = LocalDate.parse(start, formatter);
        LocalDate endDate = LocalDate.parse(end, formatter);

        System.out.println("Generating report for: " + category);
        System.out.println("From " + startDate + " to " + endDate);
        // Simulated fixed output
        System.out.println("Total Units Sold: 342");
    }
}
