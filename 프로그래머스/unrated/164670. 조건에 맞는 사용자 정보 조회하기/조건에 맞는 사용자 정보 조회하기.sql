-- 코드를 입력하세요
select uu.user_id, uu.nickname, concat(uu.city, " ",uu.street_address1, " ", uu.street_address2) as "전체주소", concat(left(uu.tlno,3),"-",mid(uu.tlno,4,4),"-",right(uu.tlno,4)) as "전화번호"
from
(
SELECT writer_id, count(board_id) as cnt
from used_goods_board
group by writer_id) as tmp
join used_goods_user as uu
on tmp.writer_id = uu.user_id
where cnt >= 3
order by uu.user_id desc