# Use the official Microsoft SQL Server image from the Docker Hub
FROM mcr.microsoft.com/mssql/server:2019-latest

# Set environment variables required for SQL Server
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=admin@1234
ENV MSSQL_PID=Express

# Expose the SQL Server port (default 1433)
EXPOSE 1433

# Create a directory for the database backup and SQL scripts
RUN mkdir -p /usr/src/app

# Copy the database backup (.bak) or .mdf/.ldf files from your PC to the container
COPY ./RecoMaster.bak /usr/src/app/RecoMaster.bak

# If you have a SQL script for restoring the database or for creating users, copy that as well
COPY ./restore-database.sql /usr/src/app/restore-database.sql

# Make sure the container has access to necessary utilities like bash and SQLCMD
RUN apt-get update && apt-get install -y curl nano apt-utils

# Set permissions for the SQL scripts
RUN chmod +x /usr/src/app/restore-database.sql

# Run the SQL Server and restore the database
# 1. Start SQL Server.
# 2. Run a script to restore the database using SQLCMD and create users.
CMD /bin/bash -c "/opt/mssql/bin/sqlservr & sleep 30s; \
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P YourStrong@Passw0rd \
    -d master -i /usr/src/app/restore-database.sql; \
    wait"

