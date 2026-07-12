SELECT title, username 
FROM tasks AS t
LEFT JOIN users as u
    ON t.user_id = u.id;