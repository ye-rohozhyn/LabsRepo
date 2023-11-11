SELECT Repairs.*, Clients.ClientCompany
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
JOIN Clients ON Cars.ClientID = Clients.ClientID
WHERE Repairs.WarrantyRepair = 1
ORDER BY Clients.ClientCompany;
