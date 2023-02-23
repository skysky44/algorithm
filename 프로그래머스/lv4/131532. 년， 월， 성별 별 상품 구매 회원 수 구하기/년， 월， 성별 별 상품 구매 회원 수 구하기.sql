-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, USER_INFO.GENDER, COUNT(DISTINCT USER_ID) AS USERS
FROM USER_INFO
INNER JOIN ONLINE_SALE
    USING (USER_ID)
GROUP BY
    YEAR, MONTH, GENDER
HAVING
    GENDER IS NOT NULL
ORDER BY
    YEAR, MONTH, GENDER;