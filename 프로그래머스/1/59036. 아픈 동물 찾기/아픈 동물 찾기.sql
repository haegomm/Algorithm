SELECT  ANIMAL_ID AS ANIMAL_ID,
        NAME      AS NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID