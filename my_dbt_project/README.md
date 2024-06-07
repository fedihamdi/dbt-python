# DBT and Python Example

This repository contains an example project demonstrating how to use DBT with Python for data transformation.

## Project Structure
```
my_dbt_project/
├── models/
│ ├── staging/
│ │ └── stg_customers.sql
│ ├── marts/
│ │ └── customers/
│ │ └── customer_orders.sql
├── tests/
│ └── assert_customer_data.sql
├── macros/
│ └── my_custom_macro.sql
├── scripts/
│ └── data_validation.py
├── dbt_project.yml
└── README.md
```


## Running the Project

1. Configure your database connection in `data_validation.py`.
2. Initialize a DBT project: `dbt init`.
3. Run the DBT models: `dbt run`.

## Additional Resources

- [DBT Documentation](https://docs.getdbt.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

