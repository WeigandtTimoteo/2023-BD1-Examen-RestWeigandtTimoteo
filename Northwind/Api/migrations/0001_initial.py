# Generated by Django 4.2.7 on 2023-11-22 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryid', models.AutoField(db_column='CategoryID', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(db_column='CategoryName', max_length=15)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('picture', models.TextField(blank=True, db_column='Picture', null=True)),
            ],
            options={
                'db_table': 'Categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customerdemographics',
            fields=[
                ('customertypeid', models.CharField(db_column='CustomerTypeID', max_length=10, primary_key=True, serialize=False)),
                ('customerdesc', models.TextField(blank=True, db_column='CustomerDesc', null=True)),
            ],
            options={
                'db_table': 'CustomerDemographics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerid', models.CharField(db_column='CustomerID', max_length=5, primary_key=True, serialize=False)),
                ('companyname', models.CharField(db_column='CompanyName', max_length=40)),
                ('contactname', models.CharField(blank=True, db_column='ContactName', max_length=30, null=True)),
                ('contacttitle', models.CharField(blank=True, db_column='ContactTitle', max_length=30, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=15, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=24, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=24, null=True)),
            ],
            options={
                'db_table': 'Customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeid', models.AutoField(db_column='EmployeeID', primary_key=True, serialize=False)),
                ('lastname', models.CharField(db_column='LastName', max_length=20)),
                ('firstname', models.CharField(db_column='FirstName', max_length=10)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=30, null=True)),
                ('titleofcourtesy', models.CharField(blank=True, db_column='TitleOfCourtesy', max_length=25, null=True)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('hiredate', models.DateTimeField(blank=True, db_column='HireDate', null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=15, null=True)),
                ('homephone', models.CharField(blank=True, db_column='HomePhone', max_length=24, null=True)),
                ('extension', models.CharField(blank=True, db_column='Extension', max_length=4, null=True)),
                ('photo', models.TextField(blank=True, db_column='Photo', null=True)),
                ('notes', models.TextField(db_column='Notes')),
                ('photopath', models.CharField(blank=True, db_column='PhotoPath', max_length=255, null=True)),
                ('salary', models.FloatField(blank=True, db_column='Salary', null=True)),
            ],
            options={
                'db_table': 'Employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.AutoField(db_column='OrderID', primary_key=True, serialize=False)),
                ('orderdate', models.DateTimeField(blank=True, db_column='OrderDate', null=True)),
                ('requireddate', models.DateTimeField(blank=True, db_column='RequiredDate', null=True)),
                ('shippeddate', models.DateTimeField(blank=True, db_column='ShippedDate', null=True)),
                ('freight', models.DecimalField(blank=True, db_column='Freight', decimal_places=4, max_digits=10, null=True)),
                ('shipname', models.CharField(blank=True, db_column='ShipName', max_length=40, null=True)),
                ('shipaddress', models.CharField(blank=True, db_column='ShipAddress', max_length=60, null=True)),
                ('shipcity', models.CharField(blank=True, db_column='ShipCity', max_length=15, null=True)),
                ('shipregion', models.CharField(blank=True, db_column='ShipRegion', max_length=15, null=True)),
                ('shippostalcode', models.CharField(blank=True, db_column='ShipPostalCode', max_length=10, null=True)),
                ('shipcountry', models.CharField(blank=True, db_column='ShipCountry', max_length=15, null=True)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.AutoField(db_column='ProductID', primary_key=True, serialize=False)),
                ('productname', models.CharField(db_column='ProductName', max_length=40)),
                ('quantityperunit', models.CharField(blank=True, db_column='QuantityPerUnit', max_length=20, null=True)),
                ('unitprice', models.DecimalField(blank=True, db_column='UnitPrice', decimal_places=4, max_digits=10, null=True)),
                ('unitsinstock', models.SmallIntegerField(blank=True, db_column='UnitsInStock', null=True)),
                ('unitsonorder', models.SmallIntegerField(blank=True, db_column='UnitsOnOrder', null=True)),
                ('reorderlevel', models.SmallIntegerField(blank=True, db_column='ReorderLevel', null=True)),
                ('discontinued', models.TextField(db_column='Discontinued')),
            ],
            options={
                'db_table': 'Products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('regionid', models.IntegerField(db_column='RegionID', primary_key=True, serialize=False)),
                ('regiondescription', models.CharField(db_column='RegionDescription', max_length=50)),
            ],
            options={
                'db_table': 'Region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('shipperid', models.AutoField(db_column='ShipperID', primary_key=True, serialize=False)),
                ('companyname', models.CharField(db_column='CompanyName', max_length=40)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=24, null=True)),
            ],
            options={
                'db_table': 'Shippers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplierid', models.AutoField(db_column='SupplierID', primary_key=True, serialize=False)),
                ('companyname', models.CharField(db_column='CompanyName', max_length=40)),
                ('contactname', models.CharField(blank=True, db_column='ContactName', max_length=30, null=True)),
                ('contacttitle', models.CharField(blank=True, db_column='ContactTitle', max_length=30, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=60, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=15, null=True)),
                ('region', models.CharField(blank=True, db_column='Region', max_length=15, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=10, null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=15, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=24, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=24, null=True)),
                ('homepage', models.TextField(blank=True, db_column='HomePage', null=True)),
            ],
            options={
                'db_table': 'Suppliers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Territories',
            fields=[
                ('territoryid', models.CharField(db_column='TerritoryID', max_length=20, primary_key=True, serialize=False)),
                ('territorydescription', models.CharField(db_column='TerritoryDescription', max_length=50)),
            ],
            options={
                'db_table': 'Territories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customercustomerdemo',
            fields=[
                ('customerid', models.OneToOneField(db_column='CustomerID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Api.customers')),
            ],
            options={
                'db_table': 'CustomerCustomerDemo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employeeterritories',
            fields=[
                ('employeeid', models.OneToOneField(db_column='EmployeeID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Api.employees')),
            ],
            options={
                'db_table': 'EmployeeTerritories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('orderid', models.OneToOneField(db_column='OrderID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='Api.orders')),
                ('unitprice', models.DecimalField(db_column='UnitPrice', decimal_places=4, max_digits=10)),
                ('quantity', models.SmallIntegerField(db_column='Quantity')),
                ('discount', models.FloatField(db_column='Discount')),
            ],
            options={
                'db_table': 'OrderDetails',
                'managed': False,
            },
        ),
    ]
