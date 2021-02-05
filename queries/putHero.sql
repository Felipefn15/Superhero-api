UPDATE Hero
    SET 
        Description = IF('{1}' != '', '{1}',Description), 
        Favorite = IF('{2}' != '', '{2}',Favorite), 
        Image = IF('{3}' != '', '{3}',Image)
WHERE 
    Name = '{0}'