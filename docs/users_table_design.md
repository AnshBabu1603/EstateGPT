# Users Table Design

## Purpose

The Users table stores every employee who can log into the EstateGPT application.

## Columns

### UserID
Type: INTEGER
Purpose: Unique identifier for each user.

### FullName
Type: VARCHAR
Purpose: Stores the employee's full name.

### Email
Type: VARCHAR
Purpose: Used for login and communication.

### Password
Type: VARCHAR
Purpose: Stores the hashed password.

### Phone
Type: VARCHAR
Purpose: Stores the employee's phone number.

### RoleID
Type: INTEGER
Purpose: Connects the user to a role.

### IsActive
Type: BOOLEAN
Purpose: Indicates whether the account is active.

### CreatedAt
Type: TIMESTAMP
Purpose: Stores when the account was created.