# EstateGPT Database Design

## Why do we need a database?

A real estate company manages customers, properties, sales agents, leads, site visits, deals, and documents. To organize this information efficiently, the application stores it in a database using separate tables.

---

## Tables

### 1. Users

Purpose:
Stores employees who use the system, such as Admins, Sales Managers, and Sales Agents.

---

### 2. Roles

Purpose:
Defines what permissions each user has in the application.

---

### 3. Customers

Purpose:
Stores customer details such as name, phone number, budget, preferred location, and property requirements.

---

### 4. Properties

Purpose:
Stores all available property information.

---

### 5. Leads

Purpose:
Represents customer interest in a property and tracks the sales process.

---

### 6. Site Visits

Purpose:
Stores scheduled property visits for customers.

---

### 7. Deals

Purpose:
Stores completed property sales and booking information.

---

### 8. Activities

Purpose:
Keeps a history of calls, emails, meetings, and follow-ups.

---

### 9. Documents

Purpose:
Stores brochures, payment plans, legal papers, and other files used by the AI assistant.