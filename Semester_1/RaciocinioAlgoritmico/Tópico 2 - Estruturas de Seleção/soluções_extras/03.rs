// Informe o dia da semana a partir de um número entre 1 e 7. Exemplo, 1- Domingo, 2- Segunda etc. Se digitar outro valor deve aparecer “valor inválido”)

use std::io;

fn main() {
    println!("Digite um número entre 1 e 7: ");

    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler entrada");

    let numero: u32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Valor inválido!");
            return;
        }
    };
    
    match numero {
        1 => println!("Domingo"),
        2 => println!("Segunda"),
        3 => println!("Terça"),
        4 => println!("Quarta"),
        5 => println!("Quinta"),
        6 => println!("Sexta"),
        7 => println!("Sábado"),
        _ => println!("Valor inválido"),
    }
    
}