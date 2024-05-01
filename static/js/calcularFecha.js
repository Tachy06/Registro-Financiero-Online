// Obtener la fecha actual
const fechaActual = new Date();

// Obtener el primer día del mes actual
const primerDiaMes = new Date(fechaActual.getFullYear(), fechaActual.getMonth(), 1);
const fechaMin = primerDiaMes.toISOString().split('T')[0];

// Obtener el último día del mes actual
const ultimoDiaMes = new Date(fechaActual.getFullYear(), fechaActual.getMonth() + 1, 0);
const fechaMax = ultimoDiaMes.toISOString().split('T')[0];

// Establecer el rango de fechas
document.getElementById('fecha').min = fechaMin;
document.getElementById('fecha').max = fechaMax;