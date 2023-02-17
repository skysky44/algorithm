-- 코드를 입력하세요
SELECT
    MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM
    (SELECT *
    FROM APPOINTMENT
    WHERE
        YEAR(APNT_YMD)  = '2022'
        AND MONTH(APNT_YMD) = '5'
    ) AS APP
GROUP BY
    MCDP_CD
ORDER BY
    5월예약건수,
    진료과코드;
    