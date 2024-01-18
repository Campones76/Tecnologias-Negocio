
alter table dbo.Transactions
ADD FOREIGN KEY (CustomerID) REFERENCES dbo.Customer(CustomerID);
alter table dbo.LicenseRenewals
ADD FOREIGN KEY (CustomerID) REFERENCES dbo.Customer(CustomerID);
alter table dbo.CustomerFirearms
ADD FOREIGN KEY (CustomerID) REFERENCES dbo.Customer(CustomerID);
alter table dbo.Firearms
ADD FOREIGN KEY (CustomerID) REFERENCES dbo.Customer(CustomerID);

alter table dbo.Transactions
ADD FOREIGN KEY (FirearmID) REFERENCES dbo.Firearms(FirearmID);
alter table dbo.SecurityMeasures
ADD FOREIGN KEY (FirearmID) REFERENCES dbo.Firearms(FirearmID);
alter table dbo.CustomerFirearms
ADD FOREIGN KEY (FirearmID) REFERENCES dbo.Firearms(FirearmID);