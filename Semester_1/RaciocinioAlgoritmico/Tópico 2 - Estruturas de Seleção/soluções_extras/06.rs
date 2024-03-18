// Informe se um ano é bissexto ou não.

use std::io;

fn main() {
    println!("Digite um ano para verificar se é bissexto: ");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler linha");

    let ano: u32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Valor inválido!");
            return;
        }
    };

    if ano % 4 == 0 {
        println!("{ano} é Bissexto");
    } else {
        println!("{ano} não é bissexto")
    }
}