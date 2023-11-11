SELECT Clients.ClientID, Clients.ClientCompany, SUM(Repairs.OneHourPrice * Repairs.Hours) AS TotalAmountPaid
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
JOIN Clients ON Cars.ClientID = Clients.ClientID
GROUP BY Clients.ClientID, Clients.ClientCompany;