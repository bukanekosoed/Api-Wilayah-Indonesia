from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Directory for HTML templates

# Function to read CSV files and convert them into lists
def baca_csv_provinsi():
    try:
        df = pd.read_csv('data/provinsi.csv', sep=';')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error saat membaca CSV provinsi: {e}")
        return []

def baca_csv_kabupaten():
    try:
        df = pd.read_csv('data/kabupaten.csv', sep=';')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error saat membaca CSV kabupaten: {e}")
        return []

def baca_csv_kecamatan():
    try:
        df = pd.read_csv('data/kecamatan.csv',sep=';')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error saat membaca CSV kecamatan: {e}")
        return []

def baca_csv_desa():
    try:
        df = pd.read_csv('data/desa.csv',sep=';')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error saat membaca CSV desa: {e}")
        return []

def baca_csv_kodepos():
    try:
        df = pd.read_csv('data/kodepos.csv', sep=';')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error saat membaca CSV kode pos: {e}")
        return []


# Load data from CSV into memory
provinsi_data = baca_csv_provinsi()
kabupaten_data = baca_csv_kabupaten()
kecamatan_data = baca_csv_kecamatan()
desa_data = baca_csv_desa()
kodepos_data = baca_csv_kodepos()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "provinsi_data": provinsi_data  # Ensure this line exists
    })

@app.get("/provinsi", response_model=List[dict])
def get_provinsi(kode: Optional[str] = None, nama: Optional[str] = None):
    """API untuk mendapatkan daftar provinsi berdasarkan kode atau nama"""
    
    results = provinsi_data
    
    if kode:
        results = [prov for prov in results if str(prov["kode_provinsi"]) == str(kode)]
    
    
    return results

@app.get("/kabupaten", response_model=List[dict])
def get_kabupaten(kode_provinsi: str):
    """API untuk mendapatkan daftar kabupaten berdasarkan kode provinsi"""
    
    kabupaten_filtered = [kab for kab in kabupaten_data if str(kab["kode_provinsi"]) == str(kode_provinsi)]
    
    if not kabupaten_filtered:
        raise HTTPException(status_code=404, detail="Kabupaten tidak ditemukan untuk kode provinsi ini")
    
    return kabupaten_filtered

@app.get("/kecamatan", response_model=List[dict])
def get_kecamatan(kode_kabupaten: str):
    """API untuk mendapatkan daftar kecamatan berdasarkan kode kabupaten"""
    
    kecamatan_filtered = [kec for kec in kecamatan_data if str(kec["kode_kabupaten"]) == str(kode_kabupaten)]
    
    if not kecamatan_filtered:
        raise HTTPException(status_code=404, detail="Kecamatan tidak ditemukan untuk kode kabupaten ini")
    
    return kecamatan_filtered

@app.get("/desa", response_model=List[dict])
def get_desa(kode_kecamatan: str):
    """API untuk mendapatkan daftar desa berdasarkan kode kecamatan"""
    
    desa_filtered = [desa for desa in desa_data if str(desa["kode_kecamatan"]) == str(kode_kecamatan)]
    
    if not desa_filtered:
        raise HTTPException(status_code=404, detail="Desa tidak ditemukan untuk kode kecamatan ini")
    
    # Add the corresponding postal code to each desa
    
    return desa_filtered

@app.get("/kodepos", response_model=List[dict])
def get_kodepos(kode_desa: str):
    kodepos = [kp for kp in kodepos_data if str(kp["kode_desa"]) == str(kode_desa)]
    if not kodepos:
        raise HTTPException(status_code=404, detail="Kode Pos tidak ditemukan")
    
    return kodepos


