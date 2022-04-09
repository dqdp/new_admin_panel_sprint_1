
INSERT_TEMPLATE = 'INSERT INTO content.{0} ({1})  VALUES {2} ON CONFLICT (id) DO NOTHING;'

COLUMNS_FILMWORK = 'id, title, description, creation_date, file_path, rating, type, created, modified'

COLUMNS_GENRE = 'id, name, description, created, modified'

COLUMNS_GENRE_FILMWORK = 'id, genre_id, film_work_id, created'

COLUMNS_PERSON = 'id, full_name, created, modified'

COLUMNS_PERSON_FILMWORK = 'id, person_id, film_work_id, role, created'
