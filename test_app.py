from sql_agent import (
    generate_sql,
    execute_query
)

query = input("Ask database: ")

sql_query = generate_sql(query)

print("\nGenerated SQL:")
print(sql_query)

results = execute_query(sql_query)

print("\nResults:")
print(results)