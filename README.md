# Azure Random Facts Generator

Random fact generator website built in flask with backend in Azure SQL.

![Alt Text](https://github.com/JanBenisek/AzureDB/blob/master/example.gif)

### How get the infrastructure running:
  - With the code below, we create resource group and create a SQL server with firewall
  - Default firewall settings and never let anyone in, so we need to add our IP
  - Don't know yours? Try `curl ipinfo.io/ip`

```
az login 
$location="westeurope" 
$resource="resource-randomfacts" 
$server="server-randomfacts"
$database="database-randomfacts"

$login="azureadmin"
$password="Password123!"

$startIP=[your-ip]
$endIP=[your-ip] 

echo "Creating $resource..."
az group create --name $resource --location "$location"

echo "Creating $server in $location..."
az sql server create --name $server --resource-group $resource --location "$location" --admin-user $login --admin-password $password

echo "Configuring firewall..."
az sql server firewall-rule create --resource-group $resource --server $server -n AllowYourIp --start-ip-address $startIP --end-ip-address $endIP

echo "Creating $database on $server..."
az sql db create --resource-group $resource --server $server --name $database --edition Basic --capacity 5 --zone-redundant false
```

### Query the DB:
  - Use the `sqlcmd` utility:
    - `sqlcmd -S "$server.database.windows.net" -d $database -U $login -P $password`

### Import data
  - We first create the tables (in our case, just one with all the random facts)
    - Do not use `;` and always use GO
    - `CREATE TABLE randomFacts(fact_key VARCHAR(50) NOT NULL, fact_source VARCHAR(500) NOT NULL, fact_text VARCHAR(500) NOT NULL)`
    - `GO`
  - After we can do the import:
    - `bcp "$database.dbo.randomFacts" in "C:/Users/benis/GitHub/AzureDB/data/facts.csv" -S "$server.database.windows.net" -U $login -P $password -q -c -t ";"`

### Run the app
  - Localy, just run `python app.py` and become the coolest person in the room, instantly!
  - Or build a Web App in Azure and deploy it with Kudu

### Useful resources:
  - https://getbootstrap.com/2.3.2/examples/justified-nav.html
  - https://www.tutorialspoint.com/flask/flask_quick_guide.htm
  - https://docs.microsoft.com/en-us/sql/tools/sqlcmd-utility?view=sql-server-ver15
