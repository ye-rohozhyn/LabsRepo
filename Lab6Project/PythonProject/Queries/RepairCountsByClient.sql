SELECT
    Clients.ClientID,
    Clients.ClientCompany,
    COUNT(CASE WHEN Repairs.RepairType = 'Type1' THEN 1 END) AS Type1Count,
    COUNT(CASE WHEN Repairs.RepairType = 'Type2' THEN 1 END) AS Type2Count,
    COUNT(CASE WHEN Repairs.RepairType = 'Type3' THEN 1 END) AS Type3Count,
    COUNT(CASE WHEN Repairs.RepairType = 'Type4' THEN 1 END) AS Type4Count,
    COUNT(*) AS TotalRepairs
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
JOIN Clients ON Cars.ClientID = Clients.ClientID
GROUP BY Clients.ClientID, Clients.ClientCompany;
