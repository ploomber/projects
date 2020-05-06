
query = """
select meta.track_id, term.* from artist_tag.artist_term term
join metadata.songs meta
using (artist_id)
limit 10;
"""

query = """
select meta.year, term.term, count(*)
from artist_tag.artist_term term
join metadata.songs meta
using (artist_id)
group by term.term
"""

query = """
with max_duration as (
select year, max(duration) as duration
from metadata.songs
group by year
)
select * from metadata.songs
join max_duration
using(year, duration)

"""
