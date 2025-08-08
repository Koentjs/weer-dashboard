from sqlalchemy import create_engine, text

DB_URL= "postgresql://postgres:L%40FM%23%21B9a%2ARv.qr@db.tejivmdhnckskbtwlzso.supabase.co:5432/postgres"
engine = create_engine(DB_URL)

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connectie gelukt!", result.fetchone())
except Exception as e:
    print("Fout bij verbinden:", e)