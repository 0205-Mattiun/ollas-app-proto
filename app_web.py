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
    "Harina": {"costo": 6.00, "contenido": 1000},
    "Queso": {"costo": 18.00, "contenido": 1000},
    "Sal": {"costo": 2.00, "contenido": 1000},
    "Huevos": {"costo": 6.50, "contenido": 1000},
    "Azúcar": {"costo": 3.50, "contenido": 1000},
    "Mantequilla": {"costo": 12.00, "contenido": 500},
    "Aceite": {"costo": 10.00, "contenido": 900},
    "Arroz": {"costo": 4.00, "contenido": 1000},
    "Papa": {"costo": 2.50, "contenido": 1000},
    "Ajo": {"costo": 5.00, "contenido": 500},
    "Cebolla": {"costo": 2.00, "contenido": 500},
    "Tomate": {"costo": 2.50, "contenido": 500},
    "Ají amarillo": {"costo": 5.00, "contenido": 500},
    "Ají panca": {"costo": 5.00, "contenido": 500},
    "Rocoto": {"costo": 3.00, "contenido": 500},
    "Culantro": {"costo": 2.00, "contenido": 100},
    "Perejil": {"costo": 2.00, "contenido": 100},
    "Huacatay": {"costo": 2.00, "contenido": 100},
    "Limón": {"costo": 2.00, "contenido": 500},
    "Naranja": {"costo": 3.00, "contenido": 500},
    "Palta": {"costo": 6.00, "contenido": 1000},
    "Zanahoria": {"costo": 2.00, "contenido": 1000},
    "Arveja": {"costo": 6.00, "contenido": 1000},
    "Choclo": {"costo": 10.00, "contenido": 1000},
    "Camote": {"costo": 2.00, "contenido": 1000},
    "Yuca": {"costo": 5.00, "contenido": 1000},
    "Plátano": {"costo": 4.00, "contenido": 1000},
    "Maíz cancha": {"costo": 5.50, "contenido": 1000},
    "Maíz mote": {"costo": 7.00, "contenido": 1000},
    "Chuño": {"costo": 5.00, "contenido": 1000},
    "Avena": {"costo": 5.50, "contenido": 500},
    "Fideos": {"costo": 3.50, "contenido": 450},
    "Leche": {"costo": 4.00, "contenido": 400},
    "Leche evaporada": {"costo": 4.00, "contenido": 400},
    "Leche condensada": {"costo": 4.90, "contenido": 180},
    "Crema de leche": {"costo": 6.00, "contenido": 200},
    "Yogur": {"costo": 7.50, "contenido": 1000},
    "Margarina": {"costo": 3.90, "contenido": 250},
    "Polvo de hornear": {"costo": 2.00, "contenido": 25},
    "Levadura": {"costo": 11.50, "contenido": 500},
    "Vainilla": {"costo": 3.00, "contenido": 100},
    "Canela": {"costo": 2.00, "contenido": 100},
    "Clavo de olor": {"costo": 2.00, "contenido": 100},
    "Pimienta": {"costo": 5.90, "contenido": 50},
    "Comino": {"costo": 4.00, "contenido": 25},
    "Orégano": {"costo": 3.00, "contenido": 21},
    "Sillao": {"costo": 2.00, "contenido": 160},
    "Vinagre": {"costo": 1.50, "contenido": 125},
    "Pan rallado": {"costo": 3.80, "contenido": 250},
    "Frijol": {"costo": 7.50, "contenido": 500},
    "Lentejas": {"costo": 5.50, "contenido": 500},
    "Quinua": {"costo": 7.50, "contenido": 1000},
    "Harina de maíz": {"costo": 7.00, "contenido": 1000},
    "Harina de trigo": {"costo": 7.70, "contenido": 1000},
    "Papa seca": {"costo": 8.00, "contenido": 500},
    "Pollo": {"costo": 12.00, "contenido": 1000},
    "Carne de res": {"costo": 26.00, "contenido": 1000},
    "Carne molida": {"costo": 20.00, "contenido": 1000},
    "Cerdo": {"costo": 15.00, "contenido": 1000},
    "Tocino": {"costo": 18.00, "contenido": 500},
    "Jamón": {"costo": 15.00, "contenido": 500},
    "Salchicha": {"costo": 11.00, "contenido": 500},
    "Chorizo": {"costo": 15.00, "contenido": 500},
    "Atún": {"costo": 6.00, "contenido": 150},
    "Pescado": {"costo": 9.00, "contenido": 1000},
    "Champiñones": {"costo": 8.00, "contenido": 200},
    "Aceituna": {"costo": 12.00, "contenido": 400},
    "Mayonesa": {"costo": 18.00, "contenido": 850},
    "Ketchup": {"costo": 7.00, "contenido": 380},
    "Cocoa": {"costo": 3.20, "contenido": 40},
    "Chocolate": {"costo": 20.00, "contenido": 200},
    "Miel": {"costo": 15.50, "contenido": 250},
    "Maní": {"costo": 10.00, "contenido": 1000},
    "Coco rallado": {"costo": 4.00, "contenido": 100},
    "Queso mozzarella": {"costo": 6.00, "contenido": 500},
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

opciones_catalogo = sorted(list(CATALOGO_DB.keys()))

insumos_seleccionados = st.multiselect(
    "Selecciona o busca ingredientes (Catálogo de 76 productos):",
    options=opciones_catalogo,
    default=list(st.session_state.receta.keys()),
    format_func=lambda item: f"{item} ({CATALOGO_DB[item]['contenido']} g/u)"
)

# Ajuste dinámico de la cantidad de paquetes por insumo
cantidades_paquetes = {}
if insumos_seleccionados:
    st.write("##### Configuración de Paquetes Usados:")
    cols = st.columns(min(len(insumos_seleccionados), 3))
    for idx, insumo in enumerate(insumos_seleccionados):
        col = cols[idx % 3]
        def_val = st.session_state.receta.get(insumo, 1)
        
        g_unitario = CATALOGO_DB[insumo]['contenido']
        costo_unitario = CATALOGO_DB[insumo]['costo']
        
        cantidades_paquetes[insumo] = col.number_input(
            f"N° Paquetes: {insumo}",
            min_value=1,
            value=int(def_val),
            step=1,
            key=f"pqt_{insumo}",
            help=f"Contenido: {g_unitario} g por paquete | Costo: S/ {costo_unitario:.2f}"
        )
        g_totales_item = cantidades_paquetes[insumo] * g_unitario
        costo_total_item = cantidades_paquetes[insumo] * costo_unitario
        col.caption(f"📦 Paquete: **{g_unitario} g** (S/ {costo_unitario:.2f})  \n⚖️ Total: **{g_totales_item} g** | **S/ {costo_total_item:.2f}**")

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
