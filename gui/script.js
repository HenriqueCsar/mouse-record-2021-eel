async function run() {
    while (true){
    let resultado = await eel.positions_mouse()();
    console.log(resultado[0], resultado[1])}
}