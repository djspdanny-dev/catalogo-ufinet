import pandas as pd
import json

archivo = "CATALOGO UFINET 1.0.xlsx"

equipo = pd.read_excel(
    archivo,
    sheet_name="EQUIPO"
)

material = pd.read_excel(
    archivo,
    sheet_name="MATERIAL"
)

equipo["TIPO"] = "Equipo"
material["TIPO"] = "Material"

df = pd.concat([
    equipo,
    material
])

df = df.drop_duplicates(
    subset=[
        "PERSONALIZADO",
        "DESCRIPCION"
    ]
)

productos = []

for _, r in df.iterrows():

    try:
        codigo = str(
            int(r["PERSONALIZADO"])
        ).zfill(6)
    except:
        codigo = str(
            r["PERSONALIZADO"]
        )

    productos.append({

        "PERSONALIZADO":
        codigo,

        "MARCA":
        str(r["MARCA"]),

        "DESCRIPCION":
        str(r["DESCRIPCION"]),

        "PRECIO":
"${:,.2f}".format(float(r["PRECIO UNITARIO"]))

        "TIPO":
        str(r["TIPO"])

    })

with open(
    "productos.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        productos,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Se generaron {len(productos)} productos"
)

