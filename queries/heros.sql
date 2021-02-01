select
    Name as 'Name',
    Description as 'Description',
    Favorite as 'Favorite',
    Image as 'Image'
from Hero
where
    ('{0}' = '' or name like '%{0}%') and
    ('{1}' = '' or favorite = true)