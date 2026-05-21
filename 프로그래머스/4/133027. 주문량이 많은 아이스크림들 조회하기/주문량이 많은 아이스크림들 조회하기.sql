-- 코드를 입력하세요
select flavor
from (
SELECT j.FLAVOR, j.TOTAL_ORDER as ii, fh.TOTAL_ORDER as iii
from (
    select flavor, sum(total_order) as total_order
    from july
    group by flavor
) j
join (
    select flavor, sum(total_order) as total_order
    from FIRST_HALF
    group by flavor
    ) fh
on fh.flavor = j.flavor
order by j.TOTAL_ORDER + fh.TOTAL_ORDER desc
)
where rownum <= 3;
