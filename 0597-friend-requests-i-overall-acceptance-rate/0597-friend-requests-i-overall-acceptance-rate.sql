# Write your MySQL query statement below
      
select 
round(
    ifnull(
    (select count(*) from (select distinct requester_id, accepter_id from RequestAccepted) AS A)
    /
    (select count(*) from (select distinct sender_id, send_to_id from FriendRequest) AS B),
    0)
    , 2) AS accept_rate
     
      