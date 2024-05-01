document.addEventListener('DOMContentLoaded', function () {
    const modoSwitch = document.getElementById('fondoSwitch');
    const body = document.body;

    // Verificar el estado guardado y aplicar el modo
    const modoActual = localStorage.getItem('modo');
    if (modoActual === 'oscuro') {
        aplicarModoOscuro();
        modoSwitch.checked = true;
    }

    // Cambiar el modo al hacer clic en el interruptor
    modoSwitch.addEventListener('change', function () {
        if (modoSwitch.checked) {
            aplicarModoOscuro();
            localStorage.setItem('modo', 'oscuro');
        } else {
            aplicarModoClaro();
            localStorage.setItem('modo', 'claro');
        }
    });

    function aplicarModoOscuro() {
        body.classList.add('fondo-oscuro');
    }

    function aplicarModoClaro() {
        body.classList.remove('fondo-oscuro');
    }
});