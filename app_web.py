import streamlit as st
import math

# Configuración de la página
st.set_page_config(
    page_title="Calculadora Ollas UNACEM",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="expanded"
)

# BASE DE DATOS LOCAL DE 76 INSUMOS
CATALOGO_DB = {
    "Harina": {"costo": 7.70, "contenido": 1000},
    "Queso": {"costo": 20.00, "contenido": 1000},
    "Sal": {"costo": 1.90, "contenido": 1000},
    "Huevos": {"costo": 14.10, "contenido": 1000},
    "Azúcar": {"costo": 4.80, "contenido": 1000},
    "Mantequilla": {"costo": 12.00, "contenido": 500},
    "Aceite": {"costo": 14.90, "contenido": 1000},
    "Arroz": {"costo": 4.38, "contenido": 1000},
    "Papa": {"costo": 2.30, "contenido": 1000},
    "Ajo": {"costo": 4.63, "contenido": 1000},
    "Cebolla": {"costo": 1.78, "contenido": 1000},
    "Tomate": {"costo": 2.50, "contenido": 1000},
    "Ají amarillo": {"costo": 5.00, "contenido": 500},
    "Ají panca": {"costo": 5.00, "contenido": 500},
    "Rocoto": {"costo": 5.00, "contenido": 1000},
    "Culantro": {"costo": 2.00, "contenido": 100},
    "Perejil": {"costo": 2.00, "contenido": 100},
    "Huacatay": {"costo": 2.00, "contenido": 100},
    "Limón": {"costo": 2.12, "contenido": 1000},
    "Naranja": {"costo": 0.85, "contenido": 1000},
    "Palta": {"costo": 7.69, "contenido": 1000},
    "Zanahoria": {"costo": 2.08, "contenido": 1000},
    "Arveja": {"costo": 7.00, "contenido": 1000},
    "Choclo": {"costo": 2.74, "contenido": 1000},
    "Camote": {"costo": 1.43, "contenido": 1000},
    "Yuca": {"costo": 2.08, "contenido": 1000},
    "Plátano": {"costo": 1.85, "contenido": 1000},
    "Maíz cancha": {"costo": 5.75, "contenido": 1000},
    "Maíz mote": {"costo": 5.75, "contenido": 1000},
    "Chuño": {"costo": 8.00, "contenido": 1000},
    "Avena": {"costo": 6.50, "contenido": 1000},
    "Fideos": {"costo": 4.70, "contenido": 500},
    "Leche": {"costo": 10.45, "contenido": 1000},
    "Leche evaporada": {"costo": 5.20, "contenido": 400},
    "Leche condensada": {"costo": 7.90, "contenido": 393},
    "Crema de leche": {"costo": 8.00, "contenido": 200},
    "Yogur": {"costo": 9.30, "contenido": 1000},
    "Margarina": {"costo": 3.70, "contenido": 200},
    "Polvo de hornear": {"costo": 4.00, "contenido": 100},
    "Levadura": {"costo": 3.50, "contenido": 100},
    "Vainilla": {"costo": 3.50, "contenido": 100},
    "Canela": {"costo": 3.00, "contenido": 100},
    "Clavo de olor": {"costo": 4.00, "contenido": 100},
    "Pimienta": {"costo": 4.00, "contenido": 100},
    "Comino": {"costo": 3.00, "contenido": 100},
    "Orégano": {"costo": 3.00, "contenido": 100},
    "Sillao": {"costo": 5.00, "contenido": 500},
    "Vinagre": {"costo": 4.00, "contenido": 1000},
    "Pan rallado": {"costo": 6.00, "contenido": 500},
    "Frijol": {"costo": 6.50, "contenido": 1000},
    "Lentejas": {"costo": 4.40, "contenido": 1000},
    "Quinua": {"costo": 9.50, "contenido": 1000},
    "Harina de maíz": {"costo": 6.00, "contenido": 1000},
    "Harina de trigo": {"costo": 7.70, "contenido": 1000},
    "Papa seca": {"costo": 8.00, "contenido": 1000},
    "Pollo": {"costo": 10.00, "contenido": 1000},
    "Carne de res": {"costo": 30.00, "contenido": 1000},
    "Carne molida": {"costo": 28.00, "contenido": 1000},
    "Cerdo": {"costo": 18.00, "contenido": 1000},
    "Tocino": {"costo": 18.00, "contenido": 500},
    "Jamón": {"costo": 15.00, "contenido": 500},
    "Salchicha": {"costo": 11.00, "contenido": 600},
    "Chorizo": {"costo": 15.00, "contenido": 500},
    "Atún": {"costo": 7.00, "contenido": 150},
    "Pescado": {"costo": 15.00, "contenido": 1000},
    "Champiñones": {"costo": 8.00, "contenido": 200},
    "Aceituna": {"costo": 8.00, "contenido": 500},
    "Mayonesa": {"costo": 6.00, "contenido": 500},
    "Ketchup": {"costo": 7.00, "contenido": 500},
    "Cocoa": {"costo": 10.00, "contenido": 200},
    "Chocolate": {"costo": 15.02, "contenido": 500},
    "Miel": {"costo": 9.50, "contenido": 500},
    "Maní": {"costo": 14.80, "contenido": 1000},
    "Coco rallado": {"costo": 8.00, "contenido": 250},
    "Queso mozzarella": {"costo": 18.00, "contenido": 500},
    "Queso parmesano": {"costo": 20.00, "contenido": 250}
}

st.title("🍲 Calculadora de Punto de Equilibrio")
st.subheader("Proyecto Ollas UNACEM")

# --- BARRA LATERAL: VARIABLES DE ENTRADA ---
with st.sidebar:
    st.header("⚙️ Variables de Entrada")
    nombre_snack = st.text_input("Nombre del Snack", "Cachanga")
    horas_trabajo = st.number_input("Tiempo de Trabajo (Horas)", min_value=0.0, value=4.0, step=0.5)
    cocineras = st.number_input("N° de Cocineras", min_value=1, value=4, step=1)
    sueldo_hora = st.number_input("Sueldo por Hora (S/)", min_value=0.0, value=5.0, step=0.5)
    costo_agua = st.number_input("Consumo de Agua (S/)", min_value=0.0, value=10.0, step=1.0)
    costo_lena = st.number_input("Costo de Leña (S/)", min_value=0.0, value=15.0, step=1.0)
    utilidad_deseada = st.number_input("Utilidad Deseada (S/)", min_value=0.0, value=100.0, step=10.0)
    porcion_g = st.number_input("Porción Unitaria (g)", min_value=1.0, value=250.0, step=10.0)
    precio_venta = st.number_input("Precio de Venta (S/)", min_value=0.1, value=4.0, step=0.5)

# --- SECCIÓN PRINCIPAL: SELECCIÓN DE INSUMOS ---
st.header("📋 Selección de Insumos del Lote")

# Inicializar estado de la receta si no existe
if "receta" not in st.session_state:
    st.session_state.receta = {
        "Harina": 1, "Queso": 1, "Sal": 1,
        "Huevos": 1, "Azúcar": 1, "Mantequilla": 1, "Aceite": 1
    }

# Selección múltiple con buscador desplegable
insumos_seleccionados = st.multiselect(
    "Selecciona o busca ingredientes (Catálogo de 76 productos):",
    options=sorted(list(CATALOGO_DB.keys())),
    default=list(st.session_state.receta.keys())
)

# Ajuste dinámico de la cantidad de paquetes por insumo
cantidades_paquetes = {}
if insumos_seleccionados:
    st.write("##### Configuración de Paquetes Usados:")
    cols = st.columns(min(len(insumos_seleccionados), 3))
    for idx, insumo in enumerate(insumos_seleccionados):
        col = cols[idx % 3]
        def_val = st.session_state.receta.get(insumo, 1)
        cantidades_paquetes[insumo] = col.number_input(
            f"Paquetes de {insumo}:",
            min_value=1,
            value=int(def_val),
            step=1,
            key=f"pqt_{insumo}"
        )

# --- CÁLCULOS CONTABLES ---
costo_total_lote = 0.0
gramos_totales_lote = 0.0

for insumo, pqt_count in cantidades_paquetes.items():
    db = CATALOGO_DB[insumo]
    costo_total_lote += pqt_count * db["costo"]
    gramos_totales_lote += pqt_count * db["contenido"]

cantidad_producida = int(gramos_totales_lote // porcion_g) if porcion_g > 0 else 0
cvu = (costo_total_lote / cantidad_producida) if cantidad_producida > 0 else 0.0
costos_fijos = (horas_trabajo * cocineras * sueldo_hora) + costo_agua + costo_lena
margen = precio_venta - cvu

if margen > 0:
    pe_unidades = math.ceil((costos_fijos + utilidad_deseada) / margen)
    pe_soles = pe_unidades * precio_venta
else:
    pe_unidades = "REVISAR PRECIO"
    pe_soles = 0.0

# --- PANEL DE RESULTADOS ---
st.divider()
st.header("📊 Resultados Contables")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Costo Lote (C22)", f"S/ {costo_total_lote:.2f}")
m2.metric("Producidos (D22)", f"{cantidad_producida} snacks")
m3.metric("Costo Var. Unitario (CVu)", f"S/ {cvu:.2f}")
m4.metric("Costos Fijos Totales (CF)", f"S/ {costos_fijos:.2f}")

st.subheader("🎯 Punto de Equilibrio con Utilidad Deseada")
res_col1, res_col2 = st.columns(2)

with res_col1:
    if isinstance(pe_unidades, int):
        st.success(f"### **{pe_unidades} snacks** a vender")
    else:
        st.error("### **Margen insuficiente** (Aumentar precio de venta)")

with res_col2:
    if isinstance(pe_unidades, int):
        st.info(f"### **S/ {pe_soles:.2f}** recaudación meta")
    else:
        st.warning("### **S/ 0.00**")