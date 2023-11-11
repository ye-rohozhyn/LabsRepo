SELECT
    Cars.CarID,
    Cars.CarBrand,
    SUM(Repairs.OneHourPrice * Repairs.Hours) AS TotalCost,
    SUM(Repairs.OneHourPrice * Repairs.Hours * (1 - Repairs.Discount)) AS TotalCostWithDiscount
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
GROUP BY Cars.CarID, Cars.CarBrand;
