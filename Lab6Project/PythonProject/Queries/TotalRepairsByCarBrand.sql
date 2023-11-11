SELECT
    Cars.CarBrand,
    COUNT(*) AS TotalRepairs
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
GROUP BY Cars.CarBrand;
