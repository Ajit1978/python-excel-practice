import pandas as pd

df = pd.DataFrame(
    {
        "X": [
            "English",
            "Hindi",
            "Marathi",
            "Math-1",
            "Math-2",
            "Sci-1",
            "Sci-2",
            "S.S.-1",
            "S.S.-2",    
        ],
        "Y": [90, 95, 92, 96, 94, 98, 97, 93, 91],        
    }
)
df = df.to_excel("1 excelWrite.xlsx")
print(df)