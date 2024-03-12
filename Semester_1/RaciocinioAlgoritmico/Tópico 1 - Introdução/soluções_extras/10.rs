// Calcule a metragem quadrada de uma casa com N pavimentos

use std::io;

fn main() {
  let largura = 10.0;
  let comprimento = 20.0;

  println!("Digite o número de pavimentos: ");
  let mut input = String::new();
  io::stdin().read_line(&mut input)
      .expect("Falha ao ler a linha");

  let pavimentos: f64 = input.trim().parse()
    .expect("Falha ao converter a entrada para número");

  let area_total: f64 = largura * comprimento * pavimentos;

  println!("A metragem quadrada é de {}", area_total)
}