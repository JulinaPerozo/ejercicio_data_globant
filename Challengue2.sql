#Challenge 2

#1

SELECT dep.department, j.job, QUARTER(DATETIME) AS Q
FROM hired_employees he
INNER JOIN departments dep ON he.department_id = dep.id
INNER JOIN jobs j ON he.job_id = j.id 
ORDER BY dep.department AND j.job

#2

SELECT d.department AS id , d.department, count(he.id) AS hired
FROM departments d
INNER JOIN hired_employees he ON d.id = he.department_id
ORDER BY hired DESC