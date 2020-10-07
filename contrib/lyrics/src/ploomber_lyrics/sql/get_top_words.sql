attach database '{{upstream["raw_artist_tags_db"]}}' as artist_tag;
attach database '{{upstream["raw_metadata_db"]}}' as metadata;
attach database '{{upstream["raw_db"]}}' as lyrics;

-- '{{artist_name_}}'

drop table if exists {{product}};

create table {{product}} as

with tracks_from_artist as (
    select * from metadata.songs
    where artist_name = '{{artist_name}}'
)

select word, sum(count) as count
from lyrics.lyrics
join tracks_from_artist
using (track_id)
group by word;

