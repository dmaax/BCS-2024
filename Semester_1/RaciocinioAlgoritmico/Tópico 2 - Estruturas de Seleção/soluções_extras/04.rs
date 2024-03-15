// Informe o maior número entre dois números quaisquer

use std::io;

fn main() {
    
    fn ler_numero(prompt: &str) -> i32 {
        println!("{}", prompt);
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Falha ao ler linha");
        input.trim().parse()
            .expect("Valor inválido")
    }

    let numero1 = ler_numero("Digite o primeiro número:");
    let numero2 = ler_numero("Digite o segundo número:");

    match numero1.partial_cmp(&numero2) {
        Some(std::cmp::Ordering::Greater) => {
            println!("O maior número é {numero1}");
        },
        Some(std::cmp::Ordering::Less) => {
            println!("O maior número é {numero2}");
        },
        Some(std::cmp::Ordering::Equal) => {
            println!("Os números {numero1} e {numero2} são iguais");
        },
        _ => {
            println!("Valor inválido")
        }
    };

}