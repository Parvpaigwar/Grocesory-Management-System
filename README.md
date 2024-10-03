# Grocery Store Management System

## Overview
The **Grocery Store Management System** is a full-stack web application designed to streamline the management of grocery store operations. This system enables store administrators to manage products, track inventory, handle customer orders, and monitor sales trends efficiently. The platform also includes data analytics to provide insights into product performance and optimize store management. The application is built using **Flask** for the backend, **MySQL** as the database, and **HTML, CSS, Bootstrap, and JavaScript** for the frontend.

## Features
- **Inventory Management:**  
  Track stock levels for grocery items, with options to add, update, or delete products from the inventory.
  
- **Order Processing:**  
  Manage customer orders, including placing new orders, updating order statuses, and generating invoices.

- **Customer Management:**  
  Maintain a database of customer information, including purchase history and preferences, to enhance customer relationship management.

- **Sales Analytics:**  
  Monitor sales data to gain insights into top-selling products, low stock items, and seasonal trends, enabling better decision-making.

- **Cross-Platform Accessibility:**  
  The application is optimized for use on various devices, ensuring smooth operations from desktops, tablets, and mobile devices.

## Tech Stack
- **Frontend:**
  - **HTML, CSS, Bootstrap** – for responsive and user-friendly design.
  - **JavaScript** – for enhanced interactivity and dynamic features.

- **Backend:**
  - **Flask** – for handling the server-side logic and API endpoints.
  - **Python** – for integrating various functionalities like data processing and order management.

- **Database:**
  - **MySQL** – for storing and managing product, order, and customer data.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Parvpaigwar/Grocesory-Management-System.git
   cd Grocesory-Management-System
   ```

2. **Install Dependencies:**
   Ensure you have Python and MySQL installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup:**
   - Set up a MySQL database and update the database credentials in the project’s configuration file.
   - Run the provided SQL script to create necessary tables for the system:
     ```bash
     mysql -u <username> -p < database_name> < db_schema.sql
     ```

4. **Run the Application:**
   Start the Flask development server:
   ```bash
   flask run
   ```

5. **Access the System:**
   Open your browser and go to `http://127.0.0.1:5000/` to access the Grocery Store Management System.

## Usage

### Inventory Management
- **Add Product:** Add new products by entering details such as name, category, price, stock, and description.
- **Update Product:** Update the product's information, including stock levels and prices.
- **Delete Product:** Remove products from the inventory if they are no longer available for sale.

### Customer Orders
- **Place Orders:** Customers can place orders by selecting products from the inventory and adding them to their cart.
- **Track Orders:** View all active orders and update their status (e.g., processing, shipped, completed).
- **Invoices:** Generate printable invoices for customer orders.

### Sales Analytics
- **Dashboard Overview:** Get insights into daily sales, total revenue, and popular products through interactive charts and tables.
- **Low Stock Alerts:** Automatically receive alerts when inventory levels are below a set threshold.
  
## Screenshots
(Add screenshots of your application here, showing key features like inventory management, order processing, and sales analytics dashboard.)

## Future Improvements
- **User Authentication:**  
  Implementing role-based access for admins and staff to ensure secure operations.

- **Advanced Analytics:**  
  Integrating more detailed analytics like customer behavior analysis and predictive sales trends.

- **Payment Gateway Integration:**  
  Adding online payment options for faster transactions.

## Contributing
Feel free to fork this repository and contribute to it by submitting a pull request. Please ensure you follow proper coding conventions and include tests where necessary.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


