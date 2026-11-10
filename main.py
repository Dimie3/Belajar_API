from fastapi import FastAPI, HTTPException
import pandas as pd

#create object FastAPI
app = FastAPI() 

# endpoint -> get data halaman utama
@app.get("/")
def handleGetData():
    # .... ada proses yang berjalan

    return{
        "message": "HELLO!"
    }

#end point -> get data from csv
@app.get("/data")
def handleCSV():
    #1 baca data dari csv
    df = pd.read_csv('mock-employees.csv')

    #2 ubah dataframe -> json
    df = df.to_dict(orient='records')
    #3 return json
    return {
        "data": df
    }

#endpoint -> get data by id (filter)
@app.get("/data/{id}") #bentuk parameter di url
def handFilter(id: int):
    #1. baca data csv
    df = pd.read_csv('mock-employees.csv')

    #2 filter data col:id
    df = df[df["id"]==id]

    #2.1 error handling: ketika hasil filter =kosong
    #-> tampilkan pesan error
    if df.empty == True:
        raise HTTPException(status_code=404, detail="data tidak ditemukan!") #error di api pake raise bukan return

    #3 ubah dataframe->json
    df = df.to_dict(orient='records')
        
    #4 return json
    return {
            "data": df
        }