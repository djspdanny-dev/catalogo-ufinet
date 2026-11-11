import pandas as pd
import json

archivo = "CATALOGO UFINET 1.0.xlsx"

# Leer hojas
equipo = pd.read_excel(
    archivo,
    sheet_name="EQUIPO"
)

material = pd.read_excel(
    archivo,
    sheet_name="MATERIAL"
)

# Agregar tipo
equipo["TIPO"] = "Equipo"
material["TIPO"] = "Material"

# Unir hojas
df = pd.concat([
    equipo,
    material
])

# Eliminar duplicados
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

    try:
        precio = float(
            r["PRECIO UNITARIO"]
        )

        precio_formateado = (
            "$" +
            "{:,.2f}".format(precio)
        )

    except:
        precio_formateado = "$0.00"

    productos.append({

        "PERSONALIZADO":
        codigo,

        "MARCA":
        str(r["MARCA"]),

        "DESCRIPCION":
        str(r["DESCRIPCION"]),

        "PRECIO":
        precio_formateado,

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
