import pysynth_b  as psb


song = (
    ('g4', 8), ('c4', 8), ('eb4', 8), ('d4', 8),  ('c4', 8),('eb4', 8), ('c4', 8), ('d4', 8),
    ('c4', 8),  ('ab4', 8),  ('bb4', 8),  ('g4', 2), ('g4', 8),  ('c4', 8),  ('eb4', 8),  ('d4', 8),  ('c4', 8), 
    ('eb4', 8),  ('d4', 8),  ('c4', 8),  ('g4', 8),  ('f#', 8)
  , ('f4', 2),  ('f4', 8), ('ab4', 8), ('b4', 8), ('d4', 4), ('f4', 8), ('ab4', 8), ('b4', 8), ('c4', 4), ('c4', 8)
  , ('eb4', 8), ('bb4', 8), ('ab4', 8), ('g4', 8), ('bb4', 8), ('ab4', 8), ('ab4', 8), ('g4', 8), ('g4', 8)
  , ('f#', 8), ('g4', 4), ('g4', 8), ('c4', 8), ('eb4', 8), ('d4', 8), ('c4', 8),('eb4', 8), ('c4', 8),('d4', 8), ('c4', 8)
  ,('ab4', 8), ('bb4', 8), ('g4', 8),('g4', 8), ('c4', 8), ('eb4', 8), ('d4', 8),  ('c4', 8),('eb4', 8), ('c4', 8), ('d4', 8),
    ('c4', 8) ,('g4', 8),  ('f#', 8)
  , ('f4', 4), ('ab4', 8), ('b4', 8), ('d4', 4),  ('f4', 8), ('ab4', 8), ('b4', 8), ('c4', 8)
  , ('c4', 8), ('eb4', 8), ('bb4', 8),  ('ab4', 8), ('g4', 8), ('bb4', 8),  ('ab4', 8), ('g4', 4)
  , ('b4', 8), ('c4', 4), ('b4', 8), ('bb4', 8),  ('d4', 8), ('c4', 4), ('ab4', 8), ('g4', 6)
)
# Beats per minute (bpm) is really quarters per minute here
psb.make_wav(song, fn = "godfather.wav", leg_stac = .9, bpm = 83)