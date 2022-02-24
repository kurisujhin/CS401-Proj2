wget --server-response \
--output-document response.out \
--header='Content-Type: application/json' \
--post-data '{"text":"#covid19 new york"}' \
http://10.106.147.48:5018/api/american;
cat response.out