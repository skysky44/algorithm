-- 코드를 입력하세요
SELECT 
    B.TITLE, BOARD_ID, REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM
    USED_GOODS_REPLY AS R
INNER JOIN USED_GOODS_BOARD AS B
    
    USING (BOARD_ID)

WHERE DATE_FORMAT(B.CREATED_DATE, '%Y-%m') = '2022-10'

ORDER BY R.CREATED_DATE , B.TITLE ;