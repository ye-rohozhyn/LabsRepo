SELECT Repairs.*, Cars.CarBrand
FROM Repairs
JOIN Cars ON Repairs.CarID = Cars.CarID
WHERE Cars.CarBrand = :desiredCarBrand;
