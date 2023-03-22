-- 코드를 입력하세요
SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, date_format(b.created_date, '%Y-%m-%d') as CREATED_DATE
from used_goods_board as a
inner join used_goods_reply as b
on a.board_id = b.board_id
where a.CREATED_DATE between '2022-10-01' and '2022-10-31'
order by created_date asc, title asc;