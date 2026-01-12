# 6. Dashboard
## Step 1: Create a view to provide a specific subset of data for visualization 
<img src="image_06/query_in_new_tab.png" width=100% height=40%>
Code for creating a view (replace the Project and Dataset names with your own)

```sh
CREATE VIEW `road-to-data-engineer-sql-db.r2de3_ws6.ws6_view`
AS
SELECT
  TIMESTAMP_MICROS(CAST(date / 1000 AS INT64)) AS date_converted
  ,thb_amount
  ,transaction_id
  ,product_id
  ,product_name
  ,quantity
  ,customer_id
  ,customer_name
  ,customer_country
FROM `road-to-data-engineer-sql-db.r2de3_ws6.ws6_output`
WHERE total_amount > 0;
```
<img src="image_06/create_view.png" width=100% height=40%>
<img src="image_06/see_view.png" width=100% height=40%>

---

## Step 2: Create a dashboard
### Dashboard: Sales Performance
Dashboard summary:
- Total Sales Revenue
- Total Quantity Sold
- Sales Trend
- % Sales of Top Products
- Sales by Country
- Top 10 Products

<img src="image_06\sales_performance.jpg" width=100% height=40%>

### Dashboard: Customer Insight 
Dashboard summary:
- Unique Customers
- Average Basket Size
- Monthly Customer Number
- Customer Purchase Frequency
- Top Customers

<img src="image_06\customer_insight.jpg" width="100%" height="40%">