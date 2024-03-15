// Informe se a pessoa digitou uma vogal ou consoante

use std::io;

fn main() {
    println!("Digite uma letra: ");
    let mut input = String::new();

    io::stdin()
        .read_line(&mut input)
        .expect("Falha ao ler a linha");
    
    let caracter = input.trim().chars().next();

    match caracter {
        Some('a') | Some('e') | Some('i') | Some('o') | Some('u') | Some('A') | Some('E') | Some('I') | Some('O') | Some('U') => {
            println!("Vogal");
        },
        Some(_) => {
            println!("Consoante");
        },
        None => {
            println!("Nenhuma entrada definida");
        }
    }

}