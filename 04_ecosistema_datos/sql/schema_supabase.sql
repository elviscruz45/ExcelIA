-- Schema Supabase para Módulo B — Ecosistema de Datos
-- Ejecutar en SQL Editor de Supabase

CREATE TABLE IF NOT EXISTS equipos (
    id SERIAL PRIMARY KEY,
    codigo TEXT NOT NULL UNIQUE,
    area TEXT NOT NULL,
    tipo TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS lecturas_pi (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    tag TEXT NOT NULL,
    valor DOUBLE PRECISION NOT NULL,
    unidad TEXT NOT NULL,
    quality TEXT NOT NULL DEFAULT 'GOOD',
    equipo_codigo TEXT
);

CREATE TABLE IF NOT EXISTS eventos_mantenimiento (
    id SERIAL PRIMARY KEY,
    equipo_id INTEGER REFERENCES equipos(id),
    inicio TIMESTAMPTZ NOT NULL,
    fin TIMESTAMPTZ NOT NULL,
    modo_falla TEXT NOT NULL,
    mttr_horas DOUBLE PRECISION NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_lecturas_timestamp ON lecturas_pi(timestamp);
CREATE INDEX IF NOT EXISTS idx_lecturas_tag ON lecturas_pi(tag);
CREATE INDEX IF NOT EXISTS idx_lecturas_quality ON lecturas_pi(quality);
CREATE INDEX IF NOT EXISTS idx_eventos_equipo ON eventos_mantenimiento(equipo_id);

-- RLS opcional: deshabilitar para curso o permitir lectura con anon key
ALTER TABLE equipos ENABLE ROW LEVEL SECURITY;
ALTER TABLE lecturas_pi ENABLE ROW LEVEL SECURITY;
ALTER TABLE eventos_mantenimiento ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Lectura pública equipos" ON equipos FOR SELECT USING (true);
CREATE POLICY "Lectura pública lecturas" ON lecturas_pi FOR SELECT USING (true);
CREATE POLICY "Lectura pública eventos" ON eventos_mantenimiento FOR SELECT USING (true);

CREATE POLICY "Insert equipos curso" ON equipos FOR INSERT WITH CHECK (true);
CREATE POLICY "Insert lecturas curso" ON lecturas_pi FOR INSERT WITH CHECK (true);
CREATE POLICY "Insert eventos curso" ON eventos_mantenimiento FOR INSERT WITH CHECK (true);
