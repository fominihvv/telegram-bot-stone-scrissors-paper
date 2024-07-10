create_new_table = '''CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL, 
    total_games INTEGER NOT NULL,
    total_wins INTEGER NOT NULL, 
    total_loses INTEGER NOT NULL,
    total_draws INTEGER NOT NULL)'''

get_user_data = '''SELECT * FROM users WHERE user_id = ?'''

update_user_data = '''UPDATE users 
                       SET 'total_games' = ?, 
                       'total_wins' = ?, 
                       'total_loses' = ?,
                       'total_draws' = ? WHERE user_id = ?'''

new_user = '''INSERT INTO users (user_id, user_name, total_games, total_wins, 
                                 total_loses, total_draws) 
                                 VALUES (?, ?, ?, ?, ?, ?)'''
