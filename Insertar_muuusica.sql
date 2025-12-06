USE muuusica;
INSERT INTO generos (nombre, imagen_path) VALUES
('Rock', 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=300'),
('Pop', 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=300'),
('Jazz', 'https://images.unsplash.com/photo-1415201364774-f6f0bb35f28f?w=300'),
('Hip-hop', 'https://images.unsplash.com/photo-1571608971218-df35abe11326?w=300'),
('Electronic', 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=300'),
('Classical', 'https://images.unsplash.com/photo-1519683384663-1a0ec7d3e54a?w=300'),
('Reggae', 'https://images.unsplash.com/photo-1501612780327-45045538702b?w=300'),
('Metal', 'https://images.unsplash.com/photo-1506091403742-e3aa39518db5?w=300'),
('Country', 'https://images.unsplash.com/photo-1516924962500-2b4b3b99ea02?w=300'),
('R&B', 'https://images.unsplash.com/photo-1571330735066-03aaa9429d89?w=300');

-- ========================================
-- 2. INSERTAR ARTISTAS (15 artistas variados)
-- ========================================
INSERT INTO artistas (nombre, biografia, sitio_web_url) VALUES
('The Rockers', 'Banda legendaria de rock formada en 1970', 'www.therockers.com'),
('Pop Princess', 'Artista pop con múltiples premios Grammy', 'www.popprincess.com'),
('Jazz Masters', 'Trío de jazz clásico de Nueva Orleans', 'www.jazzmasters.com'),
('MC Flow', 'Rapero underground del Bronx', 'www.mcflow.com'),
('DJ Electron', 'Productor de música electrónica', 'www.djelectron.com'),
('Orchestra Simphonia', 'Orquesta clásica de renombre mundial', 'www.simphonia.com'),
('Bob Reggaeman', 'Leyenda del reggae jamaicano', 'www.bobreggeaman.com'),
('Metal Heads', 'Banda de metal pesado', 'www.metalheads.com'),
('Country Roads', 'Dúo country tradicional', 'www.countryroads.com'),
('Smooth Soul', 'Cantante de R&B y soul', 'www.smoothsoul.com'),
('Indie Dreams', 'Banda indie alternativa', 'www.indiedreams.com'),
('Latin Fire', 'Grupo de música latina', 'www.latinfire.com'),
('Blues Brothers', 'Dúo de blues clásico', 'www.bluesbrothers.com'),
('Funk Master', 'Artista de funk y disco', 'www.funkmaster.com'),
('Acoustic Sessions', 'Cantautor acústico', 'www.acousticsessions.com');

-- ========================================
-- 3. INSERTAR ÁLBUMES (20 álbumes)
-- ========================================
INSERT INTO albumes (titulo, imagen_portada_path, fecha_lanzamiento, permitir_descarga) VALUES
('Rock Revolution', 'https://via.placeholder.com/300?text=Rock+Revolution', '2023-01-15', TRUE),
('Pop Sensation', 'https://via.placeholder.com/300?text=Pop+Sensation', '2023-02-20', TRUE),
('Jazz Nights', 'https://via.placeholder.com/300?text=Jazz+Nights', '2023-03-10', FALSE),
('Urban Flow', 'https://via.placeholder.com/300?text=Urban+Flow', '2023-04-05', TRUE),
('Electronic Dreams', 'https://via.placeholder.com/300?text=Electronic+Dreams', '2023-05-12', TRUE),
('Classical Masterpieces', 'https://via.placeholder.com/300?text=Classical', '2023-06-18', FALSE),
('Reggae Vibes', 'https://via.placeholder.com/300?text=Reggae+Vibes', '2023-07-22', TRUE),
('Metal Mayhem', 'https://via.placeholder.com/300?text=Metal+Mayhem', '2023-08-30', TRUE),
('Country Tales', 'https://via.placeholder.com/300?text=Country+Tales', '2023-09-14', TRUE),
('R&B Grooves', 'https://via.placeholder.com/300?text=R&B+Grooves', '2023-10-08', TRUE),
('Greatest Hits', 'https://via.placeholder.com/300?text=Greatest+Hits', '2023-11-01', TRUE),
('Summer Mix', 'https://via.placeholder.com/300?text=Summer+Mix', '2023-11-15', FALSE),
('Acoustic Live', 'https://via.placeholder.com/300?text=Acoustic+Live', '2023-12-01', TRUE),
('Dance Party', 'https://via.placeholder.com/300?text=Dance+Party', '2023-12-10', TRUE),
('Chill Out', 'https://via.placeholder.com/300?text=Chill+Out', '2024-01-05', TRUE),
('Rock Anthems', 'https://via.placeholder.com/300?text=Rock+Anthems', '2024-01-20', TRUE),
('Pop Classics', 'https://via.placeholder.com/300?text=Pop+Classics', '2024-02-14', FALSE),
('Jazz Fusion', 'https://via.placeholder.com/300?text=Jazz+Fusion', '2024-03-01', TRUE),
('Hip Hop Beats', 'https://via.placeholder.com/300?text=Hip+Hop+Beats', '2024-03-15', TRUE),
('Electronic Pulse', 'https://via.placeholder.com/300?text=Electronic+Pulse', '2024-04-01', TRUE);

-- ========================================
-- 4. INSERTAR CANCIONES (50 canciones - 5 por género)
-- ========================================
-- Rock (Album 1)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(1, 'Thunder Road', '04:23', '/music/rock/thunder_road.mp3', 8500000, 1500, TRUE),
(1, 'Electric Heart', '03:45', '/music/rock/electric_heart.mp3', 7200000, 2300, TRUE),
(1, 'Rebel Soul', '05:12', '/music/rock/rebel_soul.mp3', 9800000, 890, TRUE),
(1, 'Highway Star', '04:08', '/music/rock/highway_star.mp3', 7900000, 3400, TRUE),
(16, 'Rock Forever', '03:55', '/music/rock/rock_forever.mp3', 7500000, 1200, TRUE);

-- Pop (Album 2)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(2, 'Summer Love', '03:20', '/music/pop/summer_love.mp3', 6400000, 5600, TRUE),
(2, 'Dancing Queen', '03:35', '/music/pop/dancing_queen.mp3', 6900000, 8900, TRUE),
(2, 'Starlight', '03:15', '/music/pop/starlight.mp3', 6200000, 4300, TRUE),
(17, 'Pop Magic', '03:28', '/music/pop/pop_magic.mp3', 6600000, 2100, FALSE),
(17, 'Rainbow Sky', '03:42', '/music/pop/rainbow_sky.mp3', 7100000, 3700, TRUE);

-- Jazz (Album 3)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(3, 'Blue Moon', '06:45', '/music/jazz/blue_moon.mp3', 12900000, 780, FALSE),
(3, 'Smooth Jazz', '05:30', '/music/jazz/smooth_jazz.mp3', 10500000, 1100, FALSE),
(3, 'Night Cafe', '07:12', '/music/jazz/night_cafe.mp3', 13800000, 560, FALSE),
(18, 'Jazz Fusion', '05:55', '/music/jazz/jazz_fusion.mp3', 11300000, 890, TRUE),
(18, 'Saxo Dreams', '06:20', '/music/jazz/saxo_dreams.mp3', 12100000, 670, TRUE);

-- Hip-hop (Album 4)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(4, 'Street Life', '03:45', '/music/hiphop/street_life.mp3', 7200000, 3400, TRUE),
(4, 'Boom Bap', '04:02', '/music/hiphop/boom_bap.mp3', 7700000, 2900, TRUE),
(4, 'Flow Master', '03:38', '/music/hiphop/flow_master.mp3', 6900000, 4100, TRUE),
(19, 'Urban Legend', '03:55', '/music/hiphop/urban_legend.mp3', 7500000, 1800, TRUE),
(19, 'Beat Drop', '03:30', '/music/hiphop/beat_drop.mp3', 6700000, 2600, TRUE);

-- Electronic (Album 5)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(5, 'Synth Wave', '05:20', '/music/electronic/synth_wave.mp3', 10200000, 2100, TRUE),
(5, 'Digital Love', '04:45', '/music/electronic/digital_love.mp3', 9100000, 3500, TRUE),
(5, 'Bass Drop', '04:15', '/music/electronic/bass_drop.mp3', 8100000, 4700, TRUE),
(20, 'Neon Lights', '05:05', '/music/electronic/neon_lights.mp3', 9700000, 1900, TRUE),
(20, 'Cyber Space', '04:30', '/music/electronic/cyber_space.mp3', 8600000, 2800, TRUE);

-- Classical (Album 6)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(6, 'Symphony No.1', '12:30', '/music/classical/symphony1.mp3', 23900000, 450, FALSE),
(6, 'Piano Sonata', '08:45', '/music/classical/piano_sonata.mp3', 16700000, 680, FALSE),
(6, 'String Quartet', '09:20', '/music/classical/string_quartet.mp3', 17800000, 320, FALSE),
(6, 'Violin Solo', '07:15', '/music/classical/violin_solo.mp3', 13900000, 510, FALSE),
(6, 'Orchestra', '11:40', '/music/classical/orchestra.mp3', 22300000, 290, FALSE);

-- Reggae (Album 7)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(7, 'Island Vibes', '04:20', '/music/reggae/island_vibes.mp3', 8300000, 1200, TRUE),
(7, 'Jah Love', '03:55', '/music/reggae/jah_love.mp3', 7500000, 980, TRUE),
(7, 'Reggae Rhythm', '04:35', '/music/reggae/reggae_rhythm.mp3', 8800000, 1500, TRUE),
(7, 'One Love', '03:45', '/music/reggae/one_love.mp3', 7200000, 2100, TRUE),
(7, 'Sunset Beach', '04:10', '/music/reggae/sunset_beach.mp3', 8000000, 870, TRUE);

-- Metal (Album 8)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(8, 'Iron Fist', '05:45', '/music/metal/iron_fist.mp3', 11000000, 2300, TRUE),
(8, 'Metal Storm', '06:20', '/music/metal/metal_storm.mp3', 12100000, 1900, TRUE),
(8, 'Dark Lord', '05:30', '/music/metal/dark_lord.mp3', 10500000, 1500, TRUE),
(8, 'Rage Machine', '04:55', '/music/metal/rage_machine.mp3', 9400000, 2700, TRUE),
(8, 'Heavy Thunder', '05:15', '/music/metal/heavy_thunder.mp3', 10000000, 1100, TRUE);

-- Country (Album 9)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(9, 'Country Roads', '03:30', '/music/country/country_roads.mp3', 6700000, 3200, TRUE),
(9, 'Whiskey Night', '03:45', '/music/country/whiskey_night.mp3', 7200000, 1800, TRUE),
(9, 'Truck Song', '03:20', '/music/country/truck_song.mp3', 6400000, 2400, TRUE),
(9, 'Southern Heart', '04:05', '/music/country/southern_heart.mp3', 7800000, 1600, TRUE),
(9, 'Barn Dance', '03:35', '/music/country/barn_dance.mp3', 6900000, 2100, TRUE);

-- R&B (Album 10)
INSERT INTO canciones (album_id, titulo, duracion, ruta_archivo, tamano_archivo, num_reproducciones, permitir_descarga) VALUES
(10, 'Smooth Groove', '04:15', '/music/rnb/smooth_groove.mp3', 8100000, 2800, TRUE),
(10, 'Soul Sister', '03:50', '/music/rnb/soul_sister.mp3', 7300000, 3400, TRUE),
(10, 'Midnight Love', '04:30', '/music/rnb/midnight_love.mp3', 8600000, 4100, TRUE),
(10, 'R&B Classic', '03:40', '/music/rnb/rnb_classic.mp3', 7000000, 1900, TRUE),
(10, 'Velvet Voice', '04:00', '/music/rnb/velvet_voice.mp3', 7600000, 2500, TRUE);

-- ========================================
-- 5. RELACIONAR ÁLBUMES CON ARTISTAS
-- ========================================
INSERT INTO albumes_artistas (album_id, artista_id, rol) VALUES
(1, 1, 'Principal'),   -- Rock Revolution - The Rockers
(2, 2, 'Principal'),   -- Pop Sensation - Pop Princess
(3, 3, 'Principal'),   -- Jazz Nights - Jazz Masters
(4, 4, 'Principal'),   -- Urban Flow - MC Flow
(5, 5, 'Principal'),   -- Electronic Dreams - DJ Electron
(6, 6, 'Principal'),   -- Classical Masterpieces - Orchestra Simphonia
(7, 7, 'Principal'),   -- Reggae Vibes - Bob Reggaeman
(8, 8, 'Principal'),   -- Metal Mayhem - Metal Heads
(9, 9, 'Principal'),   -- Country Tales - Country Roads
(10, 10, 'Principal'), -- R&B Grooves - Smooth Soul
(11, 1, 'Productor'),  -- Greatest Hits - The Rockers
(12, 2, 'Productor'),  -- Summer Mix - Pop Princess
(13, 15, 'Principal'), -- Acoustic Live - Acoustic Sessions
(14, 5, 'Principal'),  -- Dance Party - DJ Electron
(15, 10, 'Productor'), -- Chill Out - Smooth Soul
(16, 1, 'Principal'),  -- Rock Anthems - The Rockers
(17, 2, 'Principal'),  -- Pop Classics - Pop Princess
(18, 3, 'Principal'),  -- Jazz Fusion - Jazz Masters
(19, 4, 'Principal'),  -- Hip Hop Beats - MC Flow
(20, 5, 'Principal');  -- Electronic Pulse - DJ Electron

-- ========================================
-- 6. RELACIONAR ÁLBUMES CON GÉNEROS
-- ========================================
INSERT INTO albumes_generos (album_id, genero_id) VALUES
(1, 1), (16, 1),  -- Rock albums
(2, 2), (17, 2),  -- Pop albums
(3, 3), (18, 3),  -- Jazz albums
(4, 4), (19, 4),  -- Hip-hop albums
(5, 5), (20, 5),  -- Electronic albums
(6, 6),           -- Classical albums
(7, 7),           -- Reggae albums
(8, 8),           -- Metal albums
(9, 9),           -- Country albums
(10, 10),         -- R&B albums
(11, 1), (11, 2), -- Greatest Hits (Rock y Pop)
(12, 2), (12, 5), -- Summer Mix (Pop y Electronic)
(13, 1), (13, 2), -- Acoustic Live (Rock y Pop)
(14, 5),          -- Dance Party (Electronic)
(15, 10), (15, 3); -- Chill Out (R&B y Jazz)

-- ========================================
-- 7. RELACIONAR CANCIONES CON ARTISTAS
-- ========================================
-- Relacionar cada canción con su artista principal
INSERT INTO canciones_artistas (cancion_id, artista_id, tipo_participacion) VALUES
-- Rock
(1, 1, 'Principal'), (2, 1, 'Principal'), (3, 1, 'Principal'), (4, 1, 'Principal'), (5, 1, 'Principal'),
-- Pop
(6, 2, 'Principal'), (7, 2, 'Principal'), (8, 2, 'Principal'), (9, 2, 'Principal'), (10, 2, 'Principal'),
-- Jazz
(11, 3, 'Principal'), (12, 3, 'Principal'), (13, 3, 'Principal'), (14, 3, 'Principal'), (15, 3, 'Principal'),
-- Hip-hop
(16, 4, 'Principal'), (17, 4, 'Principal'), (18, 4, 'Principal'), (19, 4, 'Principal'), (20, 4, 'Principal'),
-- Electronic
(21, 5, 'Principal'), (22, 5, 'Principal'), (23, 5, 'Principal'), (24, 5, 'Principal'), (25, 5, 'Principal'),
-- Classical
(26, 6, 'Principal'), (27, 6, 'Principal'), (28, 6, 'Principal'), (29, 6, 'Principal'), (30, 6, 'Principal'),
-- Reggae
(31, 7, 'Principal'), (32, 7, 'Principal'), (33, 7, 'Principal'), (34, 7, 'Principal'), (35, 7, 'Principal'),
-- Metal
(36, 8, 'Principal'), (37, 8, 'Principal'), (38, 8, 'Principal'), (39, 8, 'Principal'), (40, 8, 'Principal'),
-- Country
(41, 9, 'Principal'), (42, 9, 'Principal'), (43, 9, 'Principal'), (44, 9, 'Principal'), (45, 9, 'Principal'),
-- R&B
(46, 10, 'Principal'), (47, 10, 'Principal'), (48, 10, 'Principal'), (49, 10, 'Principal'), (50, 10, 'Principal');

-- Agregar algunos featuring
INSERT INTO canciones_artistas (cancion_id, artista_id, tipo_participacion) VALUES
(7, 4, 'Featuring'),   -- Dancing Queen feat. MC Flow
(22, 2, 'Featuring'),  -- Digital Love feat. Pop Princess
(34, 4, 'Featuring'),  -- One Love feat. MC Flow
(48, 3, 'Featuring');  -- Midnight Love feat. Jazz Masters

-- ========================================
-- 8. RELACIONAR CANCIONES CON GÉNEROS
-- ========================================
INSERT INTO canciones_generos (cancion_id, genero_id) VALUES
-- Rock (canciones 1-5)
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
-- Pop (canciones 6-10)
(6, 2), (7, 2), (8, 2), (9, 2), (10, 2),
-- Jazz (canciones 11-15)
(11, 3), (12, 3), (13, 3), (14, 3), (15, 3),
-- Hip-hop (canciones 16-20)
(16, 4), (17, 4), (18, 4), (19, 4), (20, 4),
-- Electronic (canciones 21-25)
(21, 5), (22, 5), (23, 5), (24, 5), (25, 5),
-- Classical (canciones 26-30)
(26, 6), (27, 6), (28, 6), (29, 6), (30, 6),
-- Reggae (canciones 31-35)
(31, 7), (32, 7), (33, 7), (34, 7), (35, 7),
-- Metal (canciones 36-40)
(36, 8), (37, 8), (38, 8), (39, 8), (40, 8),
-- Country (canciones 41-45)
(41, 9), (42, 9), (43, 9), (44, 9), (45, 9),
-- R&B (canciones 46-50)
(46, 10), (47, 10), (48, 10), (49, 10), (50, 10);

-- ========================================
-- 9. VERIFICAR QUE TODO SE INSERTÓ
-- ========================================
SELECT 'Géneros:' as Tabla, COUNT(*) as Total FROM generos
UNION ALL
SELECT 'Artistas:', COUNT(*) FROM artistas
UNION ALL
SELECT 'Álbumes:', COUNT(*) FROM albumes
UNION ALL
SELECT 'Canciones:', COUNT(*) FROM canciones
UNION ALL
SELECT 'Canciones-Géneros:', COUNT(*) FROM canciones_generos
UNION ALL
SELECT 'Canciones-Artistas:', COUNT(*) FROM canciones_artistas;

-- ========================================
-- 10. VER ALGUNAS CANCIONES CON SUS RELACIONES
-- ========================================
SELECT 
    c.titulo AS Cancion,
    a.titulo AS Album,
    ar.nombre AS Artista,
    g.nombre AS Genero,
    c.duracion AS Duracion
FROM canciones c
LEFT JOIN albumes a ON c.album_id = a.album_id
LEFT JOIN canciones_artistas ca ON c.cancion_id = ca.cancion_id AND ca.tipo_participacion = 'Principal'
LEFT JOIN artistas ar ON ca.artista_id = ar.artista_id
LEFT JOIN canciones_generos cg ON c.cancion_id = cg.cancion_id
LEFT JOIN generos g ON cg.genero_id = g.genero_id
LIMIT 20;