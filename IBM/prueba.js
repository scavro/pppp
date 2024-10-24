let libro ={
    titulo: 'Las legiones malditas',
    autor: 'santiago posteguillo',
    informacion:function(){
        return "El libro " + this.titulo + " esta escrito por " + this.autor;
    }
}

console.log(typeof libro.informacion)
console.log(libro.informacion())
console.log(typeof libro.informacion())
function calculo(x){
    return x
}

console.log(calculo(undefined))

let intentos = [1,5,10,12]
console.log(intentos[3])

let siglas = [
    'fmi',
    'bid',
    ['onu','unesco'],
    'birf'
]
console.log(siglas[3][1])

