// 1. Informe se uma pessoa tem o mesmo nome que você

use std::io;

fn main() {
    println!("Digite o primeiro nome: ");
    let mut nome_a = String::new();

    io::stdin()
        .read_line(&mut nome_a)
        .expect("Falha ao ler a linha");

    println!("Digite o segundo nome: ");
    let mut nome_b = String::new();

    io::stdin()
        .read_line(&mut nome_b)
        .expect("Falha ao ler a linha");
    
    if nome_a == nome_b {
        println!("Os dois nomes são iguais");
    } else {
        println!("Os nomes não são iguais");
    }
}