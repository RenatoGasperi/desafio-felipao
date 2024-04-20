class heroi {
    constructor(nome, idade, tipo) {
        this.nome = nome
        this.idade = idade
        this.tipo = tipo
        }
    
    exibirMensagem() {
            switch (this.tipo) {
                case "mago":
                    var ataque = "magia"
                    console.log(`O ${this.tipo} atacou usando ${ataque}`)
                    break;
                case "guerreiro":
                    var ataque = "espada"
                    console.log(`O ${this.tipo} atacou usando ${ataque}`)
                    break;
                case "monge":
                    var ataque = "artes marciais"
                    console.log(`O ${this.tipo} atacou usando ${ataque}`)
                    break;
                case "monge":
                    var ataque = "shuriken"
                    console.log(`O ${this.tipo} atacou usando ${ataque}`)
                    break;
                default:
                    break;
                
            }
            
        }
}

primeiroHeroi = new heroi("renato", 40, "guerreiro")

primeiroHeroi.exibirMensagem()
