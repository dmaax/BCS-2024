// Calcular a gorjeta de N%

use std::io;

fn main() {
    let total_conta: f64 = 232.50;

    println!("Digite a gorjeta em porcentagem: ");
    let mut input = String::new();
    io::stdin().read_line(&mut input)
        .expect("Falha ao ler a linha");

    let gorjeta_porcentagem: f64 = input.trim().parse()
        .expect("Falha ao converter a entrada para número");

    let gorjeta_valor: f64 = total_conta * gorjeta_porcentagem / 100.0;

    println!("O valor da gorjeta é {}", gorjeta_valor);
}
