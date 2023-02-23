-- 코드를 입력하세요
SELECT APNT_NO, PT_NAME, PT_NO, APPOINTMENT.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT
INNER JOIN PATIENT
    USING (PT_NO)
INNER JOIN DOCTOR
    ON DOCTOR.DR_ID = APPOINTMENT.MDDR_ID
WHERE
    DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'
    AND APNT_CNCL_YN = 'N'
ORDER BY
    APNT_YMD
    